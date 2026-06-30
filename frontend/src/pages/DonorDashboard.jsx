import Layout from "../components/Layout";
import FoodCard from "../components/FoodCard";

function DonorDashboard() {
  return (
    <Layout>

      <div className="container">

        <h1>Welcome back 👋</h1>

        <h2>My Donations</h2>

        <FoodCard
          foodName="Vegetable Biryani"
          quantity="25 Meals"
          category="Cooked Food"
          status="Available"
        />

      </div>

    </Layout>
  );
}

export default DonorDashboard;