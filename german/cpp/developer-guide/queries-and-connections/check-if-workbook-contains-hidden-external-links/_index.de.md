---
title: Überprüfen, ob die Arbeitsmappe versteckte externe Links enthält, mit C++
linktitle: Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält
type: docs
weight: 230
url: /de/cpp/check-if-workbook-contains-hidden-external-links/
description: Lernen Sie, wie Sie versteckte externe Links in Excel Arbeitsmappen mit {Aspose.Cells for C++} erkennen.
---

## **Mögliche Verwendungsszenarien**
Manchmal enthält die Arbeitsmappe externe Links, die versteckt sind und in Microsoft Excel nicht sichtbar sind. Aspose.Cells ruft alle externen Links ab, egal ob sichtbar oder versteckt. Sie können die Eigenschaft [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) verwenden, um zu prüfen, ob der externe Link sichtbar ist.

## **Überprüfen, ob die Arbeitsmappe versteckte externe Verknüpfungen enthält**
Der folgende Beispielcode lädt die [Quelldatei](5115413.xlsx), die versteckte externe Links enthält. Diese Links sind in Microsoft Excel nicht sichtbar, aber im Arbeitsbuch vorhanden. Nach dem Drucken von [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) und der Eigenschaft [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/) wird die Eigenschaft [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/) ausgegeben. In der untenstehenden Konsolenausgabe sehen Sie, dass alle externen Links nicht sichtbar sind.

### **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes bei Ausführung mit der angegebenen [Beispiel-Excel-Datei](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
