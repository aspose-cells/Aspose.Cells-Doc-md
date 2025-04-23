---
title: カスタム数値小数点およびグループセパレータをワークブックに指定（C++使用時）
linktitle: カスタムの小数点と桁区切りセパレーターを指定する
type: docs
weight: 110
url: /ja/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: MS ExcelおよびC++コードで、Aspose.Cells for C++ APIを使用して数値の小数点と桁区切りセパレーターを変更します。
keywords: Excelでカスタム小数点セパレーターを指定、C++でのExcelカスタム小数点セパレーター指定、Excelのカスタム桁区切りセパレーター指定、C++でのExcelカスタム桁区切りセパレーター指定、Excelの小数点と桁区切りセパレーターをカスタマイズ、C++でのExcelの小数点と桁区切りセパレーターの変更、Excelの小数点と桁区切りセパレーターの変更、Excelの小数点セパレーターの変更、C++でのExcelの小数点セパレーターの変更、Excelの桁区切りセパレーターの変更、C++でのExcelの桁区切りセパレーターの変更
---

{{% alert color="primary" %}}

Microsoft Excelでは、**その他のExcelオプション** から **詳細設定** を使用せずに、カスタムの小数点および千の区切り記号を指定できます。次のスクリーンショットでは、その手順が示されています。

Aspose.Cellsは、数値のフォーマット/解析のためにカスタムセパレータを設定するための[**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/)と[**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/)プロパティを提供します。

{{% /alert %}}

## **Microsoft Excelを使用してカスタムセパレータを指定する**

次のスクリーンショットは、**詳細設定** タブを示し、**カスタムセパレータ** を指定するセクションを強調しています。

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cellsを使用してカスタムセパレータを指定する**

次のサンプルコードは、Aspose.Cells APIを使用してカスタムセパレータを指定する方法を示しています。これにより、カスタム数値の10進セパレータとグループセパレータを、それぞれドットとスペースに設定します。

### C++コードでカスタムの小数点と桁区切りセパレーターを指定する

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

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
