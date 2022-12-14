---
title: 在 Php 中管理工作表
type: docs
weight: 10
url: /zh/java/managing-worksheets-in-php/
---
## **Aspose.Cells - 管理工作表**
### **将工作表添加到新的 Excel 文件**
使用以下方法将工作表添加到新的 Excel 文件**Aspose.Cells Java 用于 PHP** 只需调用**添加工作表**的方法**管理工作表**模块。

**PHP代码**

{{< highlight "php" >}}

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
### **使用工作表名称删除工作表**
要使用工作表名称删除工作表**Aspose.Cells Java 用于 PHP** 只需调用**按名称删除工作表**的方法**管理工作表**模块。

**PHP代码**

{{< highlight "php" >}}

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
要按工作表索引删除工作表，请使用**Aspose.Cells Java 用于 PHP** 只需调用**按索引删除工作表**的方法**管理工作表**模块。

**PHP代码**

{{< highlight "php" >}}

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
下载**管理工作表 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
