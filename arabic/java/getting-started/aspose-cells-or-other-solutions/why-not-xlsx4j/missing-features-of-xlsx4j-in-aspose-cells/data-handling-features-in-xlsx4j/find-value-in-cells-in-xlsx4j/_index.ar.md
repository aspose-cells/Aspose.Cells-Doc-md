---
title: العثور على قيمة في الخلايا في xlsx4j
type: docs
weight: 30
url: /ar/java/find-value-in-cells-in-xlsx4j/
---

## **أسبوز.خلايا - العثور على القيمة في الخلايا**
في Microsoft Excel ، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال، بالنقر على **تحرير** ثم **البحث** يفتح مربع البحث. يُدخل المستخدم قيمة وينقر **موافق** للبحث عنها. يقوم Excel بتحديد الحقول المطابقة.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [البحث عن البيانات](/cells/ar/java/find-or-search-data).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
