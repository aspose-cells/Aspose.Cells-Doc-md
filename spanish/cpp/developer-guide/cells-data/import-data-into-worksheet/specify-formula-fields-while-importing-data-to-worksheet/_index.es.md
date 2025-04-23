---
title: Especificar Campos de Fórmula al Importar Datos a la Hoja de Trabajo con C++
linktitle: Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo
type: docs
weight: 300
url: /es/cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Aprende cómo especificar Campos de Fórmula al importar datos a la hoja mediante la API Aspose.Cells for C++.
keywords: Especificar campos de fórmula al importar datos a la hoja de cálculo, establecer campos de fórmula al agregar datos a la hoja de cálculo
---

## **Escenarios de uso posibles**

Puedes especificar campos de fórmula al importar datos en tu hoja de cálculo usando el [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/getisformulas/). Esta propiedad toma un array de booleanos donde el valor **true** significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en el array será **true**.

## **Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo**

Consulta el siguiente código de ejemplo que explica cómo especificar el campo de fórmula al importar datos a una hoja de cálculo. Consulta el [archivo de Excel de salida](61767838.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

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
