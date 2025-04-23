---
title: C++でMicrosoft ExcelのOLEオブジェクトを自動的に更新する
linktitle: 自動的にOLEオブジェクトを更新
type: docs
weight: 270
url: /ja/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aspose.Cellsを使用してC++でMicrosoft ExcelのOLEオブジェクトを自動的に更新する方法を学ぶ。
---

{{% alert color="primary" %}}

Aspose.Cellsは、Microsoft ExcelでExcelファイルを開いたときにOLEオブジェクトを更新する [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) プロパティを提供します。これにより、OLEオブジェクトはMicrosoft Excelが生成した正しいOLE画像を表示します。

{{% /alert %}}

次のサンプルコードは、非実際のOLE画像を持つ [サンプルExcelファイル](5115231.xlsx) をロードします。OLEオブジェクトは実際にはMicrosoft Wordドキュメントですが、サンプルExcelファイルではMicrosoft Wordの画像の代わりに動物の画像を表示しています。ただし、[出力Excelファイル](5115225.xlsx)を開くと、Microsoft Excelが正しいOLE画像を表示しているのが確認できます。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
