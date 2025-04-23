---
title: استيراد من مصفوفة
type: docs
weight: 10
url: /ar/net/importing-from-array/
---

يمكن للمطورين استيراد البيانات من مصفوفة إلى ورقة العمل الخاصة بهم من خلال استدعاء الأسلوب **ImportArray** من مجموعة الخلايا. هناك العديد من الإصدارات المتعددة لأسلوب ImportArray ولكن الإصدار النموذجي يأخذ المعلمات التالية:

- مصفوفة, يمثل كائن المصفوفة التي تحتاج إلى استيراد محتوياتها
- رقم الصف, يمثل رقم الصف لأول خلية حيث سيتم استيراد البيانات
- رقم العمود, يمثل رقم العمود لأول خلية حيث سيتم استيراد البيانات
- هل هو عمودي, قيمة منطقية تحدد استيراد البيانات عموديا أم أفقيا

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array.xls");

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
