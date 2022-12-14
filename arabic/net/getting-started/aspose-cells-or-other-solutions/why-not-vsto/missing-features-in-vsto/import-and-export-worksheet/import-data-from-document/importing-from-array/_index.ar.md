---
title: الاستيراد من Array
type: docs
weight: 10
url: /ar/net/importing-from-array/
---
 يمكن للمطورين استيراد البيانات من مصفوفة إلى أوراق العمل الخاصة بهم عن طريق استدعاء**ImportArray** طريقة جمع Cells. هناك العديد من الإصدارات المحملة بشكل زائد من طريقة ImportArray ولكن الحمل الزائد النموذجي يأخذ المعلمات التالية:

- Array ، يمثل كائن المصفوفة الذي تحتاج محتوياته إلى الاستيراد
- رقم الصف ، يمثل رقم الصف للخلية الأولى حيث سيتم استيراد البيانات
- رقم العمود ، يمثل رقم العمود للخلية الأولى حيث سيتم استيراد البيانات
- هو عمودي ، قيمة منطقية تحدد استيراد البيانات عموديًا أو أفقيًا

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
