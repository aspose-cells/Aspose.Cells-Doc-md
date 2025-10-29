---  
title: 使用 Node.js 和 C++ 以指定打印纸张尺寸加载工作簿  
linktitle: 加载指定打印纸张大小的工作簿  
type: docs  
weight: 430  
url: /zh/nodejs-cpp/load-workbook-with-specified-printer-paper-size/  
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 加载工作簿时设置打印纸张大小。  
---  

{{% alert color="primary" %}}  
您可以使用 [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-) 方法在加载工作簿时指定所需的打印纸张大小。请注意，如果你在MS Excel中创建一个新文件，你会发现纸张大小与你的机器上默认打印机的设置相同。  
{{% /alert %}}  

 以下示例代码演示了 [**LoadOptions.setPaperSize(PaperSizeType)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setPaperSize-papersizetype-) 方法的用法。它首先创建一个工作簿，然后将其以 XLSX 格式保存到内存流中。接着，使用 A5 纸张大小加载并保存为 PDF 格式，再以 A3 纸张大小重新加载并保存为 PDF。打开生成的 PDF，检查其纸张大小，您会发现它们不同，一个是 A5，另一个是 A3。请下载由代码生成的 [A5 PDF](5115234.pdf) 和 [A3 PDF](5115233.pdf)，用于参考。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a sample workbook and add some data inside the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("P30").putValue("This is sample data.");

// Save the workbook in memory stream
const ms = workbook.saveToStream();

// Now load the workbook from memory stream with A5 paper size
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA5);
let workbookA5 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA5.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a5_out.pdf"));

// Now load the workbook again from memory stream with A3 paper size
ms.position = 0;
opts.setPaperSize(AsposeCells.PaperSizeType.PaperA3);
let workbookA3 = new AsposeCells.Workbook(ms, opts);

// Save the workbook in pdf format
workbookA3.save(path.join(dataDir, "LoadWorkbookWithPrinterSize-a3_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
