---
title: Wie man leere oder Nicht Leere Felder mit C++ filtern kann
linktitle: Wie filtert man leere oder nicht leere Felder
type: docs
weight: 85
url: /de/cpp/how-to-filter-blanks-and-non-blanks/
description: Erfahren Sie, wie man leere und Nicht Leere Felder mit der API Aspose.Cells for C++ filtert.
keywords: Leere Felder filtern, Nicht leere Felder filtern, Leere Felder im Arbeitsblatt filtern, Nicht leere Felder im Arbeitsblatt filtern, Leere Felder in Excel filtern, Nicht leere Felder in Excel filtern, Leere und Nicht leere Felder in Excel filtern
---

## **Mögliche Verwendungsszenarien**
Die Filterung von Daten in Excel ist ein wertvolles Werkzeug, das die Datenanalyse, Exploration und Präsentation verbessert, indem Benutzer sich auf bestimmte Datenuntergruppen konzentrieren können, die auf ihren Kriterien basieren. Dadurch wird der gesamte Prozess der Datenmanipulation und -interpretation effizienter und effektiver.

## **Wie man leere oder nicht leere Felder in Excel filtert**
In Excel können Sie ganz einfach leere oder nicht leere Felder mithilfe der Filteroptionen filtern. Hier erfahren Sie, wie es geht:

### **Wie man Leerzeichen in Excel filtert**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie zum Register "Daten" im Menüband.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche "Filter". Dadurch werden Filterpfeile zum ausgewählten Bereich hinzugefügt.
1. Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer "Leerzeichen" und klicken Sie auf OK. Dies zeigt nur die leeren Zellen in dieser Spalte an.
<br>
<image src="2.png" width="70%" />
1. Das Ergebnis lautet wie folgt:
<br>
<image src="3.png" width="70%" />

### **Wie man Nicht-Leerzeichen in Excel filtert**
1. Wählen Sie den Bereich aus: Klicken Sie auf den Buchstaben der Spaltenüberschrift, um die gesamte Spalte auszuwählen, oder wählen Sie den Bereich aus, in dem Sie Nicht-Leerzeichen filtern möchten.
1. Öffnen Sie das Filtermenü: Gehen Sie zum Register "Daten" im Menüband.
<br>
<image src="1.png" width="70%" />
1. Filteroptionen: Klicken Sie auf die Schaltfläche "Filter". Dadurch werden Filterpfeile zum ausgewählten Bereich hinzugefügt.
1. Nicht-Leerzeichen filtern: Klicken Sie auf den Filterpfeil in der Spalte, in der Sie Nicht-Leerzeichen filtern möchten. Deaktivieren Sie alle Optionen außer "Nicht-Leerzeichen" oder "Benutzerdefiniert" und legen Sie die Bedingungen entsprechend fest. Klicken Sie auf OK. Dies zeigt nur die Zellen an, die in dieser Spalte nicht leer sind.
<br>
<image src="4.png" width="70%" />
1. Das Ergebnis lautet wie folgt:
<br>
<image src="5.png" width="70%" />

## **Wie man Leerzeichen in Excel mit Aspose.Cells filtert**
Wenn eine Spalte Text enthält, sodass wenige Zellen leer sind, und ein Filter erforderlich ist, um nur jene Zeilen auszuwählen, in denen leere Zellen vorhanden sind, können die Funktionen [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) und [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) wie unten gezeigt verwendet werden. 

Bitte sehen Sie sich den folgenden Beispielcode an, der die [Beispiel-Excel-Datei](sample.xlsx) lädt, die einige Dummy-Daten enthält. Der Beispielcode verwendet drei Methoden, um Leerzeichen zu filtern. Anschließend speichert er die Arbeitsmappe als [ausgabe Excel-Datei](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Wie man Nicht-Leerzeichen in Excel mit Aspose.Cells filtert**

Bitte sehen Sie sich den folgenden Beispielcode an, der die [Beispieldatei Excel](sample.xlsx) lädt, die einige Dummy-Daten enthält. Nach dem Laden der Datei rufen Sie die Funktion [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) auf, um Nicht-Leer-Daten zu filtern, und speichern schließlich die Arbeitsmappe als [Ausgabe-Excel-Datei](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


