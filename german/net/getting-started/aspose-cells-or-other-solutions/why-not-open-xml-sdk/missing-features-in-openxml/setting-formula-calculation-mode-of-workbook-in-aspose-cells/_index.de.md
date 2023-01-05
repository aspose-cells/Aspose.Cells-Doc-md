---
title: Festlegen des Formelberechnungsmodus der Arbeitsmappe in Aspose.Cells
type: docs
weight: 100
url: /de/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Mit Excel können Sie den Formelberechnungsmodus festlegen, d. h. die Art und Weise, wie Formeln berechnet werden. Es gibt drei mögliche Werte:

- Automatisch - neu berechnen, wenn etwas geändert wird und jedes Mal, wenn eine Arbeitsmappe geöffnet wird.
- Automatisch außer für Datentabellen - neu berechnen, wenn etwas geändert wird, aber Datentabellen weglassen.
- Manuell – nur neu berechnen, wenn der Benutzer dies explizit anfordert, indem er F9 oder STRG+ALT+F9 drückt, oder wenn die Arbeitsmappe gespeichert wird.

{{% /alert %}} 

So stellen Sie den Formelberechnungsmodus in Microsoft Excel ein:

1.  Wählen**Formeln** und dann**Berechnungsoptionen**.
1. Wählen Sie eine der Optionen aus.

 Aspose.Cells können Sie auch die einstellen**Formelberechnungsmodus** Verwenden der Moduseigenschaft FormulaSettings.CalculationMode. Sie können ihm die Aufzählung CalcModeType zuweisen, die einen der folgenden Werte hat:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Der folgende Beispielcode erstellt zuerst eine Arbeitsmappe und setzt dann den Formelberechnungsmodus auf**Handbuch** und speichert die Arbeitsmappe als Excel-Ausgabedatei auf der Festplatte.

**C#**

{{< highlight "csharp" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Laufendes Beispiel herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
