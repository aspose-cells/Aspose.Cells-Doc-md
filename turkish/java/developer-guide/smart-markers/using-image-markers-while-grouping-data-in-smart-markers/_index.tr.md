---
title: Akıllı İşaretleyicilerde Verileri Gruplandırırken Görüntü İşaretleyicileri Kullanma
type: docs
weight: 630
url: /tr/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Bu makale, verileri akıllı işaretleyicilerde gruplandırırken görüntü işaretçilerinin kullanımını gösteren bir örnek sunmaktadır.

{{% /alert %}} 
## **Akıllı İşaretleyicilerde Verileri Gruplandırırken Görüntü İşaretleyicileri Kullanma**
Aşağıdaki örnek kod bir çalışma kitabı oluşturur ve ardından sırasıyla D2, E2 ve F2 hücrelerine aşağıdaki akıllı işaretçi etiketlerini ekler.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Ardından veri kaynağını verilerle doldurur ve[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) akıllı işaretleyici etiketlerini işleme yöntemi. Kod, bu görüntüleri kullanır, yani[ay.png](5472549.png) ve[ay2.png](5472548.png) ancak herhangi bir resmi kullanabilirsiniz. Aşağıdaki ekran görüntüsü bu örnek kodun çıktısını göstermektedir. Gördüğünüz gibi, E ve F sütunundaki veriler, D sütunundaki verilere göre gruplandırılmıştır.

![yapılacaklar:resim_alternatif_Metin](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
