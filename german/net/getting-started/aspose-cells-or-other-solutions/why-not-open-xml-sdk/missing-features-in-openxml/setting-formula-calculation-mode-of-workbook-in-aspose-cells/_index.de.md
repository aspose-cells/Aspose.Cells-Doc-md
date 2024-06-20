---
title: Berechnungsmodus der Formel in der Arbeitsmappe in Aspose.Cells einstellen
type: docs
weight: 100
url: /de/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
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

Aspose.Cells ermöglicht es Ihnen auch, den **Berechnungsmodus der Formel** mithilfe der FormulaSettings.CalculationMode- Eigenschaft festzulegen. Sie können ihm die CalcModeType-Aufzählung zuweisen, die einen der folgenden Werte enthält:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Der folgende Beispielcode erstellt zunächst eine Arbeitsmappe, setzt dann den Formelberechnungsmodus auf **Manuell** und speichert die Arbeitsmappe als Ausgabedatei auf der Festplatte.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Laufendes Beispiel herunterladen**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
