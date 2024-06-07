---
title: 加载时使用指定的打印纸张大小的工作簿
type: docs
weight: 430
url: /zh/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

您可以使用[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)方法在加载工作簿时指定所需的打印纸张大小。请注意，如果在MS Excel中创建新文件，则会发现纸张大小与计算机上默认打印机的设置相同。

{{% /alert %}}

以下示例代码说明了[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize)方法的用法。它首先创建一个工作簿，然后以XLSX格式将其保存在内存流中。然后使用A5纸张大小加载它，并将其保存为PDF格式。然后再次使用A3纸张大小加载它，并再次保存为PDF格式。如果打开输出PDF并检查其纸张大小，则会看到它们不同。一个是A5，另一个是A3。请下载代码生成的[ A5输出PDF](5115234.pdf)和[ A3输出PDF](5115233.pdf)以供参考。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
