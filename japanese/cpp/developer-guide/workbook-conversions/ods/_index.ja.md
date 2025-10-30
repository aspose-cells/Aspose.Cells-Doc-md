---
title: Excelワークブックを Ods、Sxc、Fods（OpenOffice / LibreOffice calc）に変換（C++を使用）
linktitle: Ods
type: docs
weight: 20
url: /ja/cpp/convert-excel-to-ods/
description: Aspose.Cellsを使用してExcelをOds（OpenOffice / LibreOffice Calc）に変換したり、OdsをExcelに変換したりする方法。
---

## **OpenDocumentについて**
[OpenDocument format（ODF）](https://en.wikipedia.org/wiki/OpenDocument)は、SunによってOpen Officeスイート向けに開発された電子オフィス文書のための無料かつオープンなファイルフォーマットです。OpenDocument Spreadsheet（ODS）はExcel文書のファイルフォーマットです。OpenDocumentは現在、OASISとISOの標準です。

## **Ods（OpenOffice / LibreOffice calc）をExcelに変換する**
Aspose.Cellsは、OpenOffice / LibreOffice CalcでサポートされているOds、Sxc、Fodsを読み込み、それらをExcelファイルに変換することをサポートしています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source ods file
    U16String odsFilePath(u"book1.ods");
    std::shared_ptr<Workbook> workbook = std::make_shared<Workbook>(odsFilePath);

    // Save as xlsx file
    U16String xlsxOutputPath(u"ods_out.xlsx");
    workbook->Save(xlsxOutputPath);

    // Load your source sxc file
    U16String sxcFilePath(u"book1.sxc");
    workbook = std::make_shared<Workbook>(sxcFilePath);

    // Save as xls file
    U16String xlsOutputPath(u"sxc_out.xls");
    workbook->Save(xlsOutputPath);

    // Load your source fods file
    U16String fodsFilePath(u"book1.fods");
    workbook = std::make_shared<Workbook>(fodsFilePath);

    // Save as xlsb file
    U16String xlsbOutputPath(u"fods_out.xlsb");
    workbook->Save(xlsbOutputPath);

    std::cout << "Files converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **ExcelをOds（OpenOffice / LibreOffice Calc）に変換する**
Aspose.Cellsは、ExcelファイルをOds、Sxc、Fodsに変換するサポートを提供します。以下のコード例は、[テンプレート](book1.xlsx)をOds、Sxc、Fodsファイルに変換する方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file 
    workbook.Save(u"Out.ods");

    // Save as sxc file 
    workbook.Save(u"Out.sxc");

    // Save as fods file 
    workbook.Save(u"Out.fods");

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [ODF 1.1および1.2仕様でODSファイルを保存する](/cells/ja/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [ODSファイルで背景を操作する](/cells/ja/cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="cpp" >}}
