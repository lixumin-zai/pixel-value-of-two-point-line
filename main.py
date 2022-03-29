import cv2
import numpy as np

# 图片路径
img = cv2.imread('test.tif', cv2.IMREAD_GRAYSCALE)


def LineDDA(start, end, points):
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]
    delta_x = end_x - start_x
    delta_y = end_y - start_y

    if abs(delta_x) > abs(delta_y):
        steps = abs(delta_x)
    else:
        steps = abs(delta_y)

    x_step = delta_x / steps
    y_step = delta_y / steps

    x = start_x
    y = start_y
    while steps >= 0:
        points.append([round(x), round(y)])
        x += x_step
        y += y_step
        steps -= 1


def func1():
    start = input("输入a的坐标（空格隔开x, y）：")
    end = input("输入b的坐标（空格隔开x, y）：")
    try:
        start = start.split(" ")
        end = end.split(" ")
        start = [int(start[0]), int(start[1])]
        end = [int(end[0]), int(end[1])]
        points = []
        LineDDA(start, end, points)
        with open("func1.txt", "w", encoding="utf-8") as func1_txt:
            func1_txt.write('x      \t y      \t data\n')
            for point in points:
                func1_txt.write(str(point[0]) + "    \t " + str(point[1]) + "    \t\t " + f"{img[point[1], point[0]]}" + "\n")
        cv2.line(img, (start[0], start[1]), (end[0], end[1]), (255, 255, 255), 2, 4)
        cv2.imshow("sdf", img)
        cv2.waitKey(0)
    except:
        print("输入出错，重新启动程序")

n = 0  # 定义鼠标按下的次数
def func2():
    a = []
    b = []

    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        global n
        if event == cv2.EVENT_LBUTTONDOWN:
            if n == 0:  # 首次按下保存坐标值
                n += 1
                a.append(x)
                b.append(y)
                # cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
                cv2.putText(img, "a", (x, y), cv2.FONT_HERSHEY_PLAIN,
                            1.0, (0, 0, 0), thickness=1)
                cv2.imshow("image", img)
            elif n == 1:  # 第二次按下显示矩形
                n += 1
                a.append(x)
                b.append(y)
                cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
                cv2.putText(img, "b", (x, y), cv2.FONT_HERSHEY_PLAIN,
                            1.0, (0, 0, 0), thickness=1)
                points = []
                LineDDA([a[0],b[0]], [a[1],b[1]], points)
                with open("func2.txt", "w", encoding="utf-8") as func1_txt:
                    func1_txt.write('x      \t y      \t data\n')
                    for point in points:
                        func1_txt.write(
                            str(point[0]) + "    \t " + str(point[1]) + "    \t\t " + f"{img[point[1], point[0]]}" + "\n")
                cv2.line(img, (a[0], b[0]), (a[1], b[1]), (255, 255, 255), 2, 4)
                cv2.imshow("image", img)
            else:
                cv2.destroyWindow("image")
        else:
            pass
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)

if __name__ == "__main__":
    func1()
    # func2()
