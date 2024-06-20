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

Ardından veri kaynağını veri ile doldurur ve [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) yöntemini çağırarak akıllı işaretçi etiketlerini işlemek için kullanır. Kod, bu görüntüleri kullanır: [moon.png](5472549.png) ve [moon2.png](5472548.png) ancak istediğiniz herhangi bir görüntüyü kullanabilirsiniz. Aşağıdaki ekran görüntüsü, bu örnek kodun çıktısını gösterir. Görebileceğiniz gibi, sütun E ve F'deki veriler sütun D'deki verilere göre gruplandırılmıştır.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
