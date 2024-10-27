import random
import time

def LOTTO(count):
    for i in range(count):
        draw_sets = [[x for x in range(1, 46)] for _ in range(5)]
        test_set = [x for x in range(1,46)]
        spare_sets = [[x for x in range(1, 46)] for _ in range(2)]

        draw_set_num = random.randint(0,4)
        spare_set_num = random.randint(0,1)

        result = []

        random.shuffle(draw_sets[draw_set_num])

        for _ in range(6):
            start_time = time.time_ns()
            wait_time = random.uniform(4, 5) * 1e9
            while time.time_ns()- start_time < wait_time:
                random.shuffle(draw_sets[draw_set_num])
            choosed_ball = draw_sets[draw_set_num].pop(len(draw_sets[draw_set_num])//2)
            print(choosed_ball)
            result.append(choosed_ball)

        print(sorted(result))



LOTTO(1)