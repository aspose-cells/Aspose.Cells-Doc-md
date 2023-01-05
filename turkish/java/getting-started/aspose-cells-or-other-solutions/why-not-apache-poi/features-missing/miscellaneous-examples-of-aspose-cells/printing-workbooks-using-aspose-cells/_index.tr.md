---
title: Aspose.Cells kullanarak Çalışma Kitaplarını Yazdırma
type: docs
weight: 20
url: /tr/java/printing-workbooks-using-aspose-cells/
---
## **Aspose.Cells - Çalışma Kitaplarını Yazdırma**
Elektronik tablonuzu oluşturmayı bitirdikten sonra, ihtiyaçlarınız için büyük olasılıkla sayfanın basılı bir kopyasını yazdırmak isteyeceksiniz. Yazdırırken, seçiminizi belirtmediğiniz sürece, MS Excel tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar.

Yazdırma Çalışma Sayfası

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

Çalışma Kitabını Yazdırma

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Kitaplarını Yazdırma](/cells/tr/java/printing-workbooks).

{{% /alert %}}
