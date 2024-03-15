import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        super().__init__(self.fig)
        self.historical_spending = pd.read_csv('data/historical_spending.csv')
        self.gifts_gender = pd.read_csv('data/gifts_gender.csv')
        self.gifts_age = pd.read_csv('data/gifts_age.csv')
        
    def plot_historical_spending(self):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        palette = plt.get_cmap('Set1')

        # Plot each column
        num = 0
        for column in self.historical_spending.drop(['Year', 'PercentCelebrating'], axis=1):
            num += 1
            ax.plot(self.historical_spending['Year'], self.historical_spending[column], marker='', color=palette(num), linewidth=2.5, alpha=0.9, label=column)

        # Add legend and titles using the axis object
        ax.legend(loc=2, ncol=2)
        ax.set_title("Historical Spending Trends on Valentine's Day (2010-2019)", loc='left', fontsize=12, fontweight=0, color='orange')
        ax.set_xlabel("Year")
        ax.set_ylabel("Spending ($)")
        ax.set_xticks(self.historical_spending['Year'])

        # Refresh canvas
        self.draw()
        
    def plot_gender_spending(self):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        barWidth = 0.3
        
        if 'SpendingCelebrating' in self.gifts_gender.columns:
            self.gifts_gender = self.gifts_gender.drop('SpendingCelebrating', axis=1)

        r1 = range(len(self.gifts_gender.columns[1:]))
        r2 = [x + barWidth for x in r1]

        ax.bar(r1, self.gifts_gender.iloc[0, 1:], color='#7f6d5f', width=barWidth, edgecolor='grey', label='Men')
        ax.bar(r2, self.gifts_gender.iloc[1, 1:], color='#557f2d', width=barWidth, edgecolor='grey', label='Women')

        ax.set_xlabel('Gift Categories', fontweight='bold')
        ax.set_xticks([r + barWidth for r in range(len(self.gifts_gender.columns[1:]))], self.gifts_gender.columns[1:], rotation=45)
        ax.set_ylabel('Percentage of Spending (%)')
        ax.set_title('Gift Preferences by Genders on Valentine\'s Day')
        ax.legend()

        # Refresh canvas
        self.draw()

    def plot_age_spending(self):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        barWidth = 0.85
        
        if 'SpendingCelebrating' in self.gifts_age.columns:
            self.gifts_age = self.gifts_age.drop('SpendingCelebrating', axis=1)

        r = range(len(self.gifts_age))

        for i, col in enumerate(self.gifts_age.columns[1:]):
            ax.bar(r, self.gifts_age[col], bottom=self.gifts_age[self.gifts_age.columns[1:i+1]].sum(axis=1), 
                   edgecolor='white', width=barWidth, label=col)

        ax.set_xlabel('Age Group', fontweight='bold')
        ax.set_xticks(r, self.gifts_age['Age'])
        ax.set_ylabel('Percentage of Spending (%)')
        ax.set_title('Preferences for Valentine\'s Day Gifts based on Age Groups')
        ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

        # Refresh canvas
        self.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Canvas setup
        self.canvas = MplCanvas()

        # Buttons
        self.btn_historical = QPushButton('Historical Spending Patterns')
        self.btn_historical.clicked.connect(self.canvas.plot_historical_spending)

        self.btn_gender = QPushButton('Spending Patterns by Gender')
        self.btn_gender.clicked.connect(self.canvas.plot_gender_spending)

        self.btn_age = QPushButton('Spending Patterns by Age')
        self.btn_age.clicked.connect(self.canvas.plot_age_spending)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.btn_historical)
        layout.addWidget(self.btn_gender)
        layout.addWidget(self.btn_age)
        layout.addWidget(self.canvas)

        # Central Widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Window title
        self.setWindowTitle('Valentine\'s Day Spending Analysis')

# Start Qt event loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
