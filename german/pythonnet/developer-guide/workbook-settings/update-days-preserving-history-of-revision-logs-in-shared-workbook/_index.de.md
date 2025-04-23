---
title: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe
type: docs
weight: 80
url: /de/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie an einer Arbeitsmappe zusammenarbeiten, erhalten Sie eine Option namens ***Änderungshistorie für N Tage beibehalten***, wie im folgenden Screenshot gezeigt. Mit Aspose.Cells für Python via .NET können Sie die Anzahl der Tage zur Aufbewahrung der Historie mit der [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history)-Eigenschaft aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Revisionsprotokolle, um den Verlauf 7 Tage lang zu speichern, was normalerweise 30 Tage beträgt. Bitte sehen Sie die [Ausgabedatei Excel](60489773.xlsx), die vom Code erstellt wurde, als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

