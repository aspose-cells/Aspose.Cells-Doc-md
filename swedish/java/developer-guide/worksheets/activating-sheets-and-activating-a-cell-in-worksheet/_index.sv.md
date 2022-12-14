---
title: Aktivera ark och aktivera en Cell i kalkylblad
type: docs
weight: 5
url: /sv/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

Ibland behöver du ett specifikt kalkylblad för att vara aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. På liknande sätt kanske du vill aktivera en specifik cell och ställa in rullningslisterna så att de visar den aktiva cellen. Aspose.Cells kan utföra alla dessa uppgifter som visas nedan.

-  En**aktivt ark** är ett ark du arbetar med: det aktiva arkets namn på fliken är som standard fetstilt.
-  En**aktiv cell** är en markerad cell, cellen som data matas in i när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen markeras med en kraftig ram.

{{% /alert %}}

## **Aktivera ark och aktivera en Cell**

Aspose.Cells tillhandahåller specifika API-anrop för att aktivera ett ark och en cell. Till exempel[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)egenskapen är användbar för att ställa in det aktiva bladet i en arbetsbok. På samma sätt[**Arbetsblad.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)egenskap kan användas för att ställa in och få en aktiv cell i kalkylbladet.

Använd[**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)och[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)egenskaper.

Följande exempel visar hur man aktiverar ett kalkylblad och gör en aktiv cell i det. Följande utdata genereras när koden exekveras. Rullningslisterna rullas för att göra den andra raden och den andra kolumnen som deras första synliga rad och kolumn.

**Ställer in B2-cell som en aktiv cell**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java-kod för att ställa in ett aktivt kalkylblad i Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 I**utvärdering** läge, det vill säga; utan att ställa in en giltig licens kommer det aktiva arbetsbladet alltid att vara det som innehåller utvärderingsvattenstämpeln. Detta beteende kan endast åsidosättas genom att ställa in licensen i början av programmet.

{{% /alert %}}
