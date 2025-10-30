---
title: Modificare l allineamento delle celle e mantenere la formattazione esistente
linktitle: Modificare l allineamento delle celle e mantenere la formattazione esistente
description: Usa la libreria Aspose.Cells per cambiare l allineamento delle celle e preservare la formattazione esistente in Node.js tramite C++
keywords: Aspose.Cells, Node.js tramite C++, Allineamento celle, preserva la formattazione esistente
type: docs
weight: 340
url: /it/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Possibili Scenari di Utilizzo**

A volte, vuoi cambiare l'allineamento di più celle ma anche mantenere la formattazione esistente. Aspose.Cells for Node.js via C++ permette di farlo usando il metodo [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-). Se lo imposti **true**, i cambiamenti nell'allineamento avranno effetto, altrimenti no. Nota che, l'oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) viene passato come parametro al metodo [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-), che effettivamente applica la formattazione a un intervallo di celle.

## **Modifica dell'allineamento delle celle e mantenimento della formattazione esistente**

Il seguente codice di esempio carica il [file Excel di esempio](67338585.xlsx), crea l'intervallo e centra l'allineamento in modo orizzontale e verticale e mantiene intatta la formattazione esistente. Lo screenshot seguente confronta il file Excel di esempio e il [file Excel di output](67338586.xlsx) e mostra che tutta la formattazione esistente delle celle è la stessa tranne che le celle sono ora allineate al centro in modo orizzontale e verticale.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
