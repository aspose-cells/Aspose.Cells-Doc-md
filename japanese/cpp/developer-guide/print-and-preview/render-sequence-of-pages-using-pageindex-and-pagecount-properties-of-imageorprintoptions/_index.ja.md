---
title: PageIndexとPageCountプロパティを使用してページのシーケンスをレンダリング（C++）
linktitle: ページのシーケンスをレンダリング
type: docs
weight: 110
url: /ja/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
description: Aspose.Cellsを使用してExcelファイルのページシーケンスを画像にレンダリング（C++）
---

## **可能な使用シナリオ**

Aspose.Cellsを使用してExcelファイルのページのシーケンスを[**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/)および[**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/)のプロパティを使用してイメージにレンダリングできます。これらのプロパティは、ワークシートに多数のページ（数千ページなど）がある場合でも、特定のページのみをレンダリングしたい場合に役立ちます。これにより、処理時間が節約され、レンダリングプロセスのメモリ消費量も節約されます。

## **ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする**

次のサンプルコードは、サンプルExcelファイルをロードし、[**ImageOrPrintOptions.GetPageIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpageindex/)と[**ImageOrPrintOptions.GetPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getpagecount/)のプロパティを使用してページ4、5、6、7のみをレンダリングします。こちらがコードによって生成されたレンダリングされたページです。

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **サンプルコード**

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sampleImageOrPrintOptions_PageIndexPageCount.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    ImageOrPrintOptions opts;
    opts.SetPageIndex(3);
    opts.SetPageCount(4);
    opts.SetImageType(ImageType::Png);

    SheetRender sr(ws, opts);

    for (int i = opts.GetPageIndex(); i < sr.GetPageCount(); i++)
    {
        std::wstring pageNum = std::to_wstring(i + 1);
        U16String filePath = outDir + U16String(u"outputImage-") + 
            U16String(reinterpret_cast<const char16_t*>(pageNum.c_str())) + 
            U16String(u".png");
        sr.ToImage(i, filePath);
    }

    std::cout << "Images generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
