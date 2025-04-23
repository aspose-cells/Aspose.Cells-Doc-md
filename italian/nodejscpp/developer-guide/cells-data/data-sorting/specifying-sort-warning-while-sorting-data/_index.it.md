---
title: Specificare avviso di ordinamento durante l ordinamento dei dati
type: docs
weight: 140
url: /it/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Impara come specificare avvertimenti di ordinamento durante l ordinamento dei dati usando l’API Aspose.Cells for Node.js via C++.
keywords: Aggiungi avviso di ordinamento durante l ordinamento dei dati, imposta l avviso di ordinamento durante l ordinamento dei dati, seleziona l avviso di ordinamento durante l ordinamento dei dati.
---

## **Possibili Scenari di Utilizzo**

Considera questi dati testuali cioè {11, 111, 22}. Questi dati testuali sono ordinati perché, in termini di testo, 111 viene prima di 22. Ma, se vuoi ordinare questi dati non come testo ma come numeri, allora saranno {11, 22, 111} perché numericamente 111 viene dopo 22. Aspose.Cells for Node.js via C++ fornisce la proprietà {0} per gestire questo problema. Imposta questa proprietà **true** e i tuoi dati testuali saranno ordinati come dati numerici. La schermata seguente mostra l'avvertimento di ordinamento mostrato da Microsoft Excel quando i dati testuali che assomigliano a dati numerici vengono ordinati.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Codice di Esempio**

Il seguente codice di esempio illustra l'uso della proprietà [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-) come spiegato in precedenza. Si prega di controllare il [file di esempio Excel](43352075.xlsx) e l' [output Excel file](43352076.xlsx) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

