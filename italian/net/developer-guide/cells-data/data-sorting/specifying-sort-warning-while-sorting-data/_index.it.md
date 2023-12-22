---
title: Specifica dell'avviso di ordinamento durante l'ordinamento dei dati
type: docs
weight: 140
url: /it/net/specifying-sort-warning-while-sorting-data/
description: Scopri come specificare l'avviso di ordinamento durante l'ordinamento dei dati utilizzando Aspose.Cells for .NET API.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Possibili scenari di utilizzo**

Si prega di considerare questi dati testuali, ad esempio {11, 111, 22}. Questi dati testuali vengono ordinati perché, in termini di testo, 111 viene prima di 22. Ma se vuoi ordinare questi dati non come testo ma come numeri, allora diventeranno {11, 22, 111} perché numericamente 111 viene dopo 22 Aspose.Cells fornisce[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)proprietà per affrontare questo problema. Imposta questa proprietà**VERO**i tuoi dati testuali verranno ordinati come dati numerici. La schermata seguente mostra l'avviso di ordinamento mostrato da Microsoft Excel quando vengono ordinati dati testuali che assomigliano a dati numerici.

![cose da fare:immagine_alt_testo](specifying-sort-warning-while-sorting-data_1.png)

##  **Codice d'esempio**

 Il seguente codice di esempio illustra l'utilizzo di[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) proprietà come spiegato in precedenza. Per favore controllalo[file Excel di esempio](43352075.xlsx) E[file Excel di output](43352076.xlsx) per ulteriore aiuto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
