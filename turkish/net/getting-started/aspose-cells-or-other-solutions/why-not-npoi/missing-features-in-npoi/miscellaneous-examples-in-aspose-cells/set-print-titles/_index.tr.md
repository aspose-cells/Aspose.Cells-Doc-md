---
title: Yazdırma Başlıklarını Ayarlama
type: docs
weight: 30
url: /tr/net/set-print-titles/
---

## **Aspose.Cells - Yazdırma Başlıklarını Ayarlama**
Aspose.Cells, bir çalışma sayfasının tüm sayfalarında tekrarlanacak satır ve sütun başlıklarını belirlemenize olanak tanır. Bunu yapmak için [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfının PrintTitlerColumns ve PrintTitleRows özelliklerini kullanın.

Tekrar edilecek satırlar veya sütunlar, satır veya sütun numaralarını geçirerek tanımlanır. Örneğin satırlar $1:$2 ve sütunlar $A:$B olarak tanımlanır.

**C#**

{{< highlight cs >}}

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
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Yazdırma Başlıklarını Ayarlama** formunu indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Yazdırma Seçeneklerini Ayarlama](/cells/tr/net/setting-print-options/) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
