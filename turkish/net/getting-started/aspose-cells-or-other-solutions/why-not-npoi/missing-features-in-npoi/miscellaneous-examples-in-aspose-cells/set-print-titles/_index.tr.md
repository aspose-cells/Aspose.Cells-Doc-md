---
title: Baskı Başlıklarını Ayarla
type: docs
weight: 30
url: /tr/net/set-print-titles/
---
## **Aspose.Cells - Baskı Başlıklarını Ayarla**
Aspose.Cells, yazdırılan bir çalışma sayfasının tüm sayfalarında yinelenecek satır ve sütun başlıkları belirlemenizi sağlar. Bunu yapmak için[Sayfa ayarı](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)sınıf PrintTitleColumns ve PrintTitleRows özellikleri.

Tekrarlanacak satır veya sütunlar, satır veya sütun numaraları geçirilerek tanımlanır. Örneğin, satırlar $1:$2 olarak tanımlanır ve sütunlar $A:$B olarak tanımlanır.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Baskı Başlıklarını Ayarla** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Yazdırma Seçeneklerini Ayarlama](/cells/tr/net/setting-print-options/).

{{% /alert %}}
