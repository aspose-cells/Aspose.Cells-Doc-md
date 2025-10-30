---  
title: Festlegen des Formelerkennungsmodus der Arbeitsmappe mit Node.js über C++  
linktitle: Einstellen des Formelberechnungsmodus der Arbeitsmappe  
description: Dieser Artikel zeigt, wie der Formelerkennungsmodus einer Arbeitsmappe in Microsoft Excel mit Aspose.Cells for Node.js via C++ eingestellt werden kann. Durch das Laden einer vorhandenen Excel Datei oder das Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellte Methode verwenden, um den Formelerkennungsmodus festzulegen und das Ergebnis abzurufen. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.  
keywords: Aspose.Cells, Excel, Arbeitsmappe, Formelerkennungsmodus, Einstellungen, Node.js über C++  
type: docs  
weight: 110  
url: /de/nodejs-cpp/setting-formula-calculation-mode-of-workbook/  
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

Aspose.Cells for Node.js via C++ ermöglicht auch die Einstellung des **Formelerkennungsmodus** mit der Mode-Eigenschaft [**FormulaSettings.getCalculationMode()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getCalculationMode--). Sie können ihm die [**CalcModeType**](https://reference.aspose.com/cells/nodejs-cpp/calcmodetype)-Aufzählung zuweisen, die einen der folgenden Werte hat:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Set the Formula Calculation Mode to Manual
workbook.getSettings().getFormulaSettings().setCalculationMode(AsposeCells.CalcModeType.Manual);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
