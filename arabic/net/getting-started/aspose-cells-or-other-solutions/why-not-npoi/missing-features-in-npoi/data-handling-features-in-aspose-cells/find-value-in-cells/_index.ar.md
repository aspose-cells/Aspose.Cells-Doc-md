---
title: أوجد القيمة في Cells
type: docs
weight: 20
url: /ar/net/find-value-in-cells/
---
## **Aspose.Cells - أوجد القيمة في Cells**
في Microsoft Excel ، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال ، النقر فوق**يحرر**وثم**تجد**يفتح مربع حوار البحث. يقوم المستخدمون بإدخال قيمة والنقرات**نعم**للبحث عنه. يبرز Excel الحقول المتطابقة.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**أوجد القيمة في Cells** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[البحث عن البيانات أو البحث عنها](/cells/ar/net/find-or-search-data/).

{{% /alert %}}
