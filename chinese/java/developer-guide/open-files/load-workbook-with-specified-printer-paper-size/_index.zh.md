---
title: 加载指定打印纸张大小的工作簿
type: docs
weight: 790
url: /zh/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

您可以在加载工作簿时使用[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\))方法指定您选择的打印纸张大小。请注意，如果在MS Excel中创建新文件，则会发现纸张大小与您机器上默认打印机的设置相同。

{{% /alert %}} 
## **加载带有指定打印纸张大小的工作簿**
以下示例代码说明了[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\))方法的用法。它首先创建一个工作簿，然后以XLSX格式将其保存在字节数组流中。然后将其以A5纸张大小加载，并以PDF格式保存。然后以A3纸张大小再次加载并再次以PDF格式保存。如果您打开输出的PDF并检查其纸张大小，您将看到它们是不同的。一个是A5，另一个是A3。请根据提供的代码下载由该代码生成的[A5输出PDF](5473435.pdf)和[A3输出PDF](5473436.pdf)进行参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
