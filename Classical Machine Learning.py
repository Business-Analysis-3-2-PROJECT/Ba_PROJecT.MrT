 =====================================================================
# PART A: CLASSICAL ML (RANDOM FOREST REGRESSOR)
# =====================================================================

rf_regressor = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=5, random_state=42, max_depth=10, min_samples_split=5))
])

print("\n--- Training Random Forest Model ---")
rf_regressor.fit(X_train, Y_train) 
print("Training Complete.")

Y_rf_pred = rf_regressor.predict(X_test)
rf_r2 = r2_score(Y_test, Y_rf_pred)

print("\n--- Random Forest Performance (R2 will reflect sampled data) ---")
print(f"R-squared Score (R2): {rf_r2:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(Y_test, Y_rf_pred, alpha=0.6, color='blue', label='Predicted Price')
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', lw=2, label='Ideal Prediction (Y=X)')
plt.title(f"Random Forest Actual vs. Predicted Prices (R2: {rf_r2:.4f})")
plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.legend()
plt.grid(True)
plt.show()
