---
title: Specificare avviso di ordinamento durante l ordinamento dei dati
type: docs
weight: 140
url: /it/python-net/specifying-sort-warning-while-sorting-data/
description: Scopri come specificare l avviso di ordinamento durante l ordinamento dei dati utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Aggiungi avviso di ordinamento durante l ordinamento dei dati Python, Imposta avviso di ordinamento durante l ordinamento dei dati Python, Seleziona avviso di ordinamento durante l ordinamento dei dati Python.
---

## **Possibili Scenari di Utilizzo**

Si prega di considerare questi dati testuali ovvero {11, 111, 22}. Questi dati testuali sono ordinati perché, in termini di testo, 111 viene prima di 22. Ma, se si desidera ordinare questi dati non come testo ma come numeri, diventerà {11, 22, 111} perché numericamente 111 viene dopo 22. Aspose.Cells per Python via .NET fornisce la proprietà {0} per gestire questo problema. Si prega di impostare questa proprietà **true** e i dati testuali verranno ordinati come dati numerici. La seguente schermata mostra l'avviso di ordinamento mostrato da Microsoft Excel quando i dati testuali che sembrano dati numerici vengono ordinati.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Codice di Esempio**

Il seguente codice di esempio illustra l'uso della proprietà [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) come spiegato in precedenza. Si prega di controllare il [file di esempio Excel](43352075.xlsx) e l' [output Excel file](43352076.xlsx) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
