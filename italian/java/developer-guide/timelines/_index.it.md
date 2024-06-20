---
title: Inserisci la timeline
linktitle: Timeline
type: docs
weight: 170
url: /it/java/create-timeline/
description: Scopri come creare una timeline con Aspose.Cells per Java.
---

## **Possibili Scenari di Utilizzo**

Invece di regolare i filtri per mostrare le date, è possibile utilizzare una Timeline della tabella pivot - una opzione di filtro dinamico che consente di filtrare facilmente per data/ora e ingrandire il periodo desiderato con un controllo scorrevole. Microsoft Excel ti permette di creare una timeline selezionando una tabella pivot e poi facendo clic su *Inserisci > Timeline*. Anche Aspose.Cells per Java ti consente di creare una timeline utilizzando il metodo [**Worksheet.getTimelines.add()**].

## **Creare una timeline per una tabella pivot**

Si prega di consultare il codice di esempio seguente. Carica il [file di Excel di esempio](input.xlsx) contenente la tabella pivot. Crea quindi la timeline basata sul primo campo pivot di base. Infine, salva il workbook nel formato [XLSX di output](output.xlsx). La seguente schermata mostra la timeline creata da Aspose.Cells nel file Excel di output.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

