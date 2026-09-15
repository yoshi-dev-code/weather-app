import { useState } from "react";
import "./App.css";

function App() {
    const API_URL = import.meta.env.VITE_API_URL;

    const [temperature, setTemperature] = useState(null);
    const [city, setCity] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const searchWeather = () => {
        if (city.trim() === "") {
            setError("都市名を入力してください");
            setTemperature(null);
            return;
        }

        setLoading(true);

        fetch(`${API_URL}/weather?city=${city}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    setError(data.error);
                    setTemperature(null);
                } else {
                    setTemperature(data.temperature);
                    setError("");
                }
            })
            .catch(() => {
                setError("天気情報の取得に失敗しました");
                setTemperature(null);
            })
            .finally(() => {
                setLoading(false);
            });
    };

    return (
        <div className="weather-page">
            <div className="weather-card">
                <h1>天気アプリ</h1>

                <div className="search-box">
                    <input
                        type="text"
                        value={city}
                        onChange={(e) => setCity(e.target.value)}
                        placeholder="都市名を入力"
                    />

                    <button onClick={searchWeather} disabled={loading}>
                        {loading ? "検索中..." : "検索"}
                    </button>
                </div>
                
                {error && <p className="error-message">{error}</p>}

                {temperature !== null && (
                    <p className="temperature">
                        現在の気温: {temperature}℃
                    </p>
                )}    
            </div>    
        </div>
    );
}

export default App;