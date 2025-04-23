---
title: Uppdatera antal sparade historikrevisioner på delad arbetsbok
type: docs
weight: 90
url: /sv/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Möjliga användningsscenario**

När du delar en arbetsbok får du ett alternativ som säger ***Behåll ändringshistorik i N dagar*** som visas i följande skärmbild. Du kan uppdatera antalet dagar som historiken bevaras genom att använda Aspose.Cells med [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory) egenskapen.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Den följande provkoden skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggarna att behålla historiken i 7 dagar, vilket normalt är 30 dagar. Se [utmatningen Excel-filen](60489784.xlsx) som genereras av koden för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
