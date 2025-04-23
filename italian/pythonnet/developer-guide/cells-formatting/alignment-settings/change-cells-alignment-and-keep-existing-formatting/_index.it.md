---
title: Modificare l allineamento delle celle e mantenere la formattazione esistente
description: Usa la libreria Aspose.Cells per Python via .NET per cambiare l’allineamento delle celle e preservare la formattazione esistente
keywords: Aspose.Cells per Python via .NET, allineamento celle Python, preserva la formattazione esistente
type: docs
weight: 340
url: /it/python-net/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte vuoi cambiare l’allineamento di più celle ma anche mantenere la formattazione esistente. Aspose.Cells per Python via .NET ti permette di farlo usando la proprietà [**StyleFlag.alignments**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag/alignments). Se la imposti a **true**, le modifiche all’allineamento avverranno altrimenti no. Nota che l’oggetto [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag) viene passato come parametro al metodo [**Range.apply_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style) che applica effettivamente la formattazione a un intervallo di celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file Excel di esempio](67338585.xlsx), crea l'intervallo e centra l'allineamento in modo orizzontale e verticale e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e il [file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro in modo orizzontale e verticale.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeCellsAlignmentAndKeepExistingFormatting.py" >}}

