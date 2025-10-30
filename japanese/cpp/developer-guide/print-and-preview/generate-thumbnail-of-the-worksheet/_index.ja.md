---
title: C++を使用したワークシートのサムネイル作成
linktitle: ワークシートのサムネイルを生成
type: docs
weight: 110
url: /ja/cpp/generate-thumbnail-of-the-worksheet/
description: Aspose.Cells for C++を使って画像としてワークシートのサムネイルを生成します。
---

{{% alert color="primary" %}} 

ワークシートからサムネイルを作成することは便利です。サムネイルは、ワークシートのプレビューを提供するためにWordドキュメントやPowerPointプレゼンテーションに貼り付けることができる小さなイメージです。それは、オリジナルのドキュメントをダウンロードするためのリンクを含むウェブページに追加することができ、その他の用途もたくさんあります。

{{% /alert %}} 

Aspose.Cells for C++はワークシートを画像ファイルに出力できるため、サムネイルの作成が容易です。以下のサンプルコードは、C++を使ってワークシートを画像ファイルに出力する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
