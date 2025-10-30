---
title: Aktualisieren Sie Tage, während Sie die Revision Logs im geteilten Arbeitsbuch historisieren, mit Golang via C++
linktitle: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe
type: docs
weight: 80
url: /de/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Erfahren Sie, wie Sie die Anzahl der Tage zur Historienaufbewahrung in einem geteilten Arbeitsbuch mit Aspose.Cells und Golang via C++ aktualisieren können.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Arbeitsmappe freigeben, erhalten Sie eine Option ***Änderungsverlauf für N Tage beibehalten***, wie im folgenden Screenshot gezeigt. Sie können die Anzahl der Tage zur Aufbewahrung des Verlaufs unter Verwendung der Aspose.Cells mit der [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/)-Eigenschaft aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Revisionsprotokolle, um den Verlauf 7 Tage lang zu speichern, was normalerweise 30 Tage beträgt. Bitte sehen Sie die [Ausgabedatei Excel](60489773.xlsx), die vom Code erstellt wurde, als Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
