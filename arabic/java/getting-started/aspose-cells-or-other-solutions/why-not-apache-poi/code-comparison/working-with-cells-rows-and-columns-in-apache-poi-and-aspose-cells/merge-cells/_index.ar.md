---
title: دمج الخلايا
type: docs
weight: 60
url: /ar/java/merge-cells/
---

## **أسبوس.سيلز - دمج الخلايا**
فصيلة الخلايا تحتوي على بعض الطرق المفيدة للمهمة. على سبيل المثال ، تدمج الطريقة الخلايا في خلية واحدة ضمن نطاق محدد من الخلايا.

**Java**

{{< highlight java >}}

 //Create a Workbook.

Workbook wbk = new Workbook();

//Create a Worksheet and get the first sheet.

Worksheet worksheet = wbk.getWorksheets().get(0);

//Create a Cells object to fetch all the cells.

Cells cells = worksheet.getCells();

//Merge some Cells (C6:E7) into a single C6 Cell.

cells.merge(5,2,2,3);

//Input data into C6 Cell.

worksheet.getCells().get(5,2).setValue("This is a test of merging");

//Save the Workbook.

wbk.save(dataDir + "merge_Aspose.xls");

{{< /highlight >}}
## **أباتشي POI SS - HSSF XSSF - دمج الخلايا**
يمكن استخدام Sheet.addMergedRegion لدمج الخلايا.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

Row row = sheet.createRow((short) 1);

Cell cell = row.createCell((short) 1);

cell.setCellValue("This is a test of merging");

sheet.addMergedRegion(new CellRangeAddress(

        1, //first row (0-based)

        1, //last row  (0-based)

        1, //first column (0-based)

        2  //last column  (0-based)

));

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/mergecells)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، يرجى زيارة [دمج وفك دمج (تقسيم) الخلايا](/cells/ar/java/merging-and-unmerging-cells).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
