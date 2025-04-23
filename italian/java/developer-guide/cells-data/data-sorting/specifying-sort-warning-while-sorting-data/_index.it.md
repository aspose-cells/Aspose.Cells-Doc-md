---
title: Specificare avviso di ordinamento durante l ordinamento dei dati
type: docs
weight: 100
url: /it/java/specifying-sort-warning-while-sorting-data/
---

## **Possibili Scenari di Utilizzo**
Si prega di considerare questi dati testuali ovvero {11, 111, 22}. Questi dati testuali sono ordinati così perché in termini di testo, 111 viene prima di 22. Tuttavia, se si desidera ordinare questi dati non come testo ma come numeri, diventeranno {11, 22, 111} perché numericamente 111 viene dopo 22. Aspose.Cells fornisce la proprietà [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) per gestire questo problema. Impostare questa proprietà su **true** e i dati testuali verranno ordinati come dati numerici. La schermata seguente mostra l'avviso di ordinamento visualizzato da Microsoft Excel quando i dati testuali che sembrano dati numerici vengono ordinati.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Codice di Esempio**
Il seguente codice di esempio illustra l'uso della proprietà [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) come spiegato in precedenza. Si prega di controllare il [file Excel di esempio](43352077.xlsx) e il [file Excel di output](43352078.xlsx) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
{{< app/cells/assistant language="java" >}}
