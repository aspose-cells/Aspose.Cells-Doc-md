---
title: Filtra il progetto VBA durante il caricamento di una cartella di lavoro
type: docs
weight: 140
url: /it/net/filter-vba-project-while-loading-a-workbook/
---
## **Filtra il progetto VBA durante il caricamento di una cartella di lavoro di Excel in C#**

Alcuni file .xlsm/.xslb contengono una quantità estremamente elevata di macro (o macro molto, molto lunghe). Aspose.Cells caricherà incondizionatamente questi (meta) dati all'apertura di tali cartelle di lavoro. Tuttavia, potrebbe essere necessario controllarlo[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) quando hai davvero solo bisogno di estrarre i nomi dei fogli per un gran numero di cartelle di lavoro saltando così tali contenuti non necessari. Questo filtro viene fornito introducendo una nuova opzione,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Codice d'esempio**

Il codice di esempio seguente carica una cartella di lavoro in modo che venga filtrato solo VBA. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
