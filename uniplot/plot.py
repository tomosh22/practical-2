import matplotlib.pyplot as plt


def plot_bar_show(d):
    """plots a graph of frequency against taxa for every protein"""
    print(d)
    # A list of numbers as long as the elements in d
    r = range(0, len(d))
    # Prepare a figure
    plt.figure()

    # Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    # Add labels to the x-axis, with the keys of d
    plt.xticks(r, d.keys())
    # Squash everything up so there is no white space
    plt.tight_layout()
    # Show the graph
    plt.show()
def plot_pie_show(d):
    print(d.values())
    fig1, ax1 = plt.subplots()
    ax1.pie(d.values(), labels=d.keys(),autopct='%1.1f%%')
    plt.show()