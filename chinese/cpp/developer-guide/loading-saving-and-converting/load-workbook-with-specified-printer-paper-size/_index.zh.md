---
title: 加载指定打印纸张大小的工作簿
type: docs
weight: 430
url: /zh/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

您可以使用 [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/) 方法在加载工作簿时指定所需的打印纸张大小。请注意，如果你在MS Excel中创建一个新文件，你会发现纸张大小与你的机器上默认打印机的设置相同。

{{% /alert %}}

以下示例代码展示了[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/)方法的用法。它首先创建一个工作簿，然后以XLSX格式将其保存在内存流中。然后用A5纸张大小加载并保存为PDF格式，再用A3纸张大小加载再次保存为PDF。如果打开输出的PDF并检查纸张大小，你会看到它们不同，一个是A5，另一个是A3。请下载由代码生成的[A5输出PDF](PrinterSize-a5_out.pdf)和[A3输出PDF](PrinterSize-a3_out.pdf)以供参考。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
