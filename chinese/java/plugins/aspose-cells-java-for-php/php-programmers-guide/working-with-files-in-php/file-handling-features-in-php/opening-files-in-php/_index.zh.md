---
title: 在PHP中打开文件
type: docs
weight: 10
url: /zh/java/opening-files-in-php/
---

## **Aspose.Cells - 打开Excel文件的简单方法**
### **通过路径打开**
通过引用文件路径简单地打开Microsoft Excel文件

**PHP 代码**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **通过流打开**
有时，要打开的Excel文件存储为流。在这种情况下，使用**Stream**对象包含的Excel文件的重载版本的 **Open** 方法来打开文件。

**PHP 代码**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编码网站下载**打开文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
