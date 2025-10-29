---
title: Установка формы меток данных диаграммы
description: Узнайте, как установить тип формы метки данных в диаграммах с помощью Aspose.Cells для Python via .NET. Наш гид объяснит разные доступные типы форм и покажет, как выбрать подходящую форму для ваших меток данных, чтобы повысить презентацию и удобство использования диаграмм.
keywords: Aspose.Cells для Python via .NET, создание диаграмм, метки данных, типы форм, презентация, удобство использования.
type: docs
weight: 110
url: /ru/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **Возможные сценарии использования**
Вы можете изменить тип формы подписей данных диаграммы с помощью свойства DataLabels.ShapeType. Оно принимает значение перечисления DataLabelShapeType и изменяет тип формы подписей данных соответственно. Некоторые из его значений

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Установка типа формы меток данных диаграммы**
Приведенный ниже образец кода изменяет тип формы подписей данных диаграммы на DataLabelShapeType.WedgeEllipseCallout. Пожалуйста, обратитесь к [образцу файла Excel](60489778.xlsx), использованному в этом коде, и [выходному файлу Excel](60489779.xlsx), сгенерированному им. Снимок экрана показывает эффект кода на образцовом файле Excel. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Образец кода**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
{{< app/cells/assistant language="python-net" >}}
