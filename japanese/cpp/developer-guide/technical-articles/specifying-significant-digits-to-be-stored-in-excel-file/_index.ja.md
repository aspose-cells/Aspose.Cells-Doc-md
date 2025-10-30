---
title: Excelファイルに保存される有意義な桁数を指定する（C++使用）
linktitle: 有意義な桁数の指定
type: docs
weight: 30
url: /ja/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aspose.Cells for C++を使って、Excelファイルに保存する有意義な桁数を指定する方法を学びます。
---

## **可能な使用シナリオ**

デフォルトでは、Aspose.CellsはExcelファイル内に64ビットの値の有効数字17桁を格納します。これは、MS-Excelが有効数字15桁しか格納しないのとは異なります。Aspose.Cellsの既定の動作を、[**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) プロパティを使用して15桁に変更できます。

## **Excelファイルに保存する有効桁数を指定**

以下のサンプルコードは、Aspose.CellsがExcelファイル内に64ビットの値を格納する際に15桁の有効数字を使用するように強制します。[出力Excelファイル](22774105.xlsx)を確認してください。拡張子を.zipに変更して解凍すると、Excelファイル内に15桁だけが格納されていることがわかります。以下のスクリーンショットは、[**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) プロパティが出力Excelファイルに与える影響を示しています。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **サンプルコード**

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
