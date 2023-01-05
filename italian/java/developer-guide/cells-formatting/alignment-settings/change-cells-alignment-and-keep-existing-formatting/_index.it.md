---
title: Modificare l'allineamento Cells e mantenere la formattazione esistente
type: docs
weight: 260
url: /it/java/change-cells-alignment-and-keep-existing-formatting/
---
## **Possibili scenari di utilizzo**

A volte, vuoi cambiare l'allineamento di più celle ma vuoi anche mantenere la formattazione esistente. Aspose.Cells ti permette di farlo utilizzando il[**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments) proprietà. Se lo imposterai**VERO** , i cambiamenti nell'allineamento avranno luogo altrimenti no. Notare che,[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) oggetto viene passato come parametro a[**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) metodo che applica effettivamente la formattazione all'intervallo di celle.

## **Modificare l'allineamento Cells e mantenere la formattazione esistente**

Il codice di esempio seguente carica il file[esempio di file Excel](67338592.xlsx), crea l'intervallo e il centro lo allinea orizzontalmente e verticalmente e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e[file Excel di output](67338591.xlsx)e mostra che tutta la formattazione esistente delle celle è la stessa, tranne per il fatto che le celle ora sono allineate al centro orizzontalmente e verticalmente.

![cose da fare:immagine_alt_testo](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
