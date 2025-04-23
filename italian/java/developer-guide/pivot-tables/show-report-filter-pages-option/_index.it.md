---
title: Opzione Mostra pagine filtro report
type: docs
weight: 140
url: /it/java/show-report-filter-pages-option/
---

## **Mostra l'opzione pagine filtro report**

Excel supporta la creazione di tabelle pivot, l'aggiunta di filtri dei report e l'abilitazione dell'opzione "Mostra pagine filtro report". Anche Aspose.Cells supporta questa funzionalità per abilitare l'opzione "Mostra pagine filtro report" sulla tabella pivot creata. Di seguito è riportata la schermata che mostra l'opzione in Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

A seguito di questa opzione, il workbook creato contiene più fogli di lavoro. Suddivide ogni possibile valore del filtro dei report in un foglio di lavoro separato. In questo esempio, c'è un filtro su "Posizione" e i dati hanno tre posizioni distinte (A, B, C). Questa funzionalità aggiunge 3 fogli di lavoro aggiuntivi denominati A, B, C che sono la stessa tabella pivot ma con l'opzione preselezionata A, B e C.

Il file di esempio e il file di output possono essere scaricati dai seguenti link:

[samplePivotTable.xlsx](81920917.xlsx)

[outputSamplePivotTable.xls](81920918.xlsx)

## Codice Sorgente

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-ShowReportFilterPagesOption-1.java" >}}
{{< app/cells/assistant language="java" >}}
