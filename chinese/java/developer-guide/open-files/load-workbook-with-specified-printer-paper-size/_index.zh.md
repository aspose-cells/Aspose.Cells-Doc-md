---
title: 加载具有指定打印机纸张尺寸的工作簿
type: docs
weight: 790
url: /zh/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

您可以在使用加载工作簿时指定您选择的打印机纸张尺寸[LoadOptions.setPaperSize()方法](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)） 方法。请注意，如果您在 MS Excel 中创建一个新文件，您会发现纸张尺寸与您机器中默认打印机的设置相同。

{{% /alert %}} 
## **加载具有指定打印机纸张尺寸的工作簿**
下面的示例代码说明了[LoadOptions.setPaperSize()方法](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)） 方法。它首先创建一个工作簿，然后将它以XLSX 格式保存在字节数组流中。然后加载 A5 纸张大小并以 PDF 格式保存。然后它再次加载 A3 纸张大小并再次以 PDF 格式保存。如果您打开输出的 PDF 并检查它们的纸张大小，您会发现它们是不同的。一个是A5，另一个是A3。请下载[A5输出PDF](5473435.pdf)和[A3输出PDF](5473436.pdf)生成的代码供大家参考。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
