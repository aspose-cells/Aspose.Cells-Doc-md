---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot
type: docs
weight: 80
url: /it/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: Questo articolo mostra come specificare se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells per Excel Python, libreria Python Excel, Specifica se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET fornisce la proprietà [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) che puoi usare per specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot. Se è vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se **false**, una stringa non avrà la suddetta restrizione. Il valore predefinito è **true**.

{{% /alert %}}

## **Come specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot**

Il codice di esempio seguente spiega l'uso della proprietà [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/). La stringa originale è lunga 383 caratteri. Ma quando la proprietà [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) è impostata su **true** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando la proprietà [**PivotTable.is_excel_2003_compatible**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) è impostata su **false** e la tabella pivot viene di nuovo aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
