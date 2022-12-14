---
title: 从数组导入
type: docs
weight: 10
url: /zh/net/importing-from-array/
---
开发人员可以通过调用**导入数组**Cells采集方法。 ImportArray 方法有许多重载版本，但典型的重载采用以下参数：

- Array，表示需要导入内容的数组对象
- Row Number，表示要导入数据的第一个单元格的行号
- Column Number，表示将导入数据的第一个单元格的列号
- is Vertical，布尔值，指定垂直或水平导入数据

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
