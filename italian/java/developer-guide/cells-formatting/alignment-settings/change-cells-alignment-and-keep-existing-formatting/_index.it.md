---
title: Modificare l allineamento delle celle e mantenere la formattazione esistente
type: docs
weight: 260
url: /it/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte, si desidera cambiare l'allineamento di più celle ma mantenere anche la formattazione esistente. Aspose.Cells ti permette di farlo usando la proprietà [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). Se imposti **true**, i cambiamenti nell'allineamento avranno luogo altrimenti no. Si osservi che l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) viene passato come parametro al metodo [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) che applica effettivamente la formattazione al range delle celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file di Excel di esempio](67338592.xlsx), crea il range e lo allinea al centro sia in modo orizzontale che verticale e mantiene intatta la formattazione esistente. La seguente schermata confronta il file di Excel di esempio e il [file di Excel di output](67338591.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro sia orizzontalmente che verticalmente.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
