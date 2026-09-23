"""
Problem: Best Time to Buy and Sell Stock

Description:
Given an array prices where prices[i] represents the price of a stock on day i, determine the maximum profit you can achieve by buying on one day and selling on a later day.

A valid transaction must follow these rules:

You must buy before you sell.
You can only make one transaction.
If no profit can be made, return 0.

Example:
Input:  [7, 1, 5, 3, 6, 4]
Output: 5

Complexity:
Time: O(n)
Space: O(1)
"""

def best_time_to_buy(precios):

    ganancia_posible = 0
    mayor_ganancia = 0
    menor_precio = precios[0]

    for precio_actual in precios:

        if precio_actual < menor_precio:
            menor_precio = precio_actual

        ganancia_posible = precio_actual - menor_precio
        
        if ganancia_posible > mayor_ganancia:
            mayor_ganancia = ganancia_posible

    if mayor_ganancia < 1:
        return 0
    return mayor_ganancia

print(best_time_to_buy([7, 1, 5, 3, 6, 4]))