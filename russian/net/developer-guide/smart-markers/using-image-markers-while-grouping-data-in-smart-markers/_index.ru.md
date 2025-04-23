---
title: Использование маркеров изображений при группировке данных в умных маркерах
type: docs
weight: 30
url: /ru/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Использование маркеров изображений при группировке данных в умных маркерах**
В следующем образце создается книга и затем добавляются следующие умные маркерные теги в ячейках D2, E2 и F2 соответственно.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Затем заполняются исходные данные и вызывается метод [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) для обработки умных маркерных тегов. Код использует следующие изображения, т.е. [moon.png](5115492.png) и [moon2.png](5115491.png), но вы можете использовать любое изображение.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
{{< app/cells/assistant language="csharp" >}}
