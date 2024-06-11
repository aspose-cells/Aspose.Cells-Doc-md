---
title: 将数据导入xlsx4j工作表
type: docs
weight: 50
url: /zh/java/import-data-to-worksheets-in-xlsx4j/
---

## **Aspose.Cells - 将数据导入工作表**
从数组中导入数据

Java

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the newly added worksheet by passing its sheet index

int sheetIndex = workbook.getWorksheets().add();

Worksheet worksheet= workbook.getWorksheets().get(sheetIndex);

//==================================================

//Creating an array containing names as string values

String[] names = new String[]{"laurence chen", "roman korchagin", "kyle huang"};

//Importing the array of names to 1st row and first column vertically

Cells cells = worksheet.getCells();

cells.importArray(names,0,0,false);

{{< /highlight >}}

从ArrayList中导入数据

Java

{{< highlight java >}}

 ArrayList<String> list = new ArrayList<String>();

//Add few names to the list as string values

list.add("laurence chen");

list.add("roman korchagin");

list.add("kyle huang");

//Importing the contents of ArrayList to 1st row and first column vertically

cells.importArrayList(list,2,0,true);

//==================================================

//Saving the Excel file

workbook.save(dataDir + "AsposeDataImport.xls");

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/importdatatoworksheets/AsposeImportDataToWorksheets.java)
