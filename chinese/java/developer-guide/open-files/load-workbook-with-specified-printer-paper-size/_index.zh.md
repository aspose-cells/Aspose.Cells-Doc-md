---
title: 加载指定打印纸张大小的工作簿
type: docs
weight: 790
url: /zh/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

在加载工作簿时，可以使用 [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) 方法指定所需的打印纸张大小。请注意，如果在 MS Excel 中创建新文件，则会发现纸张大小与机器的默认打印机设置相同。

{{% /alert %}} 
## **加载带有指定打印纸张大小的工作簿**
以下示例代码说明了 [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) 方法的用法。它首先创建一个工作簿，然后将其保存为 XLSX 格式的字节数组流。接着用 A5 纸张大小加载，并保存为 PDF 格式。然后再次用 A3 纸张大小加载，并再次保存为 PDF。如果打开输出的 PDF 并检查其纸张大小，会看到它们不同，一个是 A5，另一个是 A3。请下载由代码生成的 [A5 输出 PDF](5473435.pdf) 和 [A3 输出 PDF](5473436.pdf) 以供参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
