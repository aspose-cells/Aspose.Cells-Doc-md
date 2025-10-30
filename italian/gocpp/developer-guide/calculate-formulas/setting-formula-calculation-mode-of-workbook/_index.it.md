---
title: Impostare la modalità di calcolo delle formule del workbook con Golang tramite C++
linktitle: Impostazione della modalità di calcolo delle formule di Workbook
description: Questo articolo presenta come impostare la modalità di calcolo delle formule di un workbook in Microsoft Excel con la libreria Aspose.Cells usando C++. Caricando un file Excel esistente o creando uno nuovo, possiamo usare il metodo fornito da Aspose.Cells per impostare la modalità di calcolo delle formule e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, libro di lavoro, modalità di calcolo delle formule, impostazioni, C++
type: docs
weight: 110
url: /it/go-cpp/setting-formula-calculation-mode-of-workbook/
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

Aspose.Cells consente anche di impostare la **Modalità di Calcolo della Formula** utilizzando la proprietà di modalità [**FormulaSettings.GetCalculationMode()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getcalculationmode/). Puoi assegnare all'enumerazione [**CalcModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/calcmodetype/) che ha uno dei seguenti valori:

- CalcModeType::Automatic
- CalcModeType::AutomaticExceptTable
- CalcModeType::Manual

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaCalculationModeOfWorkbook.go" >}}
