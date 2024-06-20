---
title: Çalışan Kodu İndir
type: docs
weight: 50
url: /tr/java/re-order-sheets-within-workbook/
---

## **Örnek Kodu İndir**
Aspose.Cells, aynı elektronik tabloda bir çalışma sayfasını başka bir konuma taşımak için kullanılan Worksheet.moveTo() yöntemini sağlar.

**Java**

{{< highlight java >}}

 //Create a new Workbook.

Workbook workbook = new Workbook();

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet worksheet1 = worksheets.get(0);

Worksheet worksheet2 = worksheets.add("Sheet2");

Worksheet worksheet3 = worksheets.add("Sheet3");

//Move Sheets with in Workbook.

worksheet2.moveTo(0);

worksheet1.moveTo(1);

worksheet3.moveTo(2);

//Save the excel file.

workbook.save(dataDir + "AsposeMoveSheet.xls");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Çalışma Kitabı İçinde Sayfaların Yeniden Sıralanması**
Apache POI, çalışma sayfalarını istenen sırada ayarlamak için Workbook.setSheetOrder() metodunu sağlar.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

wb.createSheet("third sheet");

wb.setSheetOrder("second sheet", 0);

wb.setSheetOrder("new sheet", 1);

wb.setSheetOrder("third sheet", 2);

FileOutputStream fileOut = new FileOutputStream(dataDir + "Apache_Reordered.xls");

wb.write(fileOut);

fileOut.close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/reordersheets)

{{% alert color="primary" %}} 

Daha fazla detay için [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/java/calisma-sayfalarini-kopyalama-ve-tasima) sayfasını ziyaret edin.

{{% /alert %}}
