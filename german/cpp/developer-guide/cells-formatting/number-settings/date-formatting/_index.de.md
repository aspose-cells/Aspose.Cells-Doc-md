---
title: So formatieren Sie Zahlen in C++ als Datum
linktitle: So formatieren Sie Zahlen als Datum
type: docs
weight: 10
url: /de/cpp/format-number-to-date/
description: Dieser Artikel erklärt, wie man Zahlen mit der API Aspose.Cells for C++ in ein Datum umwandelt.
keywords: Zahlenformat als Datum, Zelleinstellungen, Zahl zu Datum formatieren, Datums und Zeiteinstellungen, Datumsformat.
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen als Daten in Excel (oder jeder Tabellenkalkulationssoftware) ist aus mehreren Gründen wichtig, insbesondere wenn Sie mit Daten arbeiten, die Zeit- oder Terminplanungsinformationen enthalten. Hier ist, warum das Formatieren von Zahlen in Daten vorteilhaft ist:

1. **Richtige Interpretation von Datumswerten**: In Excel werden Daten als Seriennummern gespeichert (z.B. 1 steht für den 1. Januar 1900 und 44210 steht für den 6. September 2021). Wenn diese Zahlen nicht als Daten formatiert sind, sehen Nutzer möglicherweise bedeutungslose Zahlen statt erkennbare Daten. Die richtige Formatierung ermöglicht Excel, sie als tatsächliche Daten anzuzeigen (z.B. 06.09.2021 statt 44210).
2. **Vereinfachung zeitbezogener Berechnungen**: Excel kann viele Berechnungen mit Daten durchführen, z.B. die Anzahl der Tage zwischen zwei Daten berechnen, Tage addieren oder subtrahieren oder den Wochentag bestimmen. Wenn die Zahlen nicht als Daten formatiert sind, kann Excel diese Berechnungen nicht effizient durchführen. Beispielsweise können Sie die Anzahl der Tage zwischen dem 01.09.2023 und dem 01.10.2023 leicht berechnen, wenn die Zahlen im Datumsformat vorliegen.
3. **Stellt Konsistenz sicher**: Wenn alle datumsbezogenen Werte korrekt formatiert sind, erscheint alle Daten in einem einheitlichen, lesbaren Stil. Diese Konsistenz ist z.B. in Geschäftsberichten, Projektplänen und Datenbanken wichtig, in denen die Datumsangaben einheitlich sein müssen. Verschiedene Regionen verwenden unterschiedliche Datumsformate (z.B. MM/TT/JJJJ in den USA vs. TT/MM/JJJJ in anderen Ländern), daher hilft die Formatierung, die Daten richtig zu interpretieren.
4. **Verbessert die Lesbarkeit**: Daten im Standardformat (z.B. 01.01.2024) sind leichter zu lesen als Rohseriennummern wie 45000. Die richtige Datumformatierung macht Ihre Tabelle benutzerfreundlicher und vermeidet Verwirrung. Dies ist besonders wichtig bei Terminplanung, Zeitlinien, Veranstaltungen oder historischen Daten.
5. **Hilft beim Sortieren und Filtern**: Wenn Daten richtig formatiert sind, erkennt Excel sie als echte Daten, was das Sortieren oder Filtern nach Zeit erleichtert. Sie können z.B. eine Liste von Ereignissen nach Datum sortieren oder einen Datenbereich filtern, um nur Datensätze zwischen zwei bestimmten Daten anzuzeigen. Ohne eine korrekte Datumformatierung erfolgt das Sortieren möglicherweise anhand der Rohzahl statt der tatsächlichen Kalendertage.
6. **Ermöglicht die Verwendung von Datumsfunktionen**: Excel bietet eine Reihe von mächtigen Datum Funktionen, wie: HEUTE(), DATEDIF(), ARBEITSTAG(), JAHR(), MONAT(), TAG(). Diese Funktionen erfordern eine korrekte Formatierung der Daten für genaue Berechnungen.
7. **Unterstützt Visualisierungen (Diagramme/Zeitstrahlen)**: Richtig formatierte Daten können verwendet werden, um Diagramme und Grafiken zu erstellen, bei denen die Zeit eine Schlüsselachse ist. Zum Beispiel benötigt Excel in einem Zeitlelidiagramm Daten in einem anerkannten Format, um Ereignisse genau abzubilden. Falsch formatierte oder nicht formatierte Zahlen können dazu führen, dass Diagramme keinen Sinn ergeben oder falsche Informationen widerspiegeln.
8. **Verhindert Fehlinterpretationen**: Rohzahlen können leicht falsch interpretiert werden. Zum Beispiel könnte 44210 als allgemeiner numerischer Wert gelesen werden, aber als Datum formatiert zeigt es, dass es der 6. September 2021 ist. Richtig formatierte Daten helfen, Fehlinterpretationen zu vermeiden.
9. **Erleichtert die Dateneingabe**: Wenn Zellen als Daten formatiert sind, werden Nutzer aufgefordert, Daten in einem gültigen Datumsformat einzugeben, was Eingabefehler verhindert und sicherstellt, dass Datumswerte korrekt erfasst werden.
10. **Wichtig für Terminplanung und Nachverfolgung**: Bei allen Szenarien, die Terminplanung, Nachverfolgung oder Fristen enthalten (z.B. Projektmanagement, Finanzprognosen oder zeitkritische Berichte), ist es entscheidend, Zahlen als Daten zu formatieren, um Genauigkeit und Verständnis sicherzustellen. Es erleichtert die bessere Planung und Umsetzung.

## **So formatieren Sie Zahlen in Excel zu Datum**
Um eine Zahl in Excel als Datum zu formatieren, folgen Sie diesen Schritten:

### **Verwendung des Menübands (Start Register)**
1. Wählen Sie die Zellen mit den Zahlen aus, die Sie als Datum formatieren möchten.
2. Gehen Sie zum Start-Register im Menüband.
3. Klicken Sie in der Gruppe Zahl auf den Dropdown-Pfeil im Feld Zahlformat (es zeigt möglicherweise "Allgemein" oder "Zahl" an).
4. Wählen Sie im Dropdown kurz Datum oder lang Datum aus. Kurz Datum: Zeigt das Datum in einem kompakten Format an, z.B. MM/TT/JJJJ (US-Format) oder TT/MM/JJJJ (internationales Format). Lang Datum: Zeigt das Datum in einem ausführlicheren Format an, z.B. Montag, 1. Januar 2024.
<br>
<img src="1.png" width=60% />

### **Verwenden des Dialogfelds Zellen formatieren**
1. Wählen Sie die Zellen aus, die Sie formatieren möchten.
2. Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie Zellen formatieren aus, oder drücken Sie Strg + 1 (Windows) oder Cmd + 1 (Mac).
3. Gehen Sie im Dialogfeld Zellen formatieren zum Registernummer.
4. Wählen Sie in der Liste auf der linken Seite Datum.
5. Wählen Sie das gewünschte Datumsformat aus der Liste auf der rechten Seite aus (z. B. MM/TT/JJJJ, Tag/Monat/Jahr oder benutzerdefinierte Formate).
<br>
<img src="2.png" width=60% />
6. Klicken Sie auf OK, um das Datumsformat anzuwenden.

## **So formatieren Sie Zahlen als Datum in Aspose.Cells**

Um Zahlen in der Bibliothek Aspose.Cells for C++ zur Arbeit mit Excel-Dateien als Datum zu formatieren, können Sie das Datumsformat programmatisch auf Zellen anwenden. So funktioniert es mit C++ und Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the date format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value that represents a date (e.g., 44210 represents 09/06/2021 in Excel)
    a1.PutValue(44210);

    // Create a style object to apply the date format
    Style a1Style = a1.GetStyle();

    // "14" represents a standard date format in Excel (MM/DD/YYYY)
    a1Style.SetNumber(14);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(44210);

    // Create a style object to apply the date format
    Style a2Style = a2.GetStyle();

    // Custom format for YYYY-MM-DD
    a2Style.SetCustom(u"YYYY-MM-DD");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"DateFormatted.xlsx");

    Aspose::Cells::Cleanup();
}
```
