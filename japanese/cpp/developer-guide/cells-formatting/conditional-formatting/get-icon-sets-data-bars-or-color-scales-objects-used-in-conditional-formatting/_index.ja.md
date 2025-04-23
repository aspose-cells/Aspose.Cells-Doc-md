---
title: 条件付き書式に使用されるアイコンセット、データバー、カラースケールオブジェクトをC++で取得
linktitle: アイコンセット、データバー、カラースケールオブジェクトの取得
description: Aspose.Cells for C++はスプレッドシートファイルを操作するためのライブラリです。条件付き書式でアイコンセット、データバー、色スケールオブジェクトを使用してスプレッドシートのデータを表示できます。この資料では、これらのオブジェクトのデータを取得する方法について説明します。
keywords: Aspose.Cells、条件付き書式、アイコンセット、データバー、カラースケール、スプレッドシート
type: docs
weight: 10
url: /ja/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

時々、セルやセル範囲の条件付き書式に使用されているアイコンセットを取得し、それに基づいて画像ファイルを作成したい場合があります。条件付き書式で使用されているデータバーやカラースケールも読む必要があるかもしれません。Aspose.Cells for C++はこの機能をサポートしています。

{{% /alert %}} 

次のコードサンプルは、条件付き書式に使用されるアイコンセットを読み取る方法を示しています。Aspose.CellsのシンプルなAPIを使用して、アイコンセットの画像データを画像として保存します。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
