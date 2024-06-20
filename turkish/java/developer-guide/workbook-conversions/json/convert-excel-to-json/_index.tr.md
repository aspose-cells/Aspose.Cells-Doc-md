---
title: Excel i JSON a Dönüştür
type: docs
weight: 20
url: /tr/java/convert-excel-to-json/
description: Aspose.Cells for Java API lerini kullanarak Excel dosyasını JSON a nasıl dönüştüreceğinizi öğrenin.
keywords: Java kullanarak Çalışma Kitabını json a dönüştürme, Excel i JSON olarak dönüştürme, Excel i JSON olarak kaydetme, Java kullanarak Çalışma Kitabını JSON a dönüştürme, Java kullanarak Çalışma Kitabını JSON olarak kaydetme, Excel i JSON olarak dışa aktarma via Java.
---

{{% alert color="primary" %}}

Aspose.Cells, bir Workbook'ü Json (JavaScript Object Notation) dosyasına dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştürme**

Excel Çalışma Kitabını JSON'a nasıl dönüştüreceğinizi merak etmeyin, çünkü Aspose.Cells Java kütüphanesi en iyi kararı verir. Aspose.Cells Java API; elektronik tabloları JSON formatına dönüştürmeyi destekler. Çalışma kitabını JSON'a dışa aktarmak için, [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) parametresi olarak [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) yönteminin ikinci parametresi olarak ekleyin. Ayrıca, çalışma sayfasını JSON'a dışa aktarıp ek ayarları belirtmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, Excel Çalışma Kitabı'nın Json olarak dışa aktarılmasını gösterir. Referans için, kod tarafından oluşturulan Json dosyası için [örnek dosyayı](sample.xlsx) dönüştürme koduna bakın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

Aşağıdaki kod örneği, ek ayarları belirtmek için JsonSaveOptions sınıfını kullanan Excel Workbook'ünü Json olarak dışa aktarmanın bir örneğini göstermektedir. Referans için kodu görmek için [kaynak dosyayı](sample.xlsx) kodla üretilen Json dosyası ile birlikte inceleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
