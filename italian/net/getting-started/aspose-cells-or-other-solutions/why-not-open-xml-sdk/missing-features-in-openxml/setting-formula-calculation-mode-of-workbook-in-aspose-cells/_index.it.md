---
title: Impostazione della modalità di calcolo della formula della cartella di lavoro in Aspose.Cells
type: docs
weight: 100
url: /it/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel consente di impostare la modalità di calcolo delle formule, ovvero il modo in cui vengono calcolate le formule. Ci sono tre possibili valori:

- Automatico: ricalcola ogni volta che qualcosa viene modificato e ogni volta che viene aperta una cartella di lavoro.
- Automatico ad eccezione delle tabelle di dati: ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle di dati.
- Manuale: ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9 o quando la cartella di lavoro viene salvata.

{{% /alert %}} 

Per impostare la modalità di calcolo della formula in Microsoft Excel:

1.  Selezionare**Formule** e poi**Opzioni di calcolo**.
1. Seleziona una delle opzioni.

 Aspose.Cells permette anche di impostare il**Modalità di calcolo della formula** utilizzando la proprietà della modalità FormulaSettings.CalculationMode. Puoi assegnargli l'enumerazione CalcModeType che ha uno dei seguenti valori:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

Il codice di esempio seguente crea innanzitutto una cartella di lavoro, quindi imposta la modalità di calcolo della formula su**Manuale** e salva la cartella di lavoro come file Excel di output su disco.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Scarica l'esempio di esecuzione**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
