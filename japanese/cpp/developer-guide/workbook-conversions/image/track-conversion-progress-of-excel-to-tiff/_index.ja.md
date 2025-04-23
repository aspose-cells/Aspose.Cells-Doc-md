---
title: C++を使用してExcelのTIFF変換進捗を追跡
linktitle: ExcelからTIFFへの変換の進行状況を追跡
type: docs
weight: 190
url: /ja/cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for C++を使用してExcelファイルのTIFFへの変換進捗を追跡する方法を学びます。
---

## **可能な使用シナリオ**

大きなExcelファイルの変換には時間がかかる場合があります。その間、読み込み画面だけでなくドキュメント変換の進行状況を表示したい場合があります。Aspose.Cellsは[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースを提供することでドキュメント変換の進捗追跡をサポートしています。[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースは[**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/)および[**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/)メソッドを提供しており、カスタムクラスに実装可能です。また、どのページをレンダリングするかも制御可能です（*TestPageSavingCallback*カスタムクラス参照）。

## **ExcelからTIFFへの変換の進行状況を追跡**

次のコード例は、[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースを実装した*TestPageSavingCallback*カスタムクラスを使用して、[ソースExcelファイル](95584311.xlsx)を読み込み、その変換進捗をコンソールに出力します。生成された出力ファイルも添付します。

[Output File](95584312.tiff)

## **サンプルコード**

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

以下は*TestTiffPageSavingCallback* カスタムクラスのコードです。

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

## **コンソール出力**

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
