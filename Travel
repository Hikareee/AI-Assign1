# Define the graph as a dictionary
graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'F': 9, 'E': 7},
}

# Define the function to calculate the total distance of a given route
def calcRouteDistance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]
    return distance

# Define the genetic algorithm loop
import random

def geneticAlgorithmLoop(graph, populationSize, eliteSize, mutationRate, generations):
    # Create the initial population
    population = []
    for i in range(populationSize):
        route = list(graph.keys())
        random.shuffle(route)
        population.append(route)

    # Loop through the generations
    for i in range(generations):
        # Calculate the fitness score of each route
        fitnessScores = {}
        for route in population:
            fitnessScores[tuple(route)] = 1 / calcRouteDistance(route, graph)
        sortedFitnessScores = sorted(fitnessScores.items(), key=lambda x: x[1], reverse=True)
        selectedRoutes = [list(route[0]) for route in sortedFitnessScores[:eliteSize]]

        # Generate the next generation of routes
        newPopulation = selectedRoutes.copy()
        while len(newPopulation) < populationSize:
            parent1, parent2 = random.sample(selectedRoutes, 2)
            child = [None] * len(graph)
            start, end = sorted(random.sample(range(len(graph)), 2))
            child[start:end + 1] = parent1[start:end + 1]
            for i in range(len(parent2)):
                if parent2[i] not in child:
                    for j in range(len(child)):
                        if child[j] is None:
                            child[j] = parent2[i]
                            break
            newPopulation.append(child)

        # Apply mutation to create a new generation of routes
        for i in range(len(newPopulation)):
            if random.random() < mutationRate:
                start, end = sorted(random.sample(range(len(graph)), 2))
                newPopulation[i][start:end + 1] = reversed(newPopulation[i][start:end + 1])

        # Update the population
        population = newPopulation

    # Find the best route and its total distance
    bestRoute = sortedFitnessScores[0][0]
    bestDistance = calcRouteDistance(bestRoute, graph)

    # Print the best route and its total distance
    print("Best Route:", bestRoute)
    print("Total Distance:", bestDistance)

geneticAlgorithmLoop(graph, populationSize=100, eliteSize=20, mutationRate=0.01, generations=500)
