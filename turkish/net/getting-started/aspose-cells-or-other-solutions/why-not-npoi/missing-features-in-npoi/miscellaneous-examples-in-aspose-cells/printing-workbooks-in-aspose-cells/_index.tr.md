---
title: Aspose.Cells'de Çalışma Kitaplarını Yazdırma
type: docs
weight: 20
url: /tr/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - Çalışma Kitaplarını Yazdırma**
Elektronik tablonuzu oluşturmayı bitirdikten sonra, ihtiyaçlarınız için büyük olasılıkla sayfanın basılı bir kopyasını yazdırmak isteyeceksiniz. Yazdırırken, seçiminizi belirtmediğiniz sürece, MS Excel tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar.

Yazdırma Çalışma Sayfası

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Çalışma Kitaplarını Yazdırma** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Kitaplarını Yazdırma](/cells/tr/net/printing-workbooks/).

{{% /alert %}}
