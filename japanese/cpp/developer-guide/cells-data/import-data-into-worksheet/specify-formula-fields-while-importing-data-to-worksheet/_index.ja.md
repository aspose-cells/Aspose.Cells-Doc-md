---
title: C++でデータをインポートするときに数式フィールドを指定する
linktitle: ワークシートへのデータインポート時に式フィールドを指定
type: docs
weight: 300
url: /ja/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Aspose.Cells for C++ APIを通じて、データをインポートする際に数式フィールドを指定する方法を学びます。
keywords: ワークシートにデータをインポートする際に式フィールドを指定、ワークシートにデータを追加する際に式フィールドを設定
---

## **可能な使用シナリオ**

[**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/)を使用して、ワークシートにデータをインポートする際に式フィールドを指定できます。このプロパティは、フィールドが式フィールドであるかどうかを示すブール値の配列を取ります。たとえば、3番目のフィールドが式フィールドの場合、配列内の3番目の値は**true**になります。

## **ワークシートにデータをインポートする際に式フィールドを指定する**

ワークシートにデータをインポートする際に式フィールドを指定する方法について説明する以下のサンプルコードを参照してください。コードによって生成される[出力Excelファイル](61767838.xlsx)と、コードの出力Excelファイルへの影響を示すスクリーンショットも参照してください。

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

static U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

class DataItems {
public:
    int Number1;
    int Number2;
    U16String Formula1;
    U16String Formula2;

    DataItems() : Number1(0), Number2(0) {}
};

void Run() {
    vector<DataItems> dis;

    DataItems di;
    di.Number1 = 2002;
    di.Number2 = 3502;
    di.Formula1 = u"=SUM(A2,B2)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2003;
    di.Number2 = 3503;
    di.Formula1 = u"=SUM(A3,B3)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2004;
    di.Number2 = 3504;
    di.Formula1 = u"=SUM(A4,B4)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    di = DataItems();
    di.Number1 = 2005;
    di.Number2 = 3505;
    di.Formula1 = u"=SUM(A5,B5)";
    di.Formula2 = u"=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")";
    dis.push_back(di);

    Workbook wb;
    Worksheet ws = wb.GetWorksheets().Get(0);

    for (size_t i = 0; i < dis.size(); ++i) {
        const DataItems& item = dis[i];
        int row = static_cast<int>(i);
        ws.GetCells().Get(row, 0).PutValue(item.Number1);
        ws.GetCells().Get(row, 1).PutValue(item.Number2);
        ws.GetCells().Get(row, 2).SetFormula(item.Formula1);
        ws.GetCells().Get(row, 3).SetFormula(item.Formula2);
    }

    wb.CalculateFormula();
    ws.AutoFitColumns();
    wb.Save(outputDir + u"outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx");

    cout << "SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully." << endl;
}

int main() {
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
