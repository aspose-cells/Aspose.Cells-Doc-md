---
title: Inserisci sequenza temporale
linktitle: Linea del tempo
type: docs
weight: 170
url: /it/java/create-timeline/
description: Scopri come creare una sequenza temporale con Aspose.Cells per java.
---
## **Possibili scenari di utilizzo**

 Invece di regolare i filtri per mostrare le date, puoi utilizzare una sequenza temporale della tabella pivot, un'opzione di filtro dinamico che ti consente di filtrare facilmente per data/ora e ingrandire il periodo desiderato con un controllo a scorrimento. Microsoft Excel consente di creare una sequenza temporale selezionando una tabella pivot e quindi facendo clic su*Inserisci > Cronologia*. Aspose.Cells per java consente inoltre di creare una sequenza temporale utilizzando il metodo [**Worksheet.getTimelines.add()**].

## **Crea sequenza temporale in una tabella pivot**

 Vedere il seguente codice di esempio. Carica il[esempio di file Excel](input.xlsx) che contiene la tabella pivot. Quindi crea la sequenza temporale basata sul primo campo pivot di base. Infine, salva la cartella di lavoro in[uscita XLSX](output.xlsx) formato. Lo screenshot seguente mostra la sequenza temporale creata da Aspose.Cells nel file Excel di output.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

