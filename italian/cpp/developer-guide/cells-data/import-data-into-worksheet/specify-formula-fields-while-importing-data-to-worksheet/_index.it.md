---
title: Specifica i campi formula durante l importazione dei dati nel foglio di lavoro con C++
linktitle: Specificare i campi della formula durante l importazione dei dati nel foglio di lavoro
type: docs
weight: 300
url: /it/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Impara come specificare i campi formula durante l importazione dei dati nel foglio di lavoro attraverso l API Aspose.Cells for C++.
keywords: Specificare campi di formula durante l importazione dei dati nel foglio di lavoro, Imposta campi di formula durante l aggiunta di dati al foglio di lavoro
---

## **Possibili Scenari di Utilizzo**

È possibile specificare i campi di formula quando si importano dati nel foglio di lavoro utilizzando [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). Questa proprietà accetta un array booleano in cui il valore **true** significa che il campo è un campo di formula. Ad esempio, se il terzo campo è un campo di formula, allora il terzo valore nell'array sarà **true**.

## **Specifica i campi di formula durante l'importazione dei dati nel foglio di lavoro.**

Si prega di consultare il seguente codice di esempio che spiega come specificare il campo della formula durante l'importazione dei dati in un foglio di lavoro. Si prega di consultare il [file Excel di output](61767838.xlsx) generato dal codice e lo screenshot che mostra l'effetto del codice sul file Excel di output.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di Esempio**

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
