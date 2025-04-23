---
title: Inserisci la timeline
linktitle: Timeline
type: docs
weight: 170
url: /it/nodejs-cpp/create-timeline/
description: Scopri come creare una timeline con Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Invece di regolare i filtri per mostrare le date, puoi usare una Timeline di PivotTable—un'opzione di filtro dinamico che ti permette di filtrare facilmente per data/ora e ingrandire il periodo desiderato con un controllo a cursore. Microsoft Excel consente di creare una timeline selezionando una tabella pivot e cliccando su *Inserisci > Timeline*. Aspose.Cells for Node.js via C++ consente anche di creare una timeline usando il metodo [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Creare una timeline per una tabella pivot**

Vedi il seguente esempio di codice. Carica il [file Excel di esempio](input.xlsx) che contiene la tabella pivot. Successivamente crea la timeline basata sul primo campo pivot di base. Infine, salva il workbook in formato [output XLSX](output.xlsx). Lo screenshot seguente mostra la timeline creata da Aspose.Cells for Node.js via C++ nel file Excel di output.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

