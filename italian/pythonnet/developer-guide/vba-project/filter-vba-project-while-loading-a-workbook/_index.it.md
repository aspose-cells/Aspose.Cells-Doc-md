---
title: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Filtra il progetto VBA durante il caricamento di un workbook Excel in Python**

Alcuni file .xlsm/.xslb contengono un numero estremamente elevato di macro (o macro molto, molto lunghe). Aspose.Cells per Python via .NET caricherà senza condizioni questi dati (meta) quando si aprono tali workbook. Potresti dover controllare questo tramite [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) quando hai davvero bisogno di estrarre solo i nomi dei fogli per un gran numero di workbook, saltando così contenuti non necessari. Questo filtro è fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

