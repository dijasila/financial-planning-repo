import matplotlib.pyplot as plt

def plot_budget_variance(budget_df):
    categories = budget_df['Category']
    budgeted = budget_df['Budgeted']
    actual = budget_df['Actual']
    variance = budget_df['Variance']

    x = range(len(categories))
    
    plt.bar(x, budgeted, width=0.4, label='Budgeted', color='blue', align='center')
    plt.bar(x, actual, width=0.4, label='Actual', color='orange', align='edge')
    plt.xticks(x, categories)
    plt.xlabel('Budget Categories')
    plt.ylabel('Amount ($)')
    plt.title('Budget vs Actual')
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../docs/budget_variance_visualization.png')
    plt.show()

if __name__ == "__main__":
    from budget_model import BudgetModel
    data = {
        'Category': ['Marketing', 'Sales', 'R&D', 'Operations'],
        'Budgeted': [50000, 100000, 75000, 60000],
        'Actual': [55000, 95000, 80000, 65000]
    }
    budget_df = pd.DataFrame(data)
    model = BudgetModel(budget_df)
    variance_df = model.calculate_variance()
    plot_budget_variance(variance_df)