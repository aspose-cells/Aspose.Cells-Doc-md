---
title: 在Php中管理工作表
type: docs
weight: 10
url: /zh/java/managing-worksheets-in-php/
---

## **Aspose.Cells - 管理工作表**
### **向新的Excel文件添加工作表**
要使用 **Aspose.Cells Java for PHP** 向新的Excel文件添加工作表, 只需调用 **ManagingWorksheets** 模块的 **add_worksheet** 方法。

**PHP 代码**

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **使用工作表名称移除工作表**
要使用 **Aspose.Cells Java for PHP** 按表名删除工作表, 只需调用 **ManagingWorksheets** 模块的 **remove_worksheet_by_name** 方法。

**PHP 代码**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **通过页索引删除工作表**
要使用 **Aspose.Cells Java for PHP** 按表索引删除工作表, 只需调用 **ManagingWorksheets** 模块的 **remove_worksheet_by_index** 方法。

**PHP 代码**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**Managing Worksheets (Aspose.Cells)**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
