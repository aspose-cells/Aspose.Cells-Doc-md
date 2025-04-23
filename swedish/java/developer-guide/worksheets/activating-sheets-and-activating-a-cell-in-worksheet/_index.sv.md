---
title: AKtivering av blad och aktivering av en cell i arbetsbok
type: docs
weight: 5
url: /sv/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

Ibland behöver du att ett specifikt arbetsblad ska vara aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. På samma sätt kan du aktivera en specifik cell och ställa in rullningsfält för att visa den aktiva cellen. Aspose.Cells kan utföra alla dessa uppgifter som visas nedan.

- Ett **aktivt blad** är ett blad du arbetar med: det aktiva bladets namn på fliken är kursivt som standard.
- En **aktiv cell** är en vald cell, cellen där data matas in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen markeras med en kraftig ram.

{{% /alert %}}

## **Aktivering av blad och aktivering av en cell**

Aspose.Cells tillhandahåller specifika API-anrop för att aktivera ett blad och en cell. Till exempel är egenskapen [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) användbar för att ställa in det aktiva bladet i en arbetsbok. På samma sätt kan egenskapen [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) användas för att ställa in och få en aktiv cell i arbetsbladet.

För att se till att de horisontella eller vertikala rullningsfälten är på rad- och kolumnindexpositionen du vill visa specifik data, använd [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) och [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn) egenskaperna.

Följande exempel visar hur man aktiverar ett arbetsblad och gör en aktiv cell i det. Följande utdata genereras vid körning av koden. Rullningsfälten rullar för att göra den 2: a raden och den 2: a kolumnen som deras första synliga rad och kolumn.

**Ställa in B2-cell som en aktiv cell**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java-kod för att ställa in ett aktivt arbetsblad i Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

I **utvärderingsläget**, det vill säga utan att ställa in en giltig licens, kommer det aktiva arbetsbladet alltid att vara det som innehåller utvärderingsvattenstämpeln. Detta beteende kan bara överridas genom att ställa in licensen i början av applikationen.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
