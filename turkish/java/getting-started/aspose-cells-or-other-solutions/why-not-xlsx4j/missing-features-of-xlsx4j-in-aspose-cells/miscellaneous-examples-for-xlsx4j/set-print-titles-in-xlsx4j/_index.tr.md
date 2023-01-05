---
title: xlsx4j'de Yazdırma Başlıklarını Ayarlama
type: docs
weight: 40
url: /tr/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - Baskı Başlıklarını Ayarla**
Aspose.Cells, yazdırılan bir çalışma sayfasının tüm sayfalarında yinelenecek satır ve sütun başlıkları belirlemenizi sağlar. Bunu yapmak için[Sayfa ayarı](/java/PageSetup)class'setPrintTitleColumns ve setPrintTitleRows özellikleri.

Tekrarlanacak satır veya sütunlar, satır veya sütun numaraları geçirilerek tanımlanır. Örneğin, satırlar $1:$2 olarak tanımlanır ve sütunlar $A:$B olarak tanımlanır.

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Yazdırma Seçeneklerini Ayarlama](/cells/tr/java/page-setup-features/#setting-print-options).

{{% /alert %}}
