import pandas as pd

class BudgetModel:
    def __init__(self, budget_data):
        self.budget_data = budget_data

    def calculate_variance(self):
        self.budget_data['Variance'] = self.budget_data['Actual'] - self.budget_data['Budgeted']
        return self.budget_data

    def summarize_budget(self):
        summary = self.budget_data[['Category', 'Budgeted', 'Actual', 'Variance']].groupby('Category').sum()
        return summary

if __name__ == "__main__":
    # Sample budget data
    data = {
        'Category': ['Marketing', 'Sales', 'R&D', 'Operations'],
        'Budgeted': [50000, 100000, 75000, 60000],
        'Actual': [55000, 95000, 80000, 65000]
    }
    budget_df = pd.DataFrame(data)
    model = BudgetModel(budget_df)
    variance_df = model.calculate_variance()
    print("Budget Variance:\n", variance_df)
    print("\nBudget Summary:\n", model.summarize_budget())