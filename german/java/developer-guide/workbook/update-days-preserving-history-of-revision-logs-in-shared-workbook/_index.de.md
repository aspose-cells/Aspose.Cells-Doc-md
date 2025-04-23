---
title: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe
type: docs
weight: 90
url: /de/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Arbeitsmappe freigeben, erhalten Sie eine Option mit der Bezeichnung ***Änderungsverlauf für N Tage beibehalten***, wie im folgenden Screenshot gezeigt. Sie können die Anzahl der Tage zur Beibehaltung des Verlaufs mithilfe von Aspose.Cells mit der Eigenschaft [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory) aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielscode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Verlaufprotokolltage unter Beibehaltung des Verlaufs auf 7 Tage, was normalerweise 30 Tage beträgt. Bitte beachten Sie die durch den Code generierte [Ausgabedatei Excel](60489784.xlsx) als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
