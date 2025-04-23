---
title: 加载指定打印纸张大小的工作簿
type: docs
weight: 430
url: /zh/python-net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

您可以使用 [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size) 方法在加载工作簿时指定所需的打印纸张大小。请注意，如果你在MS Excel中创建一个新文件，你会发现纸张大小与你的机器上默认打印机的设置相同。

{{% /alert %}}

以下示例代码说明了 [**LoadOptions.set_paper_size()**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/set_paper_size) 方法的用法。它首先创建一个工作簿，然后以XLSX格式保存到内存流中。然后在A5纸张大小下加载它并以PDF格式保存。然后再以A3纸张大小加载它，并再次以PDF格式保存。如果你打开输出的PDF并检查它们的纸张大小，你会发现它们是不同的。一个是A5，另一个是A3。请下载代码生成的 [A5输出PDF](5115234.pdf) 和 [A3输出PDF](5115233.pdf) 供参考。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-LoadWorkbookWithPrinterSize-1.py" >}}

