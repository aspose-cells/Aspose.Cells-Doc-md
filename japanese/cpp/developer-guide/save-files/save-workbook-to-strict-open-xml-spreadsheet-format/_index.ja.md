---
title: Aspose.Cells for C++を使用してワークブックをStrict Open XML Spreadsheet形式で保存する方法を学びます。
linktitle: 厳密なOpen XMLスプレッドシート形式へのブックの保存
type: docs
weight: 150
url: /ja/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Aspose.Cells for C++を使用してワークブックをStrict Open XMLスプレッドシート形式で保存する方法を学びます。
---

## **可能な使用シナリオ**

以下のサンプルコードは、ワークブックを作成し、[**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/)プロパティの値を[**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)に設定して[出力Excelファイル](67338272.xlsx)として保存します。Microsoft Excelで出力ファイルを開き、「名前を付けて保存...」ダイアログを開くと、そのフォーマットが*Strict Open XML Spreadsheet*として表示されます。

## **ストリクトなOpen XMLスプレッドシート形式でワークブックを保存**

次のサンプルコードは、Workbookを作成し、[**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcompliance/)プロパティの値を[**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/)に設定して、[出力Excelファイル](67338272.xlsx)として保存します。Microsoft Excelで出力されたExcelファイルを開き、「名前を付けて保存...」ダイアログを開くと、その形式が*Strict Open XML Spreadsheet*として表示されることがこのスクリーンショットに示されています。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Specify - Strict Open XML Spreadsheet - Format
    wb.GetSettings().SetCompliance(OoxmlCompliance::Iso29500_2008_Strict);

    // Add message in cell B4 of first worksheet
    Cell b4 = wb.GetWorksheets().Get(0).GetCells().Get(u"B4");
    b4.PutValue(u"This Excel file has Strict Open XML Spreadsheet format.");

    // Save to output Excel file
    wb.Save(u"outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with Strict Open XML Spreadsheet format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
