---
title: Infoga eller ta bort rader i ett Excel-kalkylblad
type: docs
weight: 20
url: /sv/net/insert-or-delete-rows-in-an-excel-worksheet/
description: Den här artikeln innehåller C#-koden för att infoga och ta bort rader i Excel-kalkylblad
keywords: c# insert or delete rows in excel worksheet, c# insert or delete rows in excel, c# insert rows in excel, c# delete rows in excel, insert or delete rows in excel worksheet with c#, insert or delete rows in excel with c#, insert rows in excel with c#, delete rows in excel with c#
---
{{% alert color="primary" %}}

När du skapar ett nytt kalkylblad eller arbetar med ett befintligt kalkylblad kan du behöva lägga till extra rader eller kolumner för att ta emot data. Vid andra tillfällen kan du behöva ta bort rader eller kolumner från angivna positioner i kalkylbladet.

{{% /alert %}}

 Aspose.Cells erbjuder två metoder för att infoga och ta bort rader:[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) och[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index). Dessa metoder är optimerade för prestanda och gör jobbet mycket snabbt.

 För att infoga eller ta bort ett antal rader rekommenderar vi att du alltid använder[**Cells.InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows/index) och[**Cells.DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows/index) metoder istället för att använda[**Cells.InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) eller[**Ta bort rad**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterow)metoder i en loop.

Aspose.Cells fungerar på samma sätt som Microsoft Excel gör. När rader eller kolumner läggs till flyttas kalkylbladets innehåll nedåt och åt höger. När rader eller kolumner tas bort flyttas kalkylbladets innehåll uppåt eller åt vänster. Eventuella referenser i andra kalkylblad och celler uppdateras när rader läggs till eller tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertDeleteRows-1.cs" >}}
