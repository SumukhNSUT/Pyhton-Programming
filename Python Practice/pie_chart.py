import matplotlib.pyplot as plt
province_population = [12344408, 2441523, 30523371, 110012442, 47886051]
activities = ['NDLS', 'DLI', 'ANVT', 'Punjab', 'Sindh']
plt.pie(province_population, labels=activities,
        startangle=90, autopct='%.1f%%')
plt.title('Population Province Wise')
plt.show()
