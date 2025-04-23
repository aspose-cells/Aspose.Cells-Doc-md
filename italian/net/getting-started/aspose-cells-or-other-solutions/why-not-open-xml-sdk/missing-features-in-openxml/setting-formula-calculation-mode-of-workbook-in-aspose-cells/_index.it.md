---
title: Impostare la Modalità di Calcolo delle Formule del Workbook in Aspose.Cells
type: docs
weight: 100
url: /it/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

Microsoft Excel consente di impostare la modalità di calcolo delle formule, cioè il modo in cui le formule vengono calcolate. Ci sono tre possibili valori:

- Automatico - ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperto un workbook.
- Automatico tranne per le tabelle dati - ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle dati.
- Manuale - ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9, o quando il workbook viene salvato.

{{% /alert %}} 

Per impostare la modalità di calcolo delle formule in Microsoft Excel:

1. Selezionare **Formule** e quindi **Opzioni di calcolo**.
1. Seleziona una delle opzioni.

Aspose.Cells ti consente anche di impostare la **Modalità di Calcolo della Formula** utilizzando la proprietà FormulaSettings.CalculationMode. Puoi assegnare all'enumerazione CalcModeType uno dei seguenti valori:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Il seguente codice di esempio crea prima un workbook, quindi imposta la modalità di calcolo della formula su **Manuale** e salva il workbook come file Excel di output su disco.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Scarica Esempio in Esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
