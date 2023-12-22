---
title: Modifica l'allineamento Cells e mantieni la formattazione esistente
description: Utilizza la libreria Aspose.Cells per modificare l'allineamento delle celle e preservare la formattazione esistente
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /it/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **Possibili scenari di utilizzo**

A volte, vuoi modificare l'allineamento di più celle ma vuoi anche mantenere la formattazione esistente. Aspose.Cells ti permette di farlo utilizzando il[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) proprietà. Se lo imposterai *true**, i cambiamenti nell'allineamento avranno luogo altrimenti no. Notare che,[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) l'oggetto viene passato come parametro a[**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)metodo che applica effettivamente la formattazione a un intervallo di celle.

##  **Modifica l'allineamento Cells e mantieni la formattazione esistente**

 Il codice di esempio seguente carica il file[file Excel di esempio](67338585.xlsx) , crea l'intervallo e il centro lo allinea orizzontalmente e verticalmente e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e[file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa, tranne per il fatto che le celle ora sono allineate al centro orizzontalmente e verticalmente.

![cose da fare:immagine_alt_testo](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
