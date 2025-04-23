---
title: Akıllı İşaretçi Alanında Verileri Gruplandırırken Resim İşaretçileri Kullanma
type: docs
weight: 630
url: /tr/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Bu makale, akıllı işaretçilerde veri gruplama sırasında görüntü imlerinin kullanımını açıklayan bir örnek sunar.

{{% /alert %}} 
## **Akıllı İşaretçi Alanında Verileri Gruplandırırken Resim İşaretçileri Kullanma**
Aşağıdaki örnek kod bir çalışma kitabı oluşturur ve ardından sırasıyla D2, E2 ve F2 hücrelerine aşağıdaki akıllı işaretçi etiketlerini ekler.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Daha sonra veri kaynağı veri ile doldurulur ve akıllı işaretçi etiketlerini işlemek için [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) yöntemi çağrılır. Kod, bu resimleri kullanır; örneğin [moon.png](5472549.png) ve [moon2.png](5472548.png), ancak herhangi bir resim kullanabilirsiniz. Aşağıdaki ekran görüntüsü bu örnek kodun çıktısını göstermektedir. Görüldüğü gibi, E ve F sütunlarındaki veriler, D sütunundaki verilere göre gruplanmıştır.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
