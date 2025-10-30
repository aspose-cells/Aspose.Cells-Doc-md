---
title: Einstellen des Formelberechnungsmodus der Arbeitsmappe mit C++
linktitle: Einstellen des Formelberechnungsmodus der Arbeitsmappe
description: Dieser Artikel erklärt, wie man mit Aspose.Cells in C++ den Formelberechnungsmodus einer Arbeitsmappe in Microsoft Excel einstellt. Durch das Laden einer existierenden Excel Datei oder das Erstellen einer neuen Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formelberechnungsmodus festzulegen und das Ergebnis zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Arbeitsmappe, Formelberechnungsmodus, Einstellungen, C++
type: docs
weight: 110
url: /de/cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}

Microsoft Excel ermöglicht es Ihnen, den Formelberechnungsmodus festzulegen, d.h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch - Neu berechnen, wenn sich etwas ändert, und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch mit Ausnahme von Datentabellen - Neu berechnen, wenn sich etwas ändert, aber Auslassen von Datentabellen.
- Manuell - Nur neu berechnen, wenn der Benutzer dies explizit durch Drücken von F9 oder STRG+ALT+F9 anfordert oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}}

Um den Formelberechnungsmodus in Microsoft Excel festzulegen:

1. Wählen Sie **Formeln** und dann **Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

Aspose.Cells ermöglicht Ihnen auch, den **Formelberechnungsmodus** mit Hilfe des [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getcalculationmode/)-Modus-Attributs festzulegen. Sie können ihm die [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/)-Enumeration zuweisen, die einen der folgenden Werte hat:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manuell

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
{{< app/cells/assistant language="cpp" >}}
