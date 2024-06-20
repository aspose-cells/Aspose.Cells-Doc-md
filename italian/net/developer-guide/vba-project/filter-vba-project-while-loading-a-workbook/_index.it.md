---
title: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/net/filter-vba-project-while-loading-a-workbook/
---

## **Filtra il progetto VBA durante il caricamento di un documento di lavoro Excel in C#**

Alcuni file .xlsm/.xslb hanno un numero estremamente elevato di macro (o macro molto lunghi). Aspose.Cells caricherà incondizionatamente questi metadati quando si aprono tali documenti. Potresti avere bisogno di controllare ciò attraverso [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) quando hai davvero bisogno solo di estrarre i nomi dei fogli per un gran numero di documenti, quindi saltando su tali contenuti non necessari. Questo filtro è fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
