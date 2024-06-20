---
title: Aspose.Cells te İş Kitaplarını Yazdırma
type: docs
weight: 20
url: /tr/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - İş Kitaplarını Yazdırma**
Tablonuzu oluşturmayı bitirdikten sonra muhtemelen ihtiyacınız olan tablonun kağıt kopyasını yazdırmak olacaktır. Yazdırırken, MS Excel, seçiminizi belirtmedikçe tüm çalışma sayfasını yazdırmak istediğinizi varsayar.

Çalışma Sayfasını Yazdırma

**C#**

{{< highlight cs >}}

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
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **İş Kitaplarını Yazdırma** formunu indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla bilgi için [İş Kitaplarını Yazdırma](/cells/tr/net/printing-workbooks/) sayfasını ziyaret edin.

{{% /alert %}}
