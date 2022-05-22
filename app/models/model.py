from dataclasses import dataclass

import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")  # Solves some error


@dataclass
class ModelConfig:
    config_file_path: str = (
        "app/models/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    )
    frozen_model_path: str = "app/models/object_detection/frozen_inference_graph.pb"
    labels_path: str = "app/models/object_detection/coco.names"
    output_filename: str = "prediction.png"


@dataclass
class Model:
    def __init__(self, config):
        self.config = config

    def predict(self, data):

        img = cv2.imdecode(data, flags=1)

        model = cv2.dnn_DetectionModel(
            model=self.config.frozen_model_path, config=self.config.config_file_path
        )

        classLabels = []
        with open(self.config.labels_path, "rt") as fpt:
            classLabels = fpt.read().rstrip("\n").split("\n")

        model.setInputSize(320, 320)
        model.setInputScale(1.0 / 127.5)  # 255/2
        model.setInputMean((127.5, 127.5, 127.5))  # movilenet -> [-1,1]
        model.setInputSwapRB(True)

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)

        ClassIndex = ClassIndex - 1
        classLabels[ClassIndex[0]], classLabels[ClassIndex[-1]]

        for ClassInd, conf, boxes in zip(
            ClassIndex.flatten(), confidence.flatten(), bbox
        ):
            cv2.rectangle(img, boxes, (255, 0, 0), 2)
            cv2.putText(
                img=img,
                text=classLabels[ClassInd],
                org=(boxes[0] + 10, boxes[1] + 40),
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=8,
                color=(0, 0, 255),
                thickness=10,
            )

        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.xticks([])
        plt.yticks([])
        plt.savefig(
            f"app/views/static/images/predictions/{self.config.output_filename}",
            bbox_inches="tight",
        )

        return self.config.output_filename

    def real_time(self):

        thres = 0.45  # Threshold to detect object

        cap = cv2.VideoCapture(1)
        cap.set(3, 1280)
        cap.set(4, 720)
        cap.set(10, 70)

        classNames = []
        with open(self.config.labels_path, "rt") as f:
            classNames = f.read().rstrip("n").split("n")

        configPath = "ssd_mobilenet_v3_large_coco_2020_01_14/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        weightsPath = "frozen_inference_graph.pb"

        net = cv2.dnn_DetectionModel(
            model=self.config.frozen_model_path, config=self.config.config_file_path
        )
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        while cap.isOpened():
            success, img = cap.read()
            classIds, confs, bbox = net.detect(img, confThreshold=thres)
            print(classIds, bbox)

            if len(classIds) != 0:
                for classId, confidence, box in zip(
                    classIds.flatten(), confs.flatten(), bbox
                ):
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(
                        img,
                        classNames[classId - 1].upper(),
                        (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )
                    cv2.putText(
                        img,
                        str(round(confidence * 100, 2)),
                        (box[0] + 200, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

            # cv2.imshow("Output", img)
            cv2.waitKey(1)
