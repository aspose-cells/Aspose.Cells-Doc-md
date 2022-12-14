---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot
type: docs
weight: 80
url: /it/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce il[**PivotTable.IsExcel2003Compatibile**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible)proprietà che è possibile utilizzare per specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot. Se vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se**falso** , una stringa non avrà la suddetta restrizione. Il valore predefinito è**VERO**.

{{% /alert %}}

## **Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot**

 Il seguente codice di esempio spiega l'utilizzo di[**PivotTable.IsExcel2003Compatibile**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) proprietà. La stringa originale è lunga 383 caratteri. Ma quando[**PivotTable.IsExcel2003Compatibile**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) proprietà è impostata**VERO** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando[**PivotTable.IsExcel2003Compatibile**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) proprietà è impostata**falso** e la tabella pivot viene nuovamente aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
