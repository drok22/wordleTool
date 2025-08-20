import { useState } from "react";
import { Row, Form, Button } from "react-bootstrap";

const handleKnownUpdate = (
  e: React.ChangeEvent<HTMLInputElement>,
  index: number
) => {
  if (e.target.value.length > 0) {
    const form = e.target.form;
    if (!form) return;

    const next = form.elements[index + 1] as HTMLElement | undefined;
    next?.focus();
  }
};

function App() {
  const [known, setKnown] = useState(["_", "_", "_", "_", "_"]);
  const [nonmatching, setNonMatching] = useState(["", "", "", "", ""]);
  const [eliminated, setEliminated] = useState("");
  const [possibleGuesses, setPossibleGuesses] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const filterWordsRequest = async () => {
    const filterQuery = new URLSearchParams({
      known: known.join(","),
      nonmatching: nonmatching.join(","),
      eliminated: eliminated,
    });
    setLoading(true);
    try {
      const response = await fetch(
        `http://localhost:8000/filter_words?${filterQuery.toString()}`,
        {
          method: "GET",
        }
      );
      if (!response.ok) {
        throw new Error("HTTP Error " + response.status);
      }
      const data = await response.json();
      setPossibleGuesses(data.words);
      setLoading(false);
      setError(null);
      console.log("words received: " + data.words);
    } catch (err) {
      setPossibleGuesses([]);
      setLoading(false);
      setError(err instanceof Error ? err.message : String(err));
    }
  };

  return (
    <div
      className="bg-dark text-light min-vh-100 d-flex flex-column align-items-start justify-content-start"
      style={{ padding: "2rem" }}
    >
      <h1>Wordle Helper</h1>
      <p>
        Fill in the info based on your guesses below and get a list of possible
        Wordle guesses!
      </p>
      <Form>
        <Row>
          <Form.Label>Known Letter Locations (Green Letters)</Form.Label>
        </Row>
        <Row>
          {known.map((letter, index) => (
            <Form.Control
              key={index}
              type="text"
              maxLength={1}
              style={{ width: "1.5em", textAlign: "center" }}
              value={letter === "_" ? "" : letter}
              onChange={(changed) => {
                const newLetters = [...known];
                newLetters[index] = changed.target.value || "_";
                setKnown(newLetters);
                handleKnownUpdate(
                  changed as React.ChangeEvent<HTMLInputElement>,
                  index
                );
              }}
            />
          ))}
        </Row>
        <Row>
          <Form.Label>
            Nonmatching Letter Locations (Yellow Lettes) (ABCDXYZ)
          </Form.Label>
        </Row>
        <Row>
          {nonmatching.map((group, index) => (
            <Form.Control
              key={index}
              type="text"
              maxLength={6}
              style={{ width: "5em", textAlign: "center" }}
              value={group}
              onChange={(changed) => {
                const newLetters = [...nonmatching];
                newLetters[index] = changed.target.value;
                setNonMatching(newLetters);
              }}
            />
          ))}
        </Row>
        <Row>
          <Form.Label>Eliminated Letters (Black Letters)</Form.Label>
        </Row>
        <Row>
          <Form.Control
            type="text"
            maxLength={26}
            value={eliminated}
            onChange={(changed) => {
              setEliminated(changed.target.value);
            }}
          />
        </Row>
        <Row>
          <Button
            variant="primary"
            onClick={() => {
              filterWordsRequest();
            }}
          >
            Submit
          </Button>
        </Row>
      </Form>

      {loading && <p>Loading...</p>}
      {error && <p className="text-danger">{error}</p>}
      {possibleGuesses.length > 0 && (
        <div>
          <h2>Possible Guesses</h2>
          <ul>
            {possibleGuesses.map((guess, index) => (
              <li key={index}>{guess}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
