---
title: إخفاء وإلغاء إخفاء Cells
type: docs
weight: 30
url: /ar/java/hide-and-unhide-cells/
---
## **Aspose.Cells - إخفاء وإظهار الصفوف والأعمدة**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) ، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. توفر فئة ورقة العمل مجموعة Cells تمثل كافة الخلايا في ورقة العمل. توفر مجموعة Cells عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل.

**Java**

{{< highlight "java" >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - إخفاء / إظهار Cells**
لإخفاء صف أو عمود ، توفر Apache POI SS طريقة Row.setZeroHeight (منطقية).

**Java**

{{< highlight "java" >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / cellrowscolumns / hideunhidecells)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[إخفاء وإظهار الصفوف والأعمدة](/java/hiding-and-showing-rows-and-columns).

{{% /alert %}}
