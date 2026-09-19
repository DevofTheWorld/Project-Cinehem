import { useState } from 'react'

function App() {
  const [file, setFile] = useState(null)
  const [roast, setRoast] = useState("")
  const [loading, setLoading] = useState(false)

  const handleUpload = async (e) => {
    e.preventDefault()
    if (!file) return alert("Upload a CSV first!")

    setLoading(true)
    const formData = new FormData()
    formData.append("file", file)

    try {
      const response = await fetch("http://127.0.0.1:8000/api/roast", {
        method: "POST",
        body: formData,
      })

      const data = await response.json()
      if (response.ok) {
        setRoast(data.roast)
      } else {
        alert(data.detail)
      }
    } catch (error) {
      console.error("Fetch error:", error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif' }}>
      <h1>🎬 Project Cinehem</h1>

      <form onSubmit={handleUpload}>
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Tyler is reviewing..." : "Roast Me"}
        </button>
      </form>

      {roast && (
        <div style={{ marginTop: '20px', padding: '20px', border: '2px solid #ff4500' }}>
          <h2>The Verdict:</h2>
          <p>{roast}</p>
        </div>
      )}
    </div>
  )
}

export default App