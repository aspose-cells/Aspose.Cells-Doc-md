---
title: Akıllı İşaretleyicilerde Verileri Gruplandırırken Görüntü İşaretleyicileri Kullanma
type: docs
weight: 30
url: /tr/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Akıllı İşaretleyicilerde Verileri Gruplandırırken Görüntü İşaretleyicileri Kullanma**
Aşağıdaki örnek bir çalışma kitabı oluşturur ve ardından sırasıyla D2, E2 ve F2 hücrelerine aşağıdaki akıllı işaretçi etiketlerini ekler.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Ardından veri kaynağını verilerle doldurur ve[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) akıllı işaretleyici etiketlerini işleme yöntemi. Kod, bu görüntüleri kullanır, yani[ay.png](5115492.png) ve[ay2.png](5115491.png) ancak herhangi bir resmi kullanabilirsiniz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
