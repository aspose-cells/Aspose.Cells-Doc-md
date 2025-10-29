---
title: 使用C++打印和预览工作簿
linktitle: 打印和预览
type: docs
weight: 70
url: /zh/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells支持在没有Microsoft Excel安装的情况下，使用C++打印和预览Excel文件。
---

{{% alert color="primary" %}}

创建工作表后，通常希望打印它的实体副本。本文介绍如何使用Aspose.Cells打印电子表格

{{% /alert %}}

## **打印简介**

Microsoft Excel假定您想打印整个工作表区域，除非您指定了选择区域。要使用Aspose.Cells进行打印，首先将Aspose.Cells.Rendering命名空间导入到程序中。它有几个有用的类，例如[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)和[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)


## **打印预览**

可能有一些情况下，需要将数百万页的Excel文件转换为PDF或图像。处理这些文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换这样的文件之前，用户可以检查总页数，然后决定是否转换文件。本文侧重于使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类来查找总页数。

Aspose.Cells提供打印预览功能。为此，API提供[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类。要创建整个工作簿的打印预览，通过向构造函数传递[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)对象创建[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)类的实例。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)类提供了一个[**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/)方法，返回生成预览中的页数。类似于[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)类，[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类用于为特定工作表生成打印预览。要创建工作表的打印预览，通过向构造函数传递[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)对象创建[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类的实例。[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类还提供一个[**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/)方法，返回生成预览的页数。

以下代码片段演示了通过使用示例Excel文件（94896177.xlsx）使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/)类。

### **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

执行上述示例代码生成的输出如下。

### **控制台输出**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **高级主题**
- [为呈现电子表的字体进行配置](/cells/zh/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [将工作表转换为图像-去除数据周围的空白](/cells/zh/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [将工作表转为图像以及按页面转为图像](/cells/zh/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [使用ImageOrPrint Options将工作表转换为图像](/cells/zh/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [导出工作表中的单元格范围为图像](/cells/zh/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [使用ImageOrPrintOptions从工作表中提取图像](/cells/zh/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [生成工作表的缩略图](/cells/zh/cpp/generate-thumbnail-of-the-worksheet/)
- [当没有要打印的内容时输出空白页](/cells/zh/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [页面设置和打印选项](/cells/zh/cpp/page-setup-and-printing-options/)
- [使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列](/cells/zh/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [将工作表渲染到图形上下文](/cells/zh/cpp/render-worksheet-to-graphic-context/)
- [指定工作簿渲染的个体或私有字体集](/cells/zh/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
{{< app/cells/assistant language="cpp" >}}
