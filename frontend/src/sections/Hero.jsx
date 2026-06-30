import { FaLeaf } from "react-icons/fa";
import Button from "../components/Button";

function Hero() {
  return (
    <section className="hero-section">
      <div className="container hero-container">

        <div className="hero-left">

          <div className="hero-tag">
            <FaLeaf />
            <span> Smart Food Redistribution Platform</span>
          </div>

          <h1>
            Reduce Food Waste.
            <br />
            Feed More Lives.
          </h1>

          <p>
            FoodSaver connects restaurants, hostels,
            caterers, NGOs and volunteers
            to redistribute surplus food safely,
            efficiently and responsibly.
          </p>

          <div className="hero-buttons">
            <Button text="Donate Food" />
            <Button
              text="Find Food"
              type="secondary"
            />
          </div>

        </div>

        <div className="hero-right">

          <div className="hero-image">

            🍱

          </div>

        </div>

      </div>
    </section>
  );
}

export default Hero;