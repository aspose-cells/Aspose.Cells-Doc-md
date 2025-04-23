---
title: 从ArrayList导入
type: docs
weight: 20
url: /zh/net/importing-from-arraylist/
---

开发人员可以通过调用Cells集合的**ImportArrayList**方法将数据从ArrayList导入其工作表。 ImportArray方法采用以下参数：**ArrayList**，表示需要导入其内容的ArrayList对象

- 行号，表示将要导入数据的第一个单元格的行号
- 列编号，表示要导入数据的第一个单元格的列号
- 是否垂直，一个布尔值，指定是垂直导入数据还是水平导入数据

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
{{< app/cells/assistant language="csharp" >}}
