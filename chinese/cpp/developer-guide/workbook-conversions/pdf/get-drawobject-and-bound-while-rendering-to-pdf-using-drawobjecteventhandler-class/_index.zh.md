---
title: 在使用DrawObjectEventHandler类在渲染为PDF时获取DrawObject和边界
linktitle: 在渲染为PDF时获取DrawObject和边界
type: docs
weight: 70
url: /zh/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: 学习如何在C++中使用DrawObjectEventHandler类捕获在将Excel文件渲染为PDF或图像时的DrawObject和边界。
---

## **可能的使用场景**

Aspose.Cells提供了一个抽象类 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)，其中有一个 [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) 方法。用户可以实现 [**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/) 并利用 [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) 方法来获取渲染Excel为PDF或图像时的 [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) 和 Bound。以下是对 [**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/) 方法参数的简要描述。

- drawObject: 在呈现时会初始化并返回 [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)

- x：[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)的左边界

- y：[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)的顶部

- width：[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)的宽度

- height：[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)的高度

如果您将Excel文件渲染为PDF，可以利用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)类结合[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)。同样，如果将Excel文件渲染为图片，也可以利用[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)类和[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)。

## **在使用DrawObjectEventHandler类呈现PDF时获取绘图对象和边界**

请查看以下示例代码。它加载了[示例Excel文件](64716821.xlsx)，并将其保存为[输出PDF](64716822.pdf)。在渲染为PDF时，使用[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性，捕获现有单元格和对象（如图片）的[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)和边界。如果[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)类型是单元格，则打印它的边界和字符串值；如果类型是图片，则打印它的边界和形状名称。请查看下面的示例代码输出以获取更多帮助。

## **示例代码**

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class ClsDrawObjectEventHandler : public DrawObjectEventHandler
{
public:
    void Draw(DrawObject& drawObject, float x, float y, float width, float height) override
    {
        std::cout << std::endl;

        if (drawObject.GetType() == DrawObjectEnum::Cell)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Cell Value]: " << drawObject.GetCell().GetStringValue().ToUtf8() << std::endl;
        }

        if (drawObject.GetType() == DrawObjectEnum::Image)
        {
            std::cout << "[X]: " << x << " [Y]: " << y << " [Width]: " << width << " [Height]: " << height 
                      << " [Shape Name]: " << drawObject.GetShape().GetName().ToUtf8() << std::endl;
        }

        std::cout << "----------------------" << std::endl;
    }
};

void Run()
{
    Workbook wb(u"sampleGetDrawObjectAndBoundUsingDrawObjectEventHandler.xlsx");
    PdfSaveOptions opts;
    auto drawObjectEventHandler = std::make_shared<ClsDrawObjectEventHandler>();
    opts.SetDrawObjectEventHandler(drawObjectEventHandler.get());
    wb.Save(u"outputGetDrawObjectAndBoundUsingDrawObjectEventHandler.pdf", opts);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
