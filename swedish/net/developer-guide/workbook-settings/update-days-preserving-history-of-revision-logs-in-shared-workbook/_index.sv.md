---
title: Uppdatera antal sparade historikrevisioner på delad arbetsbok
type: docs
weight: 80
url: /sv/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Möjliga användningsscenario**

När du delar en arbetsbok får du alternativet att ***Spara ändringshistorik i N dagar*** som visas i följande skärmbild. Du kan uppdatera antalet dagar att spara historik med hjälp av Aspose.Cells med egenskapen [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/net/aspose.cells.revisions/revisionlogcollection/properties/dayspreservinghistory).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Följande exempelkod skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggar dagar med bibehållen historia till 7 dagar, vilket normalt är 30 dagar. Se [output Excel-filet](60489773.xlsx) som genereras av koden för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.cs" >}}
