---
title: Использование маркеров изображений при группировке данных в смарт-маркерах
type: docs
weight: 30
url: /ru/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Использование маркеров изображений при группировке данных в смарт-маркерах**
В следующем примере создается рабочая книга, а затем добавляются следующие теги смарт-маркеров в ячейки D2, E2 и F2 соответственно.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Затем он заполняет источник данных данными и вызывает[WorkbookDesigner.Процесс()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) способ обработки тегов смарт-маркеров. Код использует эти изображения, т.е.[луна.png](5115492.png) а также[луна2.png](5115491.png) но вы можете использовать любое изображение.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
