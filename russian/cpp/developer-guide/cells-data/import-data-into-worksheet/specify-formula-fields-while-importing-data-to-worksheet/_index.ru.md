---
title: Указать поля формул при импорте данных в рабочий лист с помощью C++
linktitle: Указание формульных полей при импорте данных в рабочий лист
type: docs
weight: 300
url: /ru/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Узнайте, как указывать поля формул при импорте данных в рабочий лист через API Aspose.Cells for C++.
keywords: Укажите формульные поля при импорте данных в рабочий лист, Установите формульные поля при добавлении данных в рабочий лист
---

## **Возможные сценарии использования**

Вы можете указать формульные поля при импорте данных в свой рабочий лист, используя [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). Это свойство принимает булевый массив, где значение **True** означает, что поле является формульным. Например, если третье поле является формульным полем, то третье значение в массиве будет **True**.

## **Указание формульных полей при импорте данных в рабочий лист**

Пожалуйста, ознакомьтесь с последующим образцом кода, который объясняет, как указать формульное поле при импорте данных в рабочий лист. Пожалуйста, ознакомьтесь с [выходным файлом Excel](61767838.xlsx), сгенерированным кодом, и скриншотом, показывающим эффект кода на выходной файл Excel.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Образец кода**

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
