---
title: Ange formelfält vid import av data till arbetsblad med C++
linktitle: Ange formelfält vid import av data till kalkylbladet
type: docs
weight: 300
url: /sv/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Lär dig hur du specificerar formelfält vid import av data till arbetsblad via API n Aspose.Cells for C++.
keywords: Specificera formelfält vid import av data till kalkylblad, Ange formelfält när du lägger till data till kalkylbladet
---

## **Möjliga användningsscenario**

Du kan ange formelfält när du importerar data till ditt kalkylblad med hjälp av [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). Denna egenskap tar emot en boolesk array där värdet 'true' betyder att fältet är ett formelfält. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje värdet i arrayen att vara 'true'.

## **Ange formelfält vid import av data till kalkylbladet**

Vänligen se följande exempelkod som förklarar hur man specificerar formelfält vid import av data till ett kalkylblad. Se [utdata Excel-filen](61767838.xlsx) som genereras av koden och skärmdumpen som visar effekten av koden på utdatan från Excel-filen.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

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
