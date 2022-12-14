---
title: 在 PHP 中打开文件
type: docs
weight: 10
url: /zh/java/opening-files-in-php/
---
## **Aspose.Cells - 打开 Excel 文件的简单方法**
### **通过路径打开**
只需通过引用文件路径打开 Microsoft Excel 文件

**PHP代码**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **通过流打开**
有时，您要打开的 Excel 文件存储为流。在这种情况下，请使用 Open 方法的重载版本，该方法采用包含 Excel 文件的 Stream 对象来打开文件。

**PHP代码**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **下载运行代码**
下载**打开文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
