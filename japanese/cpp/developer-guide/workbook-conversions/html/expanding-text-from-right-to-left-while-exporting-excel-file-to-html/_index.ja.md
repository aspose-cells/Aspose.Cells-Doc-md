---
title: C++によるExcelファイルのHTMLエクスポート時に右から左へのテキスト展開を行う方法
linktitle: Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開
type: docs
weight: 60
url: /ja/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Aspose.Cells for C++を使用して、ExcelファイルのHTMLエクスポート時に右から左へのテキスト展開を行う方法を学びます。
---

{{% alert color="primary" %}} 

Aspose.Cells for C++は、ExcelファイルのHTMLエクスポート時に右から左へのテキスト展開をサポートしています。この機能はv8.9.0.0以降に実装されました。ソースExcelファイルに右から左に展開するテキストが含まれている場合、Aspose.Cellsは正しくHTMLにエクスポートします。

{{% /alert %}} 

## **Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開**

次のサンプルコードは [サンプルExcelファイル](5115502.xlsx) をHTMLに変換する例です。このスクリーンショットは、Microsoft Excel 2013でのファイルの見た目を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは [古いバージョンで生成された出力HTML](5115509) を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは [新しいバージョンで生成された出力HTML](5115508) を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットからわかるように、新しいバージョンはMicrosoft Excelと同様に、右揃えのテキストを左に正しく展開します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
