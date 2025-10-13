# =====================================================================
# PART D: CHATBOT / SOFTBOT FEATURE (Interactive Agent)
# =====================================================================

def launch_valuation_softbot(model, X_train_cols):
    """
    Simulates an interactive command-line softbot (Instant Valuation Agent).
    """
    print("\n\n=======================================================")
    print(">>> INSTANT VEHICLE VALUATION AGENT (Softbot) <<<")
    print("=======================================================")

    user_inputs = {}

    print("Note: Provide values to match the feature columns: make, model, body, year, odometer, condition, mmr.")
    user_inputs['make'] = input("Enter Vehicle Make (e.g., Toyota): ").strip()
    user_inputs['model'] = input("Enter Vehicle Model (e.g., Corolla): ").strip()
    user_inputs['body'] = input("Enter Body Type (e.g., Sedan, SUV): ").strip()

    try:
        user_inputs['year'] = int(input("Enter Year (e.g., 2019): ").strip())
        user_inputs['odometer'] = int(input("Enter Odometer Reading (e.g., 25000): ").strip())
        user_inputs['condition'] = float(input("Enter Condition Rating (1.0 - 5.0): ").strip())
        user_inputs['mmr'] = float(input("Enter Current MMR Value (Market Price Index): ").strip())
    except ValueError:
        print("Invalid input for a numerical field. Agent shutting down.")
        return

    try:
        new_data_point = pd.DataFrame([user_inputs])
        new_data_point = new_data_point.reindex(columns=X_train_cols, fill_value=np.nan)

        # Call the trained ML model
        predicted_price = model.predict(new_data_point)

        print("\n--- Agent Response ---")
        print(
            f"Predicted Optimal Selling Price for the {user_inputs['year']} {user_inputs['make']} {user_inputs['model']}:")
        print(f"💰  ${predicted_price[0]:,.2f}")

    except Exception as e:
        print(f"\nAgent encountered a prediction error: {e}")


# Call the Softbot function using the trained Random Forest model
launch_valuation_softbot(rf_regressor, X_train.columns)