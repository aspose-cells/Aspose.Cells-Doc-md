---
title: Infoga eller ta bort rader i ett Excel ark
type: docs
weight: 20
url: /sv/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Den här artikeln tillhandahåller C# koden för att infoga och ta bort rader i Excel ark
keywords: c# infoga eller ta bort rader i Excel ark, c# infoga eller ta bort rader i Excel, c# infoga rader i Excel, c# ta bort rader i Excel, infoga eller ta bort rader i Excel ark med c#, infoga eller ta bort rader i Excel med c#, infoga rader i Excel med c#, ta bort rader i Excel med c#
---

{{% alert color="primary" %}}

När du skapar ett nytt arbetsblad eller arbetar med ett befintligt arbetsblad kan du behöva lägga till extra rader eller kolumner för att rymma data. Ibland kan du behöva ta bort rader eller kolumner från specificerade positioner i arbetsbladet.

{{% /alert %}}

Aspose.Cells erbjuder två metoder för att infoga och ta bort rader:  [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) och [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Dessa metoder är optimerade för prestanda och utför jobbet mycket snabbt.

För att infoga eller ta bort ett antal rader rekommenderar vi alltid att du använder  [**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) och [**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) metoderna istället för att använda  [**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) eller [**DeleteRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow) metoderna i en slinga.

Aspose.Cells fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till skiftas innehållet i arbetsbladet nedåt och till höger. När rader eller kolumner tas bort skiftas innehållet i arbetsbladet uppåt eller till vänster. Alla referenser i andra arbetsblad och celler uppdateras när rader läggs till eller tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
