---
title: 从数组导入
type: docs
weight: 10
url: /zh/net/importing-from-array/
---

开发人员可以通过调用Cells集合的**ImportArray**方法将数据从数组导入其工作表。 ImportArray方法有许多重载版本，但典型的重载使用以下参数：

- 数组，表示需要导入其内容的数组对象
- 行号，表示导入数据的第一个单元格的行号
- 列号，表示导入数据的第一个单元格的列号
- 是否垂直，一个布尔值，指定垂直还是水平导入数据

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
