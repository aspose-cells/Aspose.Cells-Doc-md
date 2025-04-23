---
title: 使用 C++ 通过 Node.js 追踪 Excel 转 TIFF 的转换进度
linktitle: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 追踪 Excel 转换为 TIFF 的进度。在转换过程中提升用户体验。
---

## **可能的使用场景**

 有时候转换大型Excel文件需要一些时间。在此期间，你可能希望显示文档转换进度，而不是仅仅显示加载屏幕，以提升应用程序的易用性。Aspose.Cells for Node.js via C++ 支持通过提供 [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) 接口来跟踪文档转换过程。[**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) 接口提供 [**pageStartSaving(PageStartSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageStartSaving-pagestartsavingargs-) 和 [**pageEndSaving(PageEndSavingArgs)**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback/#pageEndSaving-pageendsavingargs-) 方法，你可以在自定义类中实现它们。你还可以控制哪些页面被渲染，方法如 *TestPageSavingCallback* 自定义类所示。

## **跟踪Excel转换为TIFF的进度**

下面的代码示例加载了[源 Excel 文件](95584311.xlsx)，并使用实现了 [**IPageSavingCallback**](https://reference.aspose.com/cells/nodejs-cpp/ipagesavingcallback) 接口的 *TestPageSavingCallback* 自定义类在控制台打印其转换进度。生成的输出文件已附上供您参考。

[Output File](95584312.tiff)

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const opts = new AsposeCells.ImageOrPrintOptions();

// Define TestTiffPageSavingCallback
class TestTiffPageSavingCallback {
// Implement required methods for the callback here
}

opts.setPageSavingCallback(new TestTiffPageSavingCallback());
opts.setImageType(AsposeCells.ImageType.Tiff);

const wr = new AsposeCells.WorkbookRender(workbook, opts);
wr.toImage(path.join(outputDir, "DocumentConversionProgressForTiff_out.tiff"));
```

以下是 *TestTiffPageSavingCallback* 自定义类的代码。

```javascript
const AsposeCells = require("aspose.cells.node");

class TestTiffPageSavingCallback {
pageStartSaving(args) {
console.log(`Start saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages before page index 2.
if (args.pageIndex < 2) {
args.setIsToOutput(false);
}
}

pageEndSaving(args) {
console.log(`End saving page index ${args.pageIndex} of pages ${args.pageCount}`);

// Don't output pages after page index 8.
if (args.pageIndex >= 8) {
args.setHasMorePages(false);
}
}
}
```

## **控制台输出**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
