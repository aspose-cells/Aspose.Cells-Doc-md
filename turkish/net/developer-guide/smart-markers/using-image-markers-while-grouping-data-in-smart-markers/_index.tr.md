---
title: Akıllı İşaretçi Alanında Verileri Gruplandırırken Resim İşaretçileri Kullanma
type: docs
weight: 30
url: /tr/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Akıllı İşaretçi Alanında Verileri Gruplandırırken Resim İşaretçileri Kullanma**
Aşağıdaki örnek bir çalışma kitabı oluşturur ve ardından sırasıyla D2, E2 ve F2 hücrelerine akıllı işaretçi etiketlerini ekler.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Daha sonra veri kaynağını veri ile doldurur ve [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) yöntemini çağırarak akıllı işaretçi etiketlerini işler. Kod, şu resimleri [moon.png](5115492.png) ve [moon2.png](5115491.png) kullanır ancak istediğiniz resmi kullanabilirsiniz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
