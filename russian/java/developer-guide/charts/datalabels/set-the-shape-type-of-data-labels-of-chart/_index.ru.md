---
title: Установка формы меток данных диаграммы
type: docs
weight: 70
url: /ru/java/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**

Вы можете изменить тип формы меток данных диаграммы, используя свойство [**DataLabels.ShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShapeType). Оно принимает значение перечисления [**DataLabelShapeType**](https://reference.aspose.com/cells/java/com.aspose.cells/DataLabelShapeType) и соответственно изменяет тип формы меток данных. Некоторые из его значений:

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Установка типа формы меток данных диаграммы**

Следующий образец кода изменяет тип формы меток данных диаграммы на [**DataLabelShapeType.WEDGE_ELLIPSE_CALLOUT**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabelshapetype#WEDGE-ELLIPSE-CALLOUT). Пожалуйста, посмотрите [образец файл Excel](60489794.xlsx), используемый в этом коде, и [файл Excel вывода](60489793.xlsx), сгенерированный им. На скриншоте показан эффект кода на образце файла Excel.

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-SetShapeTypeOfDataLabelsOfChart.java" >}}
{{< app/cells/assistant language="java" >}}
