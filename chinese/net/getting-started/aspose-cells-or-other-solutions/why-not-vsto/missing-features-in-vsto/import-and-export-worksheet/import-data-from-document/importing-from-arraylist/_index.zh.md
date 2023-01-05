---
title: 从 ArrayList 导入
type: docs
weight: 20
url: /zh/net/importing-from-arraylist/
---
开发人员可以通过调用**导入数组列表**Cells采集方法。 ImportArray 方法采用以下参数：**数组列表** ,代表需要导入内容的ArrayList对象

- Row Number ，表示要导入数据的第一个单元格的行号
- Column Number ，表示将导入数据的第一个单元格的列号
- 是 Vertical ，一个布尔值，指定垂直或水平导入数据

{{< highlight "csharp" >}}

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
