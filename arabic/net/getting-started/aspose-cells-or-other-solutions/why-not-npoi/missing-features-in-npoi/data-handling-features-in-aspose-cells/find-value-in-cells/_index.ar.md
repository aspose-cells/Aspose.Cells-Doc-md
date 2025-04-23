---
title: العثور على القيمة في الخلايا
type: docs
weight: 20
url: /ar/net/find-value-in-cells/
---

## **أسبوز.خلايا - العثور على القيمة في الخلايا**
في Microsoft Excel ، يمكن للمستخدمين البحث عن الخلايا التي تحتوي على بيانات محددة. على سبيل المثال، بالنقر على **تحرير** ثم **البحث** يفتح مربع البحث. يُدخل المستخدم قيمة وينقر **موافق** للبحث عنها. يقوم Excel بتحديد الحقول المطابقة.

**C#**

{{< highlight cs >}}

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
## **تحميل رمز التشغيل**
تنزيل **العثور على القيمة في الخلايا** من أي من مواقع التشفير الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [البحث عن البيانات](/cells/ar/net/find-or-search-data/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
