---
title: Uppdatera antal sparade historikrevisioner på delad arbetsbok
type: docs
weight: 80
url: /sv/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Möjliga användningsscenario**

När du delar en arbetsbok får du ett alternativ som säger ***Behåll ändringshistorik i N dagar*** som visas i följande skärmdump. Du kan ändra antalet dagar för att behålla historiken med Aspose.Cells för Python via .NET med egenskapen [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Följande exempelkod skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggar dagar med bibehållen historia till 7 dagar, vilket normalt är 30 dagar. Se [output Excel-filet](60489773.xlsx) som genereras av koden för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

