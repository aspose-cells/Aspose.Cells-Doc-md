---
title: 加载时使用指定的打印纸张大小的工作簿
type: docs
weight: 790
url: /zh/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

您可以在加载工作簿时使用 [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) 方法指定您选择的打印纸张大小。请注意，如果您在MS Excel中创建一个新文件，您将发现纸张大小与您计算机中默认打印机的设置相同。

{{% /alert %}} 
## **使用指定的打印纸张大小加载工作簿**
以下示例代码说明了使用 [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) 方法。首先创建一个工作簿，然后以XLSX格式将其保存为字节数组流。然后使用A5纸张大小加载它，并将其保存为PDF格式。再次使用A3纸张大小加载它，并将其再次保存为PDF格式。如果您打开输出的PDF并检查它们的纸张大小，您将看到它们是不同的。一个是A5，另一个是A3。请下载代码生成的 [A5输出PDF](5473435.pdf) 和 [A3输出PDF](5473436.pdf) 以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
