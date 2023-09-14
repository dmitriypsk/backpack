from typing import List, Tuple

class MultidimensionalKnapsack:
    def __init__(self, weights: List[int], volumes: List[int], values: List[int]) -> None:
        if not (len(weights) == len(volumes) == len(values)):
            raise ValueError("Списки весов, объемов и значений должны иметь одинаковую длину.")
        
        self.weights = weights
        self.volumes = volumes
        self.values = values
        self.n = len(weights)
        self.dp = {}
        self.last_calculated_limits = None

    def _calculate(self, weight_limit: int, volume_limit: int) -> None:
        if self.last_calculated_limits == (weight_limit, volume_limit):
            return

        dp = [[[0 for _ in range(volume_limit + 1)] for _ in range(weight_limit + 1)] for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            for w in range(weight_limit + 1):
                for v in range(volume_limit + 1):
                    dp[i][w][v] = dp[i-1][w][v]
                    if self.weights[i-1] <= w and self.volumes[i-1] <= v:
                        dp[i][w][v] = max(self.values[i-1] + dp[i-1][w-self.weights[i-1]][v-self.volumes[i-1]], dp[i-1][w][v])

        self.dp = dp
        self.last_calculated_limits = (weight_limit, volume_limit)

    def max_value(self, weight_limit: int, volume_limit: int) -> int:
        self._calculate(weight_limit, volume_limit)
        return self.dp[self.n][weight_limit][volume_limit]

# Тестирование
def test_knapsack():
    weights = [10, 20, 30]
    volumes = [5, 10, 15]
    values = [60, 100, 120]
    weight_limit = 50
    volume_limit = 20
    knapsack = MultidimensionalKnapsack(weights, volumes, values)
    
    result = knapsack.max_value(weight_limit, volume_limit)
    print(f"Ожидаемый результат: 180, Фактический результат: {result}")
    assert result == 180
    
    print("Тесты прошли успешно!")


test_knapsack()
