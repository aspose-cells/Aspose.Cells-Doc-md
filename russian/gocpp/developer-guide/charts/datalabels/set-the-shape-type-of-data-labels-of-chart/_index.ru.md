---
title: Установить тип фигуры меток данных графика с помощью Golang через C++
linktitle: Установка формы меток данных диаграммы
description: Узнайте, как задавать тип фигуры меток данных в графиках с помощью Aspose.Cells for C++. Наше руководство объяснит доступные типы фигур и покажет, как выбрать подходящую фигуру для ваших меток данных, чтобы улучшить презентацию и удобство использования ваших графиков.
keywords: Aspose.Cells for C++, построение графиков, метки данных, типы фигур, презентация, удобство.
type: docs
weight: 110
url: /ru/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**
Вы можете изменить тип фигуры меток данных на графике, используя свойство `DataLabels.ShapeType`. Оно принимает значение перечисления `DataLabelShapeType` и соответственно изменяет тип фигуры меток данных. Некоторые из его значений:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Установка типа формы меток данных диаграммы**
Следующий пример кода изменяет тип формы меток данных диаграммы на `DataLabelShapeType.WedgeEllipseCallout`. Обратите внимание на [пример файла Excel](60489778.xlsx), используемый в этом коде, и на [сгенерированный файл Excel](60489779.xlsx). Скриншот показывает эффект от кода на примере файла Excel. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Образец кода**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
