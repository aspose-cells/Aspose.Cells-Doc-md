---
title: シートから画像を抽出（ImageOrPrintOptions を使用、C++）
linktitle: ワークシートから画像を抽出
type: docs
weight: 140
url: /ja/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Excelワークシートから画像を抽出し、ローカルドライブに保存する方法をAspose.Cells for C++を使って学びます。
---

{{% alert color="primary" %}} 

Microsoft Excelユーザーは、スプレッドシートに画像を追加できます。Aspose.Cellsを使用すると、Microsoft Excelファイルから画像を読み込んでローカルドライブに保存することができます。この記事では、その方法を紹介します。

{{% /alert %}} 

以下のサンプルコードは、Excelファイルから画像を抽出して保存する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
