---
title: ワークシートを画像に変換  データ周囲の空白を除去するC++による方法
linktitle: ワークシートを画像に変換  データ周囲の空白を除去
type: docs
weight: 40
url: /ja/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Aspose.Cells for C++を使用してワークシートを画像に変換し、空白を除去する方法について学びます。
---

{{% alert color="primary" %}}

時には、ワークシートの画像をアプリケーションやWebページで表示する必要があります。たとえば、画像をWord文書、PDFファイル、PowerPointプレゼンテーション、あるいは他のドキュメントに挿入する必要があるかもしれません。基本的に、ワークシートを画像としてレンダリングして、他のアプリケーションに貼り付けられるようにしたいと思うでしょう。Aspose.Cellsを使用すると、Microsoft Excelのワークシートを画像に変換することができます。

{{% /alert %}}

## **データ周りの余白を削除してください**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)APIは、ワークシートを指定された属性（たとえば、画像形式、ページ化されたシートなど）で画像ファイルに変換します。いくつかの画像形式がサポートされており、BMP、GIF、JPG、TIFF、EMFなどが含まれています。

シートから画像への変換機能を使用すると、出力画像にはデフォルトで周囲に空白（境界線）が含まれます。これを除去するには、ソースワークシートの上下左右のページ設定の余白を0に設定し、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)属性を適切に指定してください。

次のコードスニペットは、出力画像のデータ周りの余白を削除します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
