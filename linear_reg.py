import matrix


class LinearRegression:

    def __init__(self, X, y, Theta, alpha):
        self.X = matrix.offset_x(X)  # (M x(n+1))
        self.y = y  # (1 x M)
        self.Theta = Theta  # (1 x (n+1))
        self.alpha = alpha
        self.M = len(X)  # M -> Number of training examples
        self.h = self.hypothesis_function()  # (1 x M)
        self.trained = False

    def hypothesis_function(self):
        """Returns the hypothesis function with a dimension of (1 x M)"""
        return matrix.dot(self.Theta, matrix.transpose(self.X))

    def error_function_der(self):
        """Returns the derivative of the error function with a dimension of (1 x (n+1))"""
        ser = matrix.dot(matrix.diff(self.h, self.y), self.X)
        J = matrix.dot_scalar(ser, 1/self.M)
        return J

    def gradient_descent(self, iterations):
        """Returns the result of gradient descent -> Theta with a dimension of (1 x (n+1))"""
        for i in range(iterations):
            J_theta = self.error_function_der()
            self.Theta = matrix.diff(self.Theta, matrix.dot_scalar(J_theta, self.alpha))

        self.trained = True
        return self.Theta

    def test_model(self):
        if not self.trained:
            print("You have not trained your model")

        y = matrix.dot(self.Theta, matrix.transpose(self.X))
        return y

theta = [[0.25, 0.5]]
ml = LinearRegression([[1], [2], [3], [4], [5]], [[2, 4, 6, 8, 10]], theta, 0.2)
print(ml.gradient_descent(10))
print("y = ", ml.y, "\n", "y_test = ", ml.test_model())
