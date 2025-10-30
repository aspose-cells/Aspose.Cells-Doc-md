---
title: Modifica l’allineamento delle celle e mantieni la formattazione esistente con Golang tramite C++
description: Utilizzare la libreria Aspose.Cells per modificare l allineamento delle celle e preservare la formattazione esistente
keywords: Aspose.Cells, C++, allineamento celle, preserva la formattazione esistente
type: docs
weight: 340
url: /it/go-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte vuoi cambiare l'allineamento di più celle ma vuoi anche conservare la formattazione esistente. Aspose.Cells ti permette di farlo usando la proprietà [**GetAlignments()**](https://reference.aspose.com/cells/go-cpp/styleflag/getalignments/). Se impostata a **true**, avverranno modifiche nell'allineamento, altrimenti no. Nota che l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag) viene passato come parametro al metodo [**ApplyStyle(const Style\& style, const StyleFlag\& flag)**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/) che applica effettivamente la formattazione a un intervallo di celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file Excel di esempio](67338585.xlsx), crea l'intervallo e centra l'allineamento in modo orizzontale e verticale e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e il [file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro in modo orizzontale e verticale.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeCellsAlignmentAndKeepExistingFormatting.go" >}}
