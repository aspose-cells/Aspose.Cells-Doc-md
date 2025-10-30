---
title: C++でURLからWeb画像を読み込み、Excelに埋め込みます
linktitle: ExcelワークシートにURLからのWeb画像をロードする
type: docs
weight: 30
url: /ja/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: URLから画像を変換してExcelに埋め込む方法をC++とAspose.Cells for C++ APIを使用して学びます。
keywords: ExcelはURLから画像を表示します。URLから画像をExcelに挿入します。ExcelでURLから画像を表示します。ExcelにURLから画像を挿入します。URLを画像に変換します。ExcelのURLから画像を読み込みます。C++、Excel
---

## ExcelワークシートにURLからの画像をロードする

Aspose.Cells for C++ APIは、URLから画像をExcelシートに読み込む簡単な方法を提供します。この記事では、画像データをメモリストリームにダウンロードし、Aspose.Cellsを使用してワークシートに挿入する方法を説明します。画像はExcelファイルに埋め込まれ、開く際に外部ダウンロードは必要ありません。

## サンプルコード

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

常に更新される画像をURLから取得する必要がある場合は、[Webアドレスからリンクされた画像を挿入](/cells/ja/cpp/insert-a-linked-picture-from-web-address/)で説明されている方法を使用してください。この方法は、ワークシートを開くたびにURLから画像をロードします。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
