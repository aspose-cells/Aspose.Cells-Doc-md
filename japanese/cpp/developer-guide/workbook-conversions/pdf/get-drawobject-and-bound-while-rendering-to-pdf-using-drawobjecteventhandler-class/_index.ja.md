---
title: DrawObjectEventHandlerクラスを使用して、PDFへのレンダリング中にDrawObjectとBoundを取得する方法
linktitle: PDFへのレンダリング中にDrawObjectとBoundを取得する
type: docs
weight: 70
url: /ja/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
description: C++でDrawObjectEventHandlerクラスを使用して、ExcelファイルをPDFや画像にレンダリング中のDrawObjectとBoundを取得する方法について学びます。
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)抽象クラスを提供しており、[**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/)メソッドがあります。ユーザーは[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)を実装し、ExcelをPDFや画像にレンダリングする際に[**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/)メソッドを利用して[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)とバウンドを取得できます。以下に、[**Draw()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/draw/)メソッドのパラメータの簡単な説明を示します。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)は初期化され、レンダリング時に返されます

- x: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) の左端

- y: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) の上端

- width: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) の幅

- height: [**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/) の高さ

ExcelファイルをPDFにレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)クラスと[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)を利用できます。同様に、Excelファイルを画像にレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)クラスと[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobjecteventhandler/)を利用できます。

## **DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject と Bound を取得**

以下のサンプルコードを参照してください。これにより、サンプルExcelファイル（64716821.xlsx）を読み込み、[出力PDF](64716822.pdf)として保存します。PDFにレンダリングする際、[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) プロパティを使用し、既存のセルや画像などのオブジェクトの[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)とBoundをキャプチャします。[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)タイプがセルの場合、そのBoundとStringValueを表示します。[**DrawObject**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/drawobject/)タイプが画像の場合、そのBoundとShape名を表示します。詳しくは以下のコンソール出力例をご確認ください。

## **サンプルコード**

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

## **コンソール出力**

{{< highlight java >}}

[X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
