---
title: Modificare l allineamento delle celle e mantenere la formattazione esistente
description: Utilizzare la libreria Aspose.Cells per modificare l allineamento delle celle e preservare la formattazione esistente
keywords: Aspose.Cells, C#, Allineamento celle, mantenere la formattazione esistente
type: docs
weight: 340
url: /it/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte desideri modificare l'allineamento di più celle ma vuoi anche mantenere la formattazione esistente. Aspose.Cells ti permette di farlo utilizzando la proprietà [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). Se imposti **true**, le modifiche all'allineamento avranno luogo altrimenti no. Si prega di notare che l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) viene passato come parametro al metodo [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle) che in realtà applica la formattazione a un intervallo di celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file Excel di esempio](67338585.xlsx), crea l'intervallo e centra l'allineamento in modo orizzontale e verticale e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e il [file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro in modo orizzontale e verticale.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
