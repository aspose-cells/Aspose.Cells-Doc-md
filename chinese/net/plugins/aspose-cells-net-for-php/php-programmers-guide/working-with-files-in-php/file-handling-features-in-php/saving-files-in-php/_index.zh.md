---
title: 在PHP中保存文件
type: docs
weight: 20
url: /zh/net/saving-files-in-php/
---

## **Aspose.Cells - 保存Excel文件**
### **通过路径打开**
通过引用文件的路径保存Microsoft Excel文件

**PHP代码**

{{< highlight php >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        //Your Code goes here for any workbook related operations

        $ptr->Call($workbook,"Save",array($dataDir.'/book1.xls'));

        print "File saved successfully!" . PHP_EOL;

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**保存文件（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
