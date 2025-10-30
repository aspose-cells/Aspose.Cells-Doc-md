---
title: C++を用いたドキュメント変換進捗の追跡
linktitle: ドキュメント変換の進行状況を追跡
type: docs
weight: 970
url: /ja/cpp/track-document-conversion-progress/
description: Aspose.Cellsを使ってC++でドキュメント変換の進行状況を追跡し、アプリケーションの使いやすさを向上させる方法を学びます。
---

## **可能な使用シナリオ**

大きなExcelファイルの変換には時間がかかる場合があります。その間、ロード画面だけでなく、ドキュメント変換の進行状況を表示することで、アプリケーションの使いやすさを向上させることが可能です。Aspose.Cellsは、[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースを提供することで、ドキュメント変換の進行状況を追跡します。[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースは、[**PageStartSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pagestartsaving/)と[**PageEndSaving**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/pageendsaving/)のメソッドを含み、カスタムクラスに実装できます。また、どのページをレンダリングするかも制御できます。これは、`TestPageSavingCallback`カスタムクラスで示されています。

## **文書変換の進行状況を追跡する**

以下のコード例では、[ソースExcelファイル](94896151.xlsx)を読み込み、`TestPageSavingCallback`カスタムクラスを使って変換進捗状況をコンソールに表示します。このクラスは[**IPageSavingCallback**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/ipagesavingcallback/)インターフェースを実装しています。

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " is starting to save." << std::endl;
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "Page " << args.GetPageIndex() + 1 << " has been saved." << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"PagesBook1.xlsx";
    U16String outputFilePath = outDir + u"DocumentConversionProgress.pdf";

    Workbook workbook(inputFilePath);
    PdfSaveOptions pdfSaveOptions;

    TestPageSavingCallback callback;
    pdfSaveOptions.SetPageSavingCallback(&callback);

    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Document conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

以下は、`TestPageSavingCallback`カスタムクラスのコード例です。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

class TestPageSavingCallback : public IPageSavingCallback
{
public:
    void PageStartSaving(PageStartSavingArgs& args) override
    {
        std::cout << "Start saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() < 2)
        {
            args.SetIsToOutput(false);
        }
    }

    void PageEndSaving(PageEndSavingArgs& args) override
    {
        std::cout << "End saving page index " << args.GetPageIndex() 
                  << " of pages " << args.GetPageCount() << std::endl;

        if (args.GetPageIndex() >= 8)
        {
            args.SetHasMorePages(false);
        }
    }
};
```

## **コンソール出力**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
