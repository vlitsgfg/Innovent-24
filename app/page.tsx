"use client";

import { SyncLoader } from "react-spinners";
import { useState } from "react";
import { CodeBlock, atomOneDark } from "react-code-blocks";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [submitted, setSubmitted] = useState(false);

  const API_KEY = "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";

  const radioButtons = new Array(6).fill(false);

  async function hanldeSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setSubmitted(true);

    const res = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${API_KEY}`,
      },
      body: JSON.stringify({
        model: "gpt-3.5-turbo",
        messages: [{ role: "assistant", content: prompt }],
      }),
    });

    const data = await res.json();
    setLoading(false);
    setSubmitted(false);
    setResponse(data.choices[0].message.content);

    const splitted = data.choices[0].message.content.split("```");
    let arr: string[] = [];

    for (let i = 1; i < splitted.length - 1; i++) {
      arr.push(splitted[i]);
    }
    setResponse(arr[0]);
  }

  return (
    <main className="min-h-screen max-w-[1000px] mx-auto">
      {submitted && loading && <SyncLoader color="#fff" />}
      <form onSubmit={hanldeSubmit} className="ml-[25%]">
        <div className="mt-8 ml-20 col">
          <div className="flex gap-4 ">
            <input type="radio" id="c++" />
            <label htmlFor="c++" className="mr-14">
              C++
            </label>
            <input type="radio" id="python" />
            <label htmlFor="python">Python</label>
            <input type="radio" id="java" />
            <label htmlFor="java">Java</label>
          </div>
          <br />
          <div className="flex gap-4">
            <input type="radio" id="javascript" />
            <label htmlFor="c++">JavaScript</label>
            <input type="radio" id="rust" />
            <label htmlFor="rust" className="mr-6">
              Rust
            </label>
            <input type="radio" id="go" />
            <label htmlFor="go">Go Lang</label>
          </div>
        </div>
        <br />
        <input
          className="rounded-lg placeholder:ml-4 px-2 py-2 w-[400px] bg-zinc-800 mt-2 text-white"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <button className="ml-4 bg-zinc-900 px-4 py-2 rounded-lg hover:bg-white hover:text-black">
          Generate
        </button>
      </form>
      {!loading && (
        <div className="font-poppins-800 mt-6">
          {response.length > 0 ? (
            <CodeBlock language={"java"} text={response} theme={atomOneDark} />
          ) : (
            <h1>This is not a Programming related concept..</h1>
          )}
        </div>
      )}
    </main>
  );
}
