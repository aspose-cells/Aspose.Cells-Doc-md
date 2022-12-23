---
title: أوجد القيمة في Cells في xlsx4j
type: docs
weight: 30
url: /ar/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - أوجد القيمة في Cells**
في Microsoft Excel ، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال ، النقر فوق**تعديل**وثم**يجد**يفتح مربع حوار البحث. يقوم المستخدمون بإدخال قيمة والنقرات**نعم**للبحث عنه. يبرز Excel الحقول المتطابقة.

**Java**

{{< highlight "java" >}}

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[البحث عن البيانات أو البحث عنها](/cells/ar/java/find-or-search-data).

{{% /alert %}}
