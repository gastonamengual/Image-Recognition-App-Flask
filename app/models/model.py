from dataclasses import dataclass

import cv2
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")  # Solves some error


@dataclass
class Model:
    def predict(self, data):

        img = cv2.imdecode(data, flags=1)

        config_file = (
            "app/models/object_detection/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        )
        frozen_model = "app/models/object_detection/frozen_inference_graph.pb"

        model = cv2.dnn_DetectionModel(model=frozen_model, config=config_file)

        classLabels = []
        file_name = "app/models/object_detection/coco.names"
        with open(file_name, "rt") as fpt:
            classLabels = fpt.read().rstrip("\n").split("\n")

        model.setInputSize(320, 320)
        model.setInputScale(1.0 / 127.5)  # 255/2
        model.setInputMean((127.5, 127.5, 127.5))  # movilenet -> [-1,1]
        model.setInputSwapRB(True)

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)

        ClassIndex = ClassIndex - 1
        classLabels[ClassIndex[0]], classLabels[ClassIndex[-1]]

        font_scale = 3
        font = cv2.FONT_HERSHEY_PLAIN
        for ClassInd, conf, boxes in zip(
            ClassIndex.flatten(), confidence.flatten(), bbox
        ):
            cv2.rectangle(img, boxes, (255, 0, 0), 2)
            cv2.putText(
                img,
                classLabels[ClassInd],
                (boxes[0] + 10, boxes[1] + 40),
                font,
                fontScale=font_scale,
                color=(0, 255, 0),
                thickness=3,
            )

        output_filename = "prediction.png"
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.savefig(
            f"app/views/static/images/predictions/{output_filename}",
            bbox_inches="tight",
        )

        return output_filename
