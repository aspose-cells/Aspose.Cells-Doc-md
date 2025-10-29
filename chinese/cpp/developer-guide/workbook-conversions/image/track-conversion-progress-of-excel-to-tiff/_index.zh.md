---
title: 跟踪Excel转TIFF的转换进度，使用C++
linktitle: 跟踪Excel转换为TIFF的进度
type: docs
weight: 190
url: /zh/cpp/track-conversion-progress-of-excel-to-tiff/
description: 学习如何使用Aspose.Cells for C++跟踪Excel文件转换为TIFF格式的进度。
---

## **可能的使用场景**

有时转换大型Excel文件可能需要一些时间。在此期间，你可能想显示文件转换的进度，而不是仅显示加载屏幕，以增强应用程序的可用性。Aspose.Cells支持通过提供[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)接口来跟踪文档转换进度。[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)接口提供[**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/)和[**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/)方法，你可以在自定义类中实现。你也可以控制哪些页面被渲染，具体演示请参考*TestPageSavingCallback*自定义类。

## **跟踪Excel转换为TIFF的进度**

以下代码示例加载了[源Excel文件](95584311.xlsx)，并利用实现了[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)接口的*TestPageSavingCallback*自定义类在控制台打印其转换进度。生成的输出文件已附在参考资料中。

[Output File](95584312.tiff)

## **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestTiffPageSavingCallback : public IPageSavingCallback {
public:
    void PageStartSaving(PageStartSavingArgs& args) override {
        // Implement page start saving logic here
    }

    void PageEndSaving(PageEndSavingArgs& args) override {
        // Implement page end saving logic here
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    ImageOrPrintOptions opts;
    opts.SetPageSavingCallback(new TestTiffPageSavingCallback());
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Tiff);

    WorkbookRender wr(workbook, opts);
    wr.ToImage(outDir + u"DocumentConversionProgressForTiff_out.tiff");

    std::cout << "Document converted to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

以下是*TestTiffPageSavingCallback*自定义类的代码。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestTiffPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages before page index 2.
        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() << " of pages " << args.GetPageCount() << std::endl;

        // Don't output pages after page index 8.
        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
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
{{< app/cells/assistant language="cpp" >}}
