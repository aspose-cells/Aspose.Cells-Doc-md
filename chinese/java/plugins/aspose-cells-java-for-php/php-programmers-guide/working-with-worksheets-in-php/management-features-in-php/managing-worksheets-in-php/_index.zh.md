---
title: 在Php中管理工作表
type: docs
weight: 10
url: /zh/java/managing-worksheets-in-php/
---

## **Aspose.Cells - 管理工作表**
### **向新的Excel文件中添加工作表**
要使用**Aspose.Cells Java for PHP**将工作表添加到新的Excel文件中，请简单调用**MangingWorksheets**模块的**add_worksheet**方法。

**PHP代码**

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
### **使用表名删除工作表**
使用**Aspose.Cells Java for PHP**，通过调用**MangingWorksheets**模块的**remove_worksheet_by_name**方法来根据工作表名称删除工作表。

**PHP代码**

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
### **使用工作表索引删除工作表**
使用**Aspose.Cells Java for PHP**，通过调用**MangingWorksheets**模块的**remove_worksheet_by_index**方法来根据工作表索引删除工作表。

**PHP代码**

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
从下面列出的任何社交编码站点下载**管理工作表（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
