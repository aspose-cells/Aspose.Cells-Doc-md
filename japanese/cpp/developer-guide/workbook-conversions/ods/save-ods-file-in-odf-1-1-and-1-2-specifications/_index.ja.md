---
title: C++を使用してODF 1.1、1.2、1.3仕様でODSファイルを保存します。
linktitle: ODF 1.1、1.2、および1.3として保存
description: Aspose.Cellsを使用してC++でExcelをODF 1.1、1.2、1.3仕様に変換します。
type: docs
weight: 230
url: /ja/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cellsは、ODSファイル（**OpenDocument Spreadsheet**）をODF（**OpenDocument Format**）1.1、1.2、1.3仕様で保存することをサポートしています。Aspose.Cellsには[**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/)プロパティがあり、ODSファイルの保存時に使用するODFバージョンを指定します。このプロパティのデフォルト値は[**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)であり、この設定なしで保存されたODSファイルは1.2仕様を使用します。

{{% /alert %}}

以下のサンプルコードは、ワークブックオブジェクトを作成し、最初のワークシートのセルA1に値を追加し、その後ODF 1.1、1.2、1.3仕様でODSファイルを保存する例です。デフォルトでは、ODSファイルはODF 1.2仕様で保存されます。

```cpp
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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
