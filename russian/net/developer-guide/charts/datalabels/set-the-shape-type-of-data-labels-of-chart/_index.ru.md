---
title: Установите тип формы меток данных диаграммы
type: docs
weight: 110
url: /ru/net/set-the-shape-type-of-data-labels-of-chart/
---
## **Возможные сценарии использования**
Вы можете изменить тип формы меток данных диаграммы с помощью свойства DataLabels.ShapeType. Он принимает значение перечисления DataLabelShapeType и соответствующим образом изменяет тип формы меток данных. Некоторые его значения

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Установите тип формы меток данных диаграммы**
 В следующем примере кода тип формы меток данных диаграммы изменяется на DataLabelShapeType.WedgeEllipseCallout. Пожалуйста, смотрите[образец файла Excel](60489778.xlsx) используется в этом коде и[выходной файл Excel](60489779.xlsx) порожденный им. На снимке экрана показано влияние кода на пример файла Excel.

![дело:изображение_альтернативный_текст](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
