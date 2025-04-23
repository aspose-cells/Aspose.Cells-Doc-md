---
title: Baskı Alanı Ayarla
type: docs
weight: 40
url: /tr/java/set-print-area/
---

## **Aspose.Cells - Baskı Alanı Ayarla**
Varsayılan olarak, sadece veri içeren çalışma sayfasının tüm alanlarını içeren baskı alanı oluşturulur. Geliştiriciler, çalışma sayfasının belirli bir baskı alanını belirleyebilirler.

Belirli bir baskı alanını seçmek için, [PageSetup](/java/pagesetup) sınıfının setPrintArea metodunu kullanın. Bu özelliği belirleyen baskı alanını tanımlayan bir hücre aralığını atayın.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Baskı Alanı Ayarla**
Workbook.setPrintArea yöntemi, baskı alanının sayfa özelliklerini ayarlamak için kullanılabilir.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Yazdırma Seçeneklerini Ayarlama](/cells/tr/java/page-setup-features/#setting-print-options) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
