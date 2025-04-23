---
title: Beim Importieren von Daten in Arbeitsblatt mit C++ Formularfelder angeben
linktitle: Formelfelder beim Importieren von Daten in das Arbeitsblatt angeben
type: docs
weight: 300
url: /de/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Lernen Sie, wie Sie Formel Felder beim Importieren von Daten in das Arbeitsblatt durch die API Aspose.Cells for C++ festlegen.
keywords: Formelfelder beim Importieren von Daten in das Arbeitsblatt angeben, Formelfelder festlegen beim Hinzufügen von Daten zum Arbeitsblatt
---

## **Mögliche Verwendungsszenarien**

Beim Importieren von Daten in Ihr Arbeitsblatt können Sie mit dem [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/) Formelfelder angeben. Diese Eigenschaft nimmt das Boolsche Array an, wobei der Wert **true** bedeutet, dass das Feld ein Formelfeld ist. Wenn beispielsweise das dritte Feld ein Formelfeld ist, wird der dritte Wert im Array **true** sein.

## **Formelfelder beim Import von Daten in ein Arbeitsblatt angeben**

Bitte sehen Sie sich den folgenden Beispielcode an, der erklärt, wie Sie das Formelfeld beim Importieren von Daten in ein Arbeitsblatt angeben. Bitte sehen Sie sich die [Ausgabedatei Excel](61767838.xlsx) an, die vom Code generiert wurde, sowie den Screenshot, der die Auswirkung des Codes auf die Ausgabedatei Excel zeigt.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Beispielcode**

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
