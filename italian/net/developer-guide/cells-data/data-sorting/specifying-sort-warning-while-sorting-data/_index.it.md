---
title: Specifica dell'avviso di ordinamento durante l'ordinamento dei dati
type: docs
weight: 140
url: /it/net/specifying-sort-warning-while-sorting-data/
---
## **Possibili scenari di utilizzo**

Si prega di considerare questi dati testuali, ad esempio {11, 111, 22}. Questi dati testuali sono ordinati perché, in termini di testo, 111 viene prima di 22. Ma, se vuoi ordinare questi dati non come testo ma come numeri, allora diventeranno {11, 22, 111} perché numericamente 111 viene dopo 22 Aspose.Cells fornisce[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)proprietà per affrontare questo problema. Si prega di impostare questa proprietà**VERO**e i tuoi dati testuali saranno ordinati come dati numerici. Lo screenshot seguente mostra l'avviso di ordinamento mostrato da Microsoft Excel quando vengono ordinati dati testuali che sembrano dati numerici.

![cose da fare:immagine_alt_testo](specifying-sort-warning-while-sorting-data_1.png)

## **Codice d'esempio**

 Il codice di esempio seguente illustra l'utilizzo di[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)proprietà come spiegato in precedenza. Si prega di controllare il suo[esempio di file Excel](43352075.xlsx) e[file Excel di output](43352076.xlsx) per ulteriore aiuto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
