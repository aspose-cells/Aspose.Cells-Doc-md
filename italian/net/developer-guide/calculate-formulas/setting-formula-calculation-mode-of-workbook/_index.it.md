---
title: Impostazione della modalità di calcolo della formula della cartella di lavoro
description: Questo articolo illustra come impostare la modalità di calcolo della formula di una cartella di lavoro in Excel Microsoft con la libreria Aspose.Cells. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare il metodo fornito da Aspose.Cells per impostare la modalità di calcolo della formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, workbook, formula calculation mode, settings
type: docs
weight: 110
url: /it/net/setting-formula-calculation-mode-of-workbook/
---
{{% alert color="primary" %}}

Microsoft Excel consente di impostare la modalità di calcolo delle formule, ovvero il modo in cui vengono calcolate le formule. Ci sono tre valori possibili:

- Automatico: ricalcola ogni volta che viene modificato qualcosa e ogni volta che viene aperta una cartella di lavoro.
- Automatico tranne che per le tabelle dati: ricalcola ogni volta che qualcosa viene modificato, ma tralasciando le tabelle dati.
- Manuale: ricalcola solo quando l'utente lo richiede esplicitamente premendo F9 o CTRL+ALT+F9 oppure quando la cartella di lavoro viene salvata.

{{% /alert %}}

Per impostare la modalità di calcolo della formula in Microsoft Excel:

1.  Selezionare**Formule** e poi *Opzioni di calcolo**.
1. Seleziona una delle opzioni.

 Aspose.Cells permette anche di impostare il**Modalità di calcolo della formula** utilizzando[**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode) proprietà della modalità. Puoi assegnargli il[**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype)enumerazione che ha uno dei seguenti valori:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
