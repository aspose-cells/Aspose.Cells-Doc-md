---
title: Çalışma Kitaplarını xlsx4j'de Yazdırma
type: docs
weight: 30
url: /tr/java/printing-workbooks-in-xlsx4j/
---
## **Aspose.Cells - Çalışma Kitaplarını Yazdırma**
Elektronik tablonuzu oluşturmayı bitirdikten sonra, ihtiyaçlarınız için büyük olasılıkla sayfanın basılı bir kopyasını yazdırmak isteyeceksiniz. Yazdırırken, seçiminizi belirtmediğiniz sürece, MS Excel tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar.

**Yazdırma Çalışma Sayfası**

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

**Çalışma Kitabını Yazdırma**

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[ Çalışma Kitaplarını Yazdırma](/cells/tr/java/printing-workbooks).

{{% /alert %}}
