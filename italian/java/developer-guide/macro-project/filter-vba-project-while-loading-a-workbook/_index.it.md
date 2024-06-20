---
title: Filtra il progetto VBA durante il caricamento di un cartella di lavoro
type: docs
weight: 70
url: /it/java/filter-vba-project-while-loading-a-workbook/
---

## **Possibili Scenari di Utilizzo**
Alcuni file .xlsm/.xslb hanno un numero estremamente grande di macro (o macro molto, molto lunghe). Aspose.Cells caricherà incondizionatamente questi dati (meta) quando si aprono tali cartelle di lavoro. Potrebbe essere necessario controllare questo utilizzando LoadDataFilterOptions, quando si ha davvero solo bisogno di estrarre i nomi dei fogli per un gran numero di cartelle di lavoro, saltando contenuti non necessari. Questo filtro è fornito introducendo la nuova opzione LoadDataFilterOptions.VBA.
## **Codice di Esempio**
Il seguente codice di esempio carica una cartella di lavoro in modo che venga filtrato solo il VBA. Il file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Imposta le opzioni di caricamento, non vogliamo caricare il VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Crea un oggetto cartella di lavoro dal file Excel di esempio utilizzando le opzioni di caricamento
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Salva l'output in formato pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
