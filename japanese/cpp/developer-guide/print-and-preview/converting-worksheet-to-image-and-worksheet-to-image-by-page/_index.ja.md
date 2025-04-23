---
title: ページ単位のワークシート変換と画像変換の方法（C++）
linktitle: ワークシートを画像に変換し、ページごとにワークシートを画像に変換
type: docs
weight: 80
url: /ja/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Aspose.Cellsを使用し、ワークシートを画像に変換し、複数ページのワークシートをページごとに画像化する方法について学びます。
---

{{% alert color="primary" %}}

このドキュメントは、開発者がワークシートを画像に変換し、複数ページのワークシートをページごとに画像化する方法について詳細に理解できるように設計されています。

時には、アプリケーションやWebページでワークシートを画像として表示する必要があります。たとえば、その画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があるかもしれません。単純に言えば、ワークシートを画像としてレンダリングしたいと思います。Aspose.Cellsは、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは、ワークブックを複数のページごとに1つの画像ファイルに変換することもサポートしています。

これを実現するためにOffice Automationを使用することも考えられますが、Office Automationにはいくつかの問題点もあります。理由や課題には、セキュリティ、安定性、スケーラビリティ/速度、価格、機能などさまざまです。要するに、多くの理由がありますが、主なものはMicrosoft自身がOffice Automationに強く反対していることです。

{{% /alert %}}

## **Aspose.Cellsを使用してワークシートを画像ファイルに変換する方法**

この記事では、Visual Studioでコンソールアプリケーションを作成し、Aspose.Cells APIを使用してわずか数行のコードでワークシートを画像に変換し、複数のページを持つワークシートを1つの画像に変換する方法を示します。

プログラムやプロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)名前空間を含める必要があります。これは、[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)などの有用なクラスを持っています。[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)クラスは、ワークシートの画像をレンダリングするためのもので、オーバーロードされた[**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)メソッドを備えており、任意の属性やオプションを設定してワークシートを直接画像ファイルに変換できます。これにより、`System.Drawing.Bitmap`オブジェクトを返し、画像ファイルをディスクやストリームに保存可能です。サポートされる画像フォーマットには、BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなどがあります。

この記事では以下の方法について説明します:

- ワークシートを画像に変換する
- ワークシートの各ページを画像に変換する

このタスクでは、Aspose.Cellsを使用して、テンプレートワークブックからワークシートを画像ファイルに変換する方法を示します。

### **プロジェクトのセットアップ**

1. まず、[Aspose.Cells for C++のダウンロード](https://downloads.aspose.com/cells/cpp)。
1. 開発コンピュータにインストールします。すべての [Aspose](http://www.aspose.com/) コンポーネントは、インストール時に評価モードで動作します。評価モードには時間制限はなく、生成されたドキュメントに透かしが挿入されるだけです。今すぐ Visual Studio を起動し、新しいコンソールアプリケーションを作成します。この例では C++ のコンソールアプリケーションを使用します。作成したプロジェクトに Aspose.Cells への参照を追加してください。

### **ワークシートを画像ファイルに変換**

Microsoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました：**Testbook.xlsx**（1つのワークシート）。次に、テンプレートファイルのワークシートSheet1をSheetImage.jpgという画像ファイルに変換します。

コンポーネントがタスクを達成するために使用したコードは以下の通りです。**Testbook.xlsx**のSheet1を画像ファイルに変換し、この変換がどれほど簡単であるかを説明します。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cellsを使用して、ワークシートを画像ファイルにページごとに変換する**

この例では、Aspose.Cellsを使用して、複数のページを持つテンプレートワークブックからワークシートを1つの画像ファイルに変換する方法を示します。

### **ページ単位でシートを画像に変換**

私はMicrosoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました: **Testbook2.xlsx** (1 ワークシート)。

これで、テンプレートファイルのワークシート Sheet1 を画像ファイルに変換します（1ページごとのファイル）。すでにコンソールアプリケーションを作成してコピー作業を行う準備ができているため、コンソールアプリケーションの作成手順をスキップして、直接ワークシートの変換手順に移ります。

以下は、そのタスクを実現するためにコンポーネントが使用するコードです。Testbook2.xlsxのSheet1をページごとに画像ファイルに変換します。

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
