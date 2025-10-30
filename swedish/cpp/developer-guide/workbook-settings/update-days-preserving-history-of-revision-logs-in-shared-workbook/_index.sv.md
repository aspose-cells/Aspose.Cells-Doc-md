---
title: Uppdatera dagar och bevara revisionslogg i delat arbetsbok med C++
linktitle: Uppdatera antal sparade historikrevisioner på delad arbetsbok
type: docs
weight: 80
url: /sv/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Lär dig hur du uppdaterar antalet dagar för att bevara historik i ett delat arbetsblad med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

När du delar en arbetsbok får du alternativet att ***Spara ändringshistorik i N dagar*** som visas i följande skärmbild. Du kan uppdatera antalet dagar att spara historik med hjälp av Aspose.Cells med egenskapen [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/).

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Uppdatera antal sparade historikrevisioner på delad arbetsbok**

Följande exempelkod skapar en tom arbetsbok, delar den sedan och uppdaterar revisionsloggar dagar med bibehållen historia till 7 dagar, vilket normalt är 30 dagar. Se [output Excel-filet](60489773.xlsx) som genereras av koden för en referens.

## **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
