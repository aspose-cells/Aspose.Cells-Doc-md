---
title: 在将数据导入工作表时通过C++指定公式字段
linktitle: 在导入数据到工作表时指定公式字段
type: docs
weight: 300
url: /zh/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: 通过Aspose.Cells for C++ API学习如何在导入数据到工作表时指定公式字段。
keywords: 在导入数据到工作表时指定公式字段，添加数据到工作表时设置公式字段
---

## **可能的使用场景**

您可以使用[**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/)在导入数据到工作表时指定公式字段。此属性接受布尔数组，其中值true表示该字段是公式字段。例如，如果第三个字段是公式字段，则数组中的第三个值将为true。

## **在工作表导入数据时指定公式字段**

请参阅以下示例代码，说明了如何在导入数据到工作表时指定公式字段。请参阅代码生成的输出Excel文件(61767838.xlsx)和显示代码对输出Excel文件的影响的屏幕截图。

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **示例代码**

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
{{< app/cells/assistant language="cpp" >}}
