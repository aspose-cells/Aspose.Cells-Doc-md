---
title: C++を使用した複数エンコーディングのCSVファイルの読み取り
linktitle: 複数のエンコーディングでのCSVファイルの読み込み
type: docs
weight: 200
url: /ja/cpp/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for C++を使用して、複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）を持つCSVファイルの読み取り方法を学びます。
---

{{% alert color="primary" %}}

時には、CSVファイルに複数のエンコーディング（Unicode、ANSI、UTF8、UTF7など）が含まれている場合があります。Aspose.Cellsを使えば、そのようなCSVファイルをロードして、PDFやXLSXなどの他のフォーマットに変換できます。

{{% /alert %}}

Aspose.Cellsは[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)プロパティを提供しており、これを**true**に設定する必要があります。そうすることで、複数エンコーディングのCSVファイルを正しく読み込むことができます。

以下のスクリーンショットは、2行を含むサンプルCSVファイルを示しています。最初の行は**ANSI**エンコーディングで、2行目は**Unicode**エンコーディングです。

|**入力ファイル**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

以下のスクリーンショットは、上記のCSVファイルから変換されたXLSXファイルを、[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)プロパティを**true**に設定しなかった場合を示しています。ご覧のとおり、Unicodeテキストは正しく変換されませんでした。

|**出力ファイル1: 複数のエンコーディングを考慮していない**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

以下のスクリーンショットは、[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/cpp/aspose.cells/txtloadoptions/ismultiencoded/)プロパティを**true**に設定した後の、上記のCSVファイルから変換されたXLSXファイルを示しています。ご覧のとおり、Unicodeテキストは正しく変換されています。

|**出力ファイル2: IsMultiEncodedをtrueに設定**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

以下は、上記のCSVファイルを正しくXLSX形式に変換するサンプルコードです。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input CSV file
    U16String filePath = srcDir + u"MultiEncoded.csv";

    // Create TxtLoadOptions and set MultiEncoded property to true
    TxtLoadOptions options;
    options.SetIsMultiEncoded(true);

    // Load the CSV file into Workbook with the specified options
    Workbook workbook(filePath, options);

    // Save the workbook in XLSX format
    workbook.Save(filePath + u".out.xlsx", SaveFormat::Xlsx);

    std::cout << "File converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## 関連記事

- [CSV ファイルを開く](/cells/ja/cpp/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="cpp" >}}
