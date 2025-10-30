---
title: Implementar etiquetas de subtotal o total general en otros idiomas con C++
linktitle: Implementar etiquetas de subtotal o total general en otros idiomas
type: docs
weight: 50
url: /es/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Aprende cómo implementar etiquetas de subtotal y total general en idiomas que no sean inglés usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, quieres mostrar etiquetas de subtotal y total general en idiomas no inglés como chino, japonés, árabe, hindi, etc. Aspose.Cells te permite hacer esto usando la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) y la propiedad [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Por favor, consulta este artículo sobre cómo usar la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/):

- [Usando la Clase GlobalizationSettings para Etiquetas de Subtotal Personalizadas y Otra Etiqueta de Gráfico de Sectores](/cells/es/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementar etiquetas de subtotal o total general en otros idiomas**

El siguiente código de ejemplo carga el archivo de Excel de ejemplo [archivo de muestra](5115151.xlsx) e implementa nombres de subtotal y total general en chino. Por favor, revisa el [archivo de Excel de salida](5115152.xlsx) generado por este código para tu referencia. Primero creamos una clase de [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) y luego la usamos en nuestro código.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

Ahora usa la clase creada anteriormente en el código como se muestra abajo:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
