---
title: Filtra il progetto VBA durante il caricamento di una cartella di lavoro
type: docs
weight: 70
url: /it/java/filter-vba-project-while-loading-a-workbook/
---
## **Possibili scenari di utilizzo**
Alcuni file .xlsm/.xslb hanno una quantità estremamente grande di macro (o macro molto, molto lunghe). Aspose.Cells caricherà incondizionatamente questi (meta) dati all'apertura di tali cartelle di lavoro. Potrebbe essere necessario controllarlo tramite LoadDataFilterOptions, quando in realtà è necessario estrarre solo i nomi dei fogli per un numero elevato di cartelle di lavoro, saltando così tali contenuti non necessari. Questo filtro viene fornito introducendo la nuova opzione LoadDataFilterOptions.VBA.
## **Codice d'esempio**
Il codice di esempio seguente carica una cartella di lavoro in modo che venga filtrato solo VBA. Il file di esempio per testare questa funzione può essere scaricato dal seguente link:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Imposta le opzioni di caricamento, non vogliamo caricare VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Crea un oggetto cartella di lavoro da un file excel di esempio utilizzando le opzioni di caricamento
Libro della cartella di lavoro = nuova cartella di lavoro (srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Salva l'output in formato pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
