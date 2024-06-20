---
title: استيراد من ArrayList
type: docs
weight: 20
url: /ar/net/importing-from-arraylist/
---

يمكن للمطورين استيراد البيانات من ArrayList إلى ورقة العمل الخاصة بهم من خلال استدعاء الأسلوب **ImportArrayList** من مجموعة الخلايا. يأخذ أسلوب ImportArray المعلمات التالية: **ArrayList** , يمثل كائن ArrayList الذي تحتاج إلى استيراد محتوياته

- رقم الصف , يمثل رقم الصف لأول خلية حيث سيتم استيراد البيانات
- رقم العمود , يمثل رقم العمود لأول خلية حيث سيتم استيراد البيانات
- هل هو عمودي , قيمة منطقية تحدد استيراد البيانات عموديا أم أفقيا

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save("DataImport from Array List.xls");


{{< /highlight >}}
