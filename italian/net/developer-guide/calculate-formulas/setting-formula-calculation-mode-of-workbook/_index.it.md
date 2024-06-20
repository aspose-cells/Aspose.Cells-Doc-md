---
title: Impostazione della modalità di calcolo delle formule di Workbook
description: Questo articolo presenta come impostare la modalità di calcolo della formula di un libro di lavoro in Microsoft Excel con la libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per impostare la modalità di calcolo della formula e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, libro di lavoro, modalità di calcolo della formula, impostazioni
type: docs
weight: 110
url: /it/net/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells consente anche di impostare la **Modalità di Calcolo della Formula** utilizzando la proprietà di modalità [**FormulaSettings.CalculationMode**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/calculationmode). Puoi assegnare all'enumerazione [**CalcModeType**](https://reference.aspose.com/cells/net/aspose.cells/calcmodetype) che ha uno dei seguenti valori:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingFormulaCalculationModeWorkbook-1.cs" >}}
