import cv2

# 读取图像
# img = cv2.imread('3.jpg')
# # 显示图像
# # cv2.imshow('image', img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# # 旋转图像
# rows, cols = img.shape[:2]
# M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
# rotated_img = cv2.warpAffine(img, M, (cols, rows))
# # 保存旋转后的图像
# cv2.imwrite('rotated_image.jpg', rotated_img)


# 读取视频
cap = cv2.VideoCapture('7-19 构建应用.mp4')
while (cap.isOpened()):
    # 读取视频帧
    ret, frame = cap.read()
    if ret == True:
        # 显示视频帧
        cv2.imshow('video', frame)
        # q键退出
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        # 关闭视频
            cap.release()
            cv2.destroyAllWindows()