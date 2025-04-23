---
title: Yazdırma Başlıklarını Ayarlama
type: docs
weight: 10
url: /tr/java/set-print-titles/
---

## **Aspose.Cells - Yazdırma Başlıklarını Ayarlama**
Aspose.Cells, yazdırılan bir çalışma sayfasının tüm sayfalarında tekrar edecek satır ve sütun başlıklarını belirtmenize olanak tanır. Bunu yapmak için [PageSetup](/java/pagesetup) sınıfının setPrintTitleColumns ve setPrintTitleRows özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

**Java**

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Yazdırma Seçeneklerini Ayarlama](/cells/tr/java/page-setup-features/#setting-print-options) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
