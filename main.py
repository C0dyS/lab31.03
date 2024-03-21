class MathClass:
    @staticmethod
    def max(*args):
        if not args:
            return None
        largest_number_founder = args[0]
        for _ in args:
            if _ > largest_number_founder:
                largest_number_founder = _
        return largest_number_founder
    @staticmethod
    def min(*args):
        if not args:
            return None
        smallest_number_founder = args[0]
        for _ in args:
            if _ < smallest_number_founder:
                smallest_number_founder = _
        return smallest_number_founder
    @staticmethod
    def factorial(a):
        result = 1
        if a < 0:
            raise ValueError("negative number")
        elif a == 1:
            return 1
        else:
            for i in range(1,a+1):
                result *= i
            return result

    @staticmethod
    def arithmetic_mean(*args):
        if not args:
            return None
        summ = 0
        for _ in args:
            summ += _
        return summ/len(args)



