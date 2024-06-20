---
title: Infoga eller ta bort rader i ett Excel ark
type: docs
weight: 20
url: /sv/python-net/insert-or-delete-rows-in-an-excel-worksheet/
description: Den här artikeln tillhandahåller Python koden för att infoga och ta bort rader i Excel kalkylblad med hjälp av Aspose.Cells för Python via .NET biblioteket.
keywords: Python Excel bibliotek, Python infoga eller ta bort rader i Excel kalkylblad, Python infoga eller ta bort rader i Excel, Python infoga rader i Excel, Python ta bort rader i Excel, infoga eller ta bort rader i Excel kalkylblad med Python, infoga eller ta bort rader i Excel med Python, infoga rader i Excel med Python, ta bort rader i Excel med Python
---

{{% alert color="primary" %}}

När du skapar ett nytt arbetsblad eller arbetar med ett befintligt arbetsblad kan du behöva lägga till extra rader eller kolumner för att rymma data. Ibland kan du behöva ta bort rader eller kolumner från specificerade positioner i arbetsbladet.

{{% /alert %}}

Aspose.Cells för Python via .NET erbjuder två metoder för att infoga och ta bort rader: [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) och [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/). Dessa metoder är optimerade för prestanda och utför jobbet mycket snabbt.

För att infoga eller ta bort ett antal rader rekommenderar vi alltid att du använder  [**Cells.insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/) och [**Cells.delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/) metoderna istället för att använda  [**Cells.insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row) eller [**delete_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_row) metoderna i en slinga.

Aspose.Cells for Python via .NET fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till, skiftas arbetsbladets innehåll nedåt och åt höger. När rader eller kolumner tas bort, skiftas arbetsbladets innehåll uppåt eller åt vänster. Eventuella referenser i andra arbetsblad och celler uppdateras när rader läggs till eller tas bort.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertDeleteRows-1.py" >}}
