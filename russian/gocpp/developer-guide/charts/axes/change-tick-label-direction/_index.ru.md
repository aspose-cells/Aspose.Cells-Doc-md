---
title: Изменить направление подписи шкалы с помощью Golang через C++
linktitle: Изменение направления меток делений
description: Узнайте, как изменить направление меток шкалы в Aspose.Cells for C++. Наше руководство поможет вам понять, как регулировать ориентацию меток на осях, включая горизонтальную, вертикальную и наклонную.
keywords: Aspose.Cells for C++, метки шкалы, направление, ориентация, оси, горизонтально, вертикально, наклонно.
type: docs
weight: 170
url: /ru/go-cpp/change-tick-label-direction/
---

## **Изменение направления меток делений**

Aspose.Cells позволяет изменять направление меток осей, используя свойство [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/). Свойство [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/go-cpp/ticklabels/getdirectiontype/) принимает значение перечисления [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). Перечисление [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) включает следующие члены:

- Горизонтальное
- Вертикальное
- Повернуть90
- Повернуть270
- Стековое

Следующее изображение сравнивает исходный файл и результат:

### **Изображение исходного файла**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Изображение выходного файла**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Следующий фрагмент кода изменяет направление меток делений с Повернуть90 на Горизонтальное.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeTickLabelDirection.go" >}}
Исходные и выходные файлы можно загрузить по следующим ссылкам.

[Исходный файл](105480221.xlsx)

[Выходной файл](105480223.xlsx)
