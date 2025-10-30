---
title: Filtra il progetto VBA durante il caricamento di un workbook con Golang tramite C++
linktitle: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 140
url: /it/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Impara come filtrare i progetti VBA durante il caricamento di un workbook Excel usando Aspose.Cells con Golang tramite C++.
---

## **Filtra il progetto VBA durante il caricamento di un file Excel in C++**

Alcuni file .xlsm/.xslb contengono un numero estremamente elevato di macro (o macro molto, molto lunghe). Aspose.Cells caricherà incondizionatamente questi dati durante l'apertura di tali workbook. Potrebbe essere necessario controllare questo tramite [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) quando si desidera estrarre solo i nomi dei fogli da un gran numero di workbook, ignorando contenuti non necessari. Questo filtro viene fornito introducendo una nuova opzione, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Codice di Esempio**

Il seguente codice di esempio carica un documento di lavoro in modo che solo il VBA venga filtrato. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
