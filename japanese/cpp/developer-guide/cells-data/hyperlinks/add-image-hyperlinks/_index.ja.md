---
title: 画像ハイパーリンクをC++で追加
linktitle: 画像ハイパーリンクの追加
type: docs
weight: 140
url: /ja/cpp/add-image-hyperlinks/
description: Aspose.Cells for C++ APIを通じて画像ハイパーリンクの追加方法を学びます。
keywords: 画像ハイパーリンクの追加、画像ハイパーリンクの挿入
---

{{% alert color="primary" %}} 

ハイパーリンクは、他のワークシートやウェブサイト上の情報にアクセスするのに役立ちます。Microsoft Excelでは、セル内のテキストや画像にハイパーリンクを追加できます。画像ハイパーリンクを使うと、ワークシートの移動が簡単になります。たとえば、次へ、前へのボタンや特定のサイトにリンクするロゴなどがあります。このドキュメントでは、Aspose.Cellsを使用してワークシートに画像ハイパーリンクを挿入する方法について説明します。

{{% /alert %}} 

Aspose.Cellsを使用してスプレッドシートの画像にハイパーリンクを追加する方法を示すサンプルコード

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
