---
title: Neues Arbeitsblatt erstellen
type: docs
weight: 10
url: /de/java/create-new-worksheet/
---

## **Aspose.Cells - Neues Arbeitsblatt erstellen**
Ein Arbeitsblatt zu Arbeitsmappe hinzufügen

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet worksheet = worksheets.add("My Worksheet");

//Saving the Excel file

workbook.save("newWorksheet.xls");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Neues Arbeitsblatt erstellen**
Ein Arbeitsblatt zu Arbeitsmappe hinzufügen

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook(); // or new XSSFWorkbook();

Sheet sheet1 = wb.createSheet("new sheet");

Sheet sheet2 = wb.createSheet("second sheet");

// Note that sheet name is Excel must not exceed 31 characters

// and must not contain any of the any of the following characters:

// 0x0000

// 0x0003

// colon (:)

// backslash (\)

// asterisk (*)

// question mark (?)

// forward slash (/)

// opening square bracket ([)

// closing square bracket (])

// You can use org.apache.poi.ss.util.WorkbookUtil#createSafeSheetName(String nameProposal)}

// for a safe way to create valid names, this utility replaces invalid characters with a space (' ')

String safeName = WorkbookUtil.createSafeSheetName("[O'Brien's sales*?]");

Sheet sheet3 = wb.createSheet(safeName);

FileOutputStream fileOut = new FileOutputStream("newWorksheet.xls");

wb.write(fileOut);

fileOut.close();


{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/createnewworksheet)
{{< app/cells/assistant language="java" >}}
