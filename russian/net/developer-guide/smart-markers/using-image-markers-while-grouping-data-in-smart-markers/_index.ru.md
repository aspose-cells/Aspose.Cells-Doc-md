---
title: Как использовать маркеры изображений в Smart Markers
type: docs
weight: 30
url: /ru/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **Возможные сценарии использования**
Маркеры изображений — это специализированные заполняющие шаблоны в системах шаблонов (таких как FoxPro, Handlebars или современные UI-фреймворки), которые динамически внедряют изображения или визуальные ресурсы в шаблоны. Иногда необходимо вставлять изображения с помощью smart markers. Aspose.Cells позволяет добавлять изображения к smart markers.

## **Параметры изображений в Smart Markers**
Умные маркеры для управления изображениями.

- **Изображение:FitToCell** - Автоматически подгонять изображение под высоту строки и ширину столбца.
- **Изображение:МасштабN** - Масштабировать высоту и ширину до N процентов.
- **Picture:Width:Nin&Height:Nin** - Вывести изображение высотой N дюймов и шириной N дюймов. Также можно указать позиции слева и сверху (в пунктах).

## **Как использовать маркеры изображений в Smart Markers**
Пожалуйста, посмотрите следующий пример кода, который показывает, как вставлять изображения с помощью Smart Markers.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **Как использовать маркеры изображений при группировке данных в Smart Markers**
В следующем образце создается книга и затем добавляются следующие умные маркерные теги в ячейках D2, E2 и F2 соответственно.

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Затем заполняются исходные данные и вызывается метод [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) для обработки умных маркерных тегов. Код использует следующие изображения, т.е. [moon.png](5115492.png) и [moon2.png](5115491.png), но вы можете использовать любое изображение.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
