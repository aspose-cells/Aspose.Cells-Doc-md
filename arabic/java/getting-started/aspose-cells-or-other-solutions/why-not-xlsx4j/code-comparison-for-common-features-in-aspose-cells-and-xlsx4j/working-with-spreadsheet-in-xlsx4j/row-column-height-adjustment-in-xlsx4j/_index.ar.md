---
title: ضبط ارتفاع الصف والعمود في xlsx4j
type: docs
weight: 50
url: /ar/java/row-column-height-adjustment-in-xlsx4j/
---

## **Aspose.Cells - تعديل ارتفاع الصف والعمود**
من الممكن تعيين ارتفاع صف واحد عن طريق استدعاء طريقة setRowHeight لمجموعة Cells. تأخذ طريقة setRowHeight  المعلمات التالية:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

قم بتعيين عرض عمود عن طريق استدعاء طريقة setColumnWidth لمجموعة Cells. تأخذ طريقة setColumnWidth  المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Setting the height of all rows in the worksheet to 8

worksheet.getCells().setStandardHeight(8f);

//Setting the height of the second row to 40

cells.setRowHeight(1, 40);



//Setting the width of the second column to 17.5

cells.setColumnWidth(1, 17.5);

{{< /highlight >}}
## **xlsx4j - تعديل ارتفاع الصف والعمود**
يُستخدم Row.setHt لتعيين ارتفاع مخصص للصفوف باستخدام xlsx4j. يجب تعيين setCustomHeight على TRUE.

**Java**

{{< highlight java >}}

 SpreadsheetMLPackage pkg = SpreadsheetMLPackage.createPackage();

WorksheetPart sheet = pkg.createWorksheetPart(new PartName("/sheet1.xml"), "Sheet1", 1);

CTSheetFormatPr format = Context.getsmlObjectFactory().createCTSheetFormatPr();

format.setDefaultRowHeight(5);

format.setCustomHeight(Boolean.TRUE);

sheet.getJaxbElement().setSheetFormatPr(format);

SheetData sheetData = sheet.getJaxbElement().getSheetData();

Row row = Context.getsmlObjectFactory().createRow();

row.setHt(66.0);

row.setCustomHeight(Boolean.TRUE);

row.setR(1L);

Cell cell1 = Context.getsmlObjectFactory().createCell();

cell1.setV("1234");

row.getC().add(cell1);

Cell cell2 = Context.getsmlObjectFactory().createCell();

cell2.setV("56");

row.getC().add(cell2);

sheetData.getRow().add(row);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/worksheet/adjustheight)

{{% alert color="primary" %}} 

للمزيد من التفاصيل، قم بزيارة [ضبط ارتفاع الصف وعرض العمود](/java/adjusting-row-height-and-volumn-width).

{{% /alert %}}
