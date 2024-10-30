class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class  # від 1 до 7
        self.clean_mark = clean_mark  # від 1 до 10
        self.brand = brand  # назва бренду


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int
    ):
        self.distance_from_city_center = distance_from_city_center  # 1.0 - 10.0
        self.clean_power = clean_power  # максимальний рівень чистоти, до якого миємо
        self.average_rating = average_rating  # рейтинг від 1.0 до 5.0
        self.count_of_ratings = count_of_ratings  # кількість оцінок

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class *
            (self.clean_power - car.clean_mark) *
            self.average_rating /
            self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def serve_cars(self, cars: list[Car]) -> float:
        total_income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_income, 1)

    def rate_service(self, new_rate: int):
        total_rating_sum = self.average_rating * self.count_of_ratings
        total_rating_sum += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_rating_sum / self.count_of_ratings, 1)
