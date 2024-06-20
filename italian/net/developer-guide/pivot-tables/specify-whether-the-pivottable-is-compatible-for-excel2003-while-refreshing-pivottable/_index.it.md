---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot
type: docs
weight: 80
url: /it/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) che puoi utilizzare per specificare se la tabella pivot è compatibile per Excel 2003 durante l'aggiornamento della tabella pivot. Se è vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se è falso, una stringa non avrà la restrizione menzionata. Il valore predefinito è vero.

{{% /alert %}}

## **Specificare se la tabella pivot è compatibile per Excel2003 durante l'aggiornamento della tabella pivot**

Il codice di esempio seguente spiega l'uso della proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible). La stringa originale è lunga 383 caratteri. Ma quando la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) è impostata su **true** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando la proprietà [**PivotTable.IsExcel2003Compatible**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isexcel2003compatible) è impostata su **false** e la tabella pivot viene di nuovo aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTableExamples-SpecifyCompatibility-1.cs" >}}
