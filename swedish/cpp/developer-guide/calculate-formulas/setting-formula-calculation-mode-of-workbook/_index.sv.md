---
title: Ställa in formelberäkningsläge för arbetsbok med C++
linktitle: Ställa in formelberäkningsläget för arbetsboken
description: Denna artikel introducerar hur man ställer in formelberäkningsläge för en arbetsbok i Microsoft Excel med Aspose.Cells biblioteket med C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda metoden som tillhandahålls av Aspose.Cells för att ställa in formelberäkningsläget och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, arbetsbok, formelberäkningsläge, inställningar, C++
type: docs
weight: 110
url: /sv/cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel tillåter dig att ställa in formelberäkningsläget, det vill säga hur formler beräknas. Det finns tre möjliga värden:

- Automatisk - beräknas om varje gång något ändras och varje gång en arbetsbok öppnas.
- Automatisk, utom för datatabeller - beräknas om varje gång något ändras, men exkluderar datatabeller.
- Manuell - beräknas endast när användaren uttryckligen begär det genom att trycka på F9 eller CTRL+ALT+F9 eller när arbetsboken sparas.

{{% /alert %}}

För att ställa in formelberäkningsläge i Microsoft Excel:

1. Välj **Formler** och sedan **Beräkningsalternativ**.
1. Välj ett av alternativen.

Aspose.Cells tillåter också att du ställer in **Formelberäkningsläget** med hjälp av [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getcalculationmode/)-lägesegenskapen. Du kan tilldela den [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/)-uppräkningen som har ett av följande värden:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create a workbook
    Workbook workbook;

    // Set the Formula Calculation Mode to Manual
    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);

    // Save the workbook
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully with manual calculation mode!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
