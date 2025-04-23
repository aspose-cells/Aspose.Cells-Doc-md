---
title: Aspose.Cells kullanarak İş Kitaplarını Yazdırma
type: docs
weight: 20
url: /tr/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - İş Kitaplarını Yazdırma**
Tablonuzu oluşturmayı bitirdikten sonra muhtemelen ihtiyacınız olan tablonun kağıt kopyasını yazdırmak olacaktır. Yazdırırken, MS Excel, seçiminizi belirtmedikçe tüm çalışma sayfasını yazdırmak istediğinizi varsayar.

Çalışma Sayfasını Yazdırma

**Java**

{{< highlight java >}}

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

Örnek Kodu İndirme

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Kitaplarını Yazdırma](/cells/tr/java/printing-workbooks) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
