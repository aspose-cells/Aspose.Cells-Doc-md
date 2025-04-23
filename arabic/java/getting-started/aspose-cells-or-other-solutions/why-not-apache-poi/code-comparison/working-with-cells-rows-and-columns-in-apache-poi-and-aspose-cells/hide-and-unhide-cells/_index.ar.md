---
title: إخفاء وإظهار الخلايا
type: docs
weight: 30
url: /ar/java/hide-and-unhide-cells/
---

## **Aspose.Cells - إخفاء وإظهار الصفوف والأعمدة**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة WorksheetCollection التي تسمح بالوصول إلى كل ورق عمل في ملف Excel. تمثل الورقة عمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر الفئة Worksheet مجموعة Cells التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة Cells عدة أساليب لإدارة الصفوف أو الأعمدة في ورقة العمل. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - إخفاء / إظهار الخلايا**
يوفر Apache POI SS طريقة Row.setZeroHeight(boolean) لإخفاء صف أو عمود.

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إخفاء وعرض الصفوف والأعمدة](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
