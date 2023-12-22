---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot
type: docs
weight: 80
url: /it/python-net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
description: In questo articolo viene illustrato come specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot con Aspose.Cells for Python via .NET.
keywords: Specify whether the PivotTable is compatible for Excel2003 while refreshing PivotTable
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET fornisce il[**Tabella pivot.is_excel_2003_compatibile**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) proprietà che è possibile utilizzare per specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot. Se vero, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se *false**, una stringa non avrà la restrizione sopra menzionata. Il valore predefinito è *true**.

{{% /alert %}}

##  **Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot**

 Il seguente codice di esempio spiega l'utilizzo di[**Tabella pivot.is_excel_2003_compatibile**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) proprietà. La stringa originale è lunga 383 caratteri. Ma quando[**Tabella pivot.is_excel_2003_compatibile**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la proprietà è impostata**VERO** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando[**Tabella pivot.is_excel_2003_compatibile**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_excel_2003_compatible/) la proprietà è impostata**falso** la tabella pivot viene nuovamente aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SpecifyCompatibility-1.py" >}}
