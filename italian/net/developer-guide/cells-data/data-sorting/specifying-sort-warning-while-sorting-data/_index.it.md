---
title: Specificare avviso di ordinamento durante l ordinamento dei dati
type: docs
weight: 140
url: /it/net/specifying-sort-warning-while-sorting-data/
description: Scopri come specificare un avviso di ordinamento durante l ordinamento dei dati utilizzando l API Aspose.Cells for .NET.
keywords: Aggiungi avviso di ordinamento durante l ordinamento dei dati, imposta l avviso di ordinamento durante l ordinamento dei dati, seleziona l avviso di ordinamento durante l ordinamento dei dati.
---

## **Possibili Scenari di Utilizzo**

Si prega di considerare questi dati testuali, cioè {11, 111, 22}. Questi dati testuali sono ordinati perché, in termini di testo, 111 viene prima di 22. Ma, se si desidera ordinare questi dati non come testo ma come numeri, diventeranno {11, 22, 111} perché numericamente 111 viene dopo 22. Aspose.Cells fornisce la proprietà {0} per gestire questo problema. Si prega di impostare questa proprietà su **true** e i vostri dati testuali verranno ordinati come dati numerici. La seguente schermata mostra l'avviso di ordinamento mostrato da Microsoft Excel quando i dati testuali che sembrano dati numerici vengono ordinati.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Codice di Esempio**

Il seguente codice di esempio illustra l'uso della proprietà [**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) come spiegato in precedenza. Si prega di controllare il [file di esempio Excel](43352075.xlsx) e l' [output Excel file](43352076.xlsx) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
{{< app/cells/assistant language="csharp" >}}
