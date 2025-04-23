---
title: Aktualisierung der Tage bei Beibehaltung der Versionsverlaufsprotokolle in gemeinsamer Arbeitsmappe mit C++
linktitle: Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe
type: docs
weight: 80
url: /de/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Erfahren Sie, wie Sie das Tage Intervall für die Verlaufsaufbewahrung in einer gemeinsamen Arbeitsmappe mit Aspose.Cells und C++ aktualisieren.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine Arbeitsmappe freigeben, erhalten Sie eine Option ***Änderungsverlauf für N Tage beibehalten***, wie im folgenden Screenshot gezeigt. Sie können die Anzahl der Tage zur Aufbewahrung des Verlaufs unter Verwendung der Aspose.Cells mit der [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/)-Eigenschaft aktualisieren.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Aktualisieren von Tagen unter Beibehaltung des Verlaufprotokolls in einer freigegebenen Arbeitsmappe**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe, teilt sie dann und aktualisiert die Revisionsprotokolle, um den Verlauf 7 Tage lang zu speichern, was normalerweise 30 Tage beträgt. Bitte sehen Sie die [Ausgabedatei Excel](60489773.xlsx), die vom Code erstellt wurde, als Referenz an.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
