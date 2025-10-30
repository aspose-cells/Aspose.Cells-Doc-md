---
title: Inserire una timeline con Golang tramite C++
linktitle: Timeline
type: docs
weight: 170
url: /it/go-cpp/create-timeline/
description: Impara come creare una linea temporale con Aspose.Cells usando C++.
---

## **Possibili Scenari di Utilizzo**

Invece di regolare i filtri per mostrare le date, puoi usare una Timeline PivotTable—un'opzione di filtro dinamico che ti permette di filtrare facilmente per data/ora e ingrandire il periodo desiderato con un controllo a cursore. Microsoft Excel ti permette di creare una timeline selezionando una tabella pivot e cliccando su *Inserisci > Timeline*. Aspose.Cells ti permette anche di creare una timeline usando il metodo [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/).

## **Creare una timeline per una tabella pivot**

Si prega di consultare il codice di esempio seguente. Carica il [file di Excel di esempio](input.xlsx) contenente la tabella pivot. Crea quindi la timeline basata sul primo campo pivot di base. Infine, salva il workbook nel formato [XLSX di output](output.xlsx). La seguente schermata mostra la timeline creata da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}
