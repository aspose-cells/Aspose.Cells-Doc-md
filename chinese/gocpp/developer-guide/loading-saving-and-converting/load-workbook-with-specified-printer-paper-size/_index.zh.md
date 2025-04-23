---
title: 加载指定打印纸张大小的工作簿
type: docs
weight: 430
url: /zh/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

您可以在加载工作簿时使用[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/)方法指定所需的打印纸张大小。请注意，如果在Microsoft Excel中新建文件，默认打印机的纸张大小会被应用设置覆盖。

{{% /alert %}}

以下示例演示了如何使用[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/)方法。首先创建一个工作簿，然后在内存流中以XLSX格式保存。之后以A5纸张大小加载，保存为PDF格式；再以A3纸张大小加载，保存为PDF。打开输出的PDF文件检查纸张大小即可看到不同的设置。可下载由此代码生成的[A5输出PDF](PrinterSize-a5_out.pdf) 和 [A3输出PDF](PrinterSize-a3_out.pdf)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
