---
title: Sayfa Ayarı  Sayfaya Sığdırma Ayarı
type: docs
weight: 30
url: /tr/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Sayfa Ayarı - Sayfaya Sığdırma Ayarı**
Çalışsayfadaki içeriği belirli bir sayıda sayfaya sığdırmak için, [PageSetup](/cells/tr/java/page-setup-fit-to-page-setting/) sınıfının setFitToPagesTall ve setFitToPagesWide metodlarını kullanın. Bu metodlar aynı zamanda çalışsayfalarını ölçeklendirmek için de kullanılır.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Sayfa Ayarı - Sayfaya Sığdırma Ayarı**
Apache POI SS, sayfaya sığdırma ayarları için setFitHeight ve setFitWidth metodlarını kullanır.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

Daha fazla detay için [Sayfa Seçeneklerini Ayarlama](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options) adresini ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
