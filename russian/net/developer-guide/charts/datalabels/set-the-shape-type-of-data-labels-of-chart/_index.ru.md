---
title: Установка формы меток данных диаграммы
description: Узнайте, как установить тип формы подписей данных на диаграмме с помощью Aspose.Cells for .NET. Наше руководство объяснит различные доступные типы форм и покажет вам, как выбрать подходящий тип формы для ваших подписей данных, чтобы улучшить представление и удобство использования ваших диаграмм
keywords: Aspose.Cells for .NET, построение диаграмм, подписи данных, типы форм, представление, удобство использования
type: docs
weight: 110
url: /ru/net/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**
Вы можете изменить тип формы подписей данных диаграммы с помощью свойства DataLabels.ShapeType. Оно принимает значение перечисления DataLabelShapeType и изменяет тип формы подписей данных соответственно. Некоторые из его значений

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Установка типа формы меток данных диаграммы**
Приведенный ниже образец кода изменяет тип формы подписей данных диаграммы на DataLabelShapeType.WedgeEllipseCallout. Пожалуйста, обратитесь к [образцу файла Excel](60489778.xlsx), использованному в этом коде, и [выходному файлу Excel](60489779.xlsx), сгенерированному им. Снимок экрана показывает эффект кода на образцовом файле Excel. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
