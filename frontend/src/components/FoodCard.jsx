function FoodCard({
  foodName,
  quantity,
  category,
  status
}) {
  return (
    <div className="food-card">

      <h3>{foodName}</h3>

      <p>
        <strong>Quantity:</strong> {quantity}
      </p>

      <p>
        <strong>Category:</strong> {category}
      </p>

      <span className="food-status">
        {status}
      </span>

      <div className="food-actions">
        <button className="edit-btn">
          Edit
        </button>

        <button className="delete-btn">
          Delete
        </button>
      </div>

    </div>
  );
}

export default FoodCard;