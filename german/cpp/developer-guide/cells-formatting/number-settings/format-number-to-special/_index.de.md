---
title: Wie man Nummern in spezieller Form mit C++ formatiert
linktitle: Wie man Nummern speziell formatiert
type: docs
weight: 10
url: /de/cpp/how-to-format-number-to-special/
description: Dieser Artikel stellt vor, wie man mit der API Aspose.Cells for C++ Nummern in einer speziellen Form formatiert.
keywords: Eine Nummer in ein spezielles Muster formatieren, Ein bestimmtes Muster zur Formatierung von Zahlen anwenden, Nummernformatierung individuell gestalten, Das Erscheinungsbild von Zahlen in ein besonderes Format bringen, Zahlen einer bestimmten Formatierungsregel folgen lassen, Nummern speziell formatieren
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen in Excel in ein spezielles Format ist eine leistungsfähige Funktion, mit der Benutzer Zahlen in einer lesbareren, verständlicheren oder standardisierten Weise anzeigen können. Dies ist besonders nützlich in verschiedenen Szenarien wie Finanzberichterstattung, Datenanalyse und alltäglicher Tabellenkalkulation. Hier sind einige Gründe, warum Sie Zahlen in Excel speziell formatieren möchten:

1. **Verbesserte Lesbarkeit**: Spezielle Formatierungen machen Zahlen leichter lesbar und verständlich. Beispielsweise macht die Formatierung einer Nummer als Telefonnummer (z.B. (123) 456-7890) oder Sozialversicherungsnummer (z.B. 123-45-6789) diese sofort erkennbar und besser lesbar als einfache Ziffern.

2. **Konsistenz**: Das Anwenden eines speziellen Formats sorgt für Konsistenz Ihrer Daten, was für Berichte oder Datensätze, die geteilt oder in Präsentationen verwendet werden, entscheidend ist. Konsistente Zahlenformate helfen beim Vergleich von Daten und der Wahrung professioneller Standards.

3. **Dateninterpretation**: Bestimmte Formate erleichtern die schnelle Interpretation der Daten. Beispielsweise zeigt die Formatierung von Zahlen als Währung sofort finanzielle Werte an, während Prozentformate Verhältnisse oder Vergleiche hervorheben können, ohne dass zusätzliche Berechnungen oder Erklärungen erforderlich sind.

4. **Fehlerreduktion**: Durch die spezielle Formatierung von Zahlen können Fehler bei Dateneingabe oder -interpretation verringert werden. Beispiel: Das Formatieren einer Zelle zur Anzeige von Daten stellt sicher, dass alle Datumseinträge einer einheitlichen Struktur entsprechen, was Missverständnisse reduziert.

5. **Platzersparnis**: Spezielle Formate wie wissenschaftliche Notation können große Zahlen kompakter machen, was in der Tabelle Platz spart, ohne Informationen zu verlieren. Besonders nützlich bei sehr großen oder sehr kleinen Zahlen.

6. **Einhaltung von Standards**: In vielen Bereichen gibt es spezifische Standards, wie Zahlen dargestellt werden sollen (z.B. Buchhaltung, Wissenschaft, Technik). Spezielle Formate stellen sicher, dass Ihre Daten diesen Normen entsprechen.

7. **Bedingte Formatierung**: Über die statische Formatierung hinaus ermöglicht Excel bedingte Zahlenformatierungen, bei denen das Format je nach Wert der Zelle geändert wird (z.B. rot einfärben, wenn ein Budget überschritten wird). Dieser dynamische Ansatz hebt wichtige Informationen oder Trends hervor.

8. **Automatisierung und Effizienz**: Sobald Sie ein spezielles Format für eine Zelle oder einen Zellbereich eingerichtet haben, wendet Excel dieses Format automatisch auf neue eingegebene Daten an. Dies spart Zeit und sorgt für Einheitlichkeit, ohne dass manuelle Anpassungen notwendig sind.

Excel bietet eine Vielzahl vordefinierter spezieller Formate, darunter Währung, Buchhaltung, Datum, Uhrzeit, Telefonnummer, Postleitzahl und Sozialversicherungsnummer. Außerdem können benutzerdefinierte Nummernformate erstellt werden, wodurch die Flexibilität bei der Gestaltung von Formaten erhöht wird.

## **So formatieren Sie Nummern in Excel speziell**
Das spezielle Formatieren von Nummern in Excel ermöglicht es Ihnen, Zahlen auf eine lesbarere oder individuellere Art anzuzeigen, z.B. Telefonnummern, Postleitzahlen, Sozialversicherungsnummern oder andere spezifische Formate. So geht's:

### Mit integrierten speziellen Formaten

1. **Zellen auswählen**: Klicken Sie auf die Zelle oder den Zellbereich, den Sie formatieren möchten.
2. **Formatierungsdialog öffnen**: Rechtsklick auf die ausgewählten Zellen und „Zellen formatieren“ wählen oder `Strg` + `1` drücken, um den Dialog zu öffnen.
3. **Kategorie „Spezial“ wählen**: Im Dialog „Zellen formatieren“ gehen Sie auf die Registerkarte „Zahl“ und in der Kategorie-Liste auf „Spezial“.
4. **Format auswählen**: Sie sehen eine Liste vordefinierter Spezialformate wie PLZ, Telefonnummer und Sozialversicherungsnummer (je nach Region). Wählen Sie das passende aus.
5. **Übernehmen und OK**: Klicken Sie auf „OK“, um das gewählte Format anzuwenden.

### Benutzerdefinierte Formate erstellen

Wenn die integrierten Spezialformate nicht Ihren Bedürfnissen entsprechen, können Sie ein benutzerdefiniertes Format erstellen:

1. **Zellen auswählen**: Markieren Sie die Zelle oder den Bereich, den Sie formatieren möchten.
2. **Zellenformatierung öffnen**: Rechtsklick und „Zellen formatieren“ wählen oder `Strg` + `1` drücken.
3. **Zur Kategorie „Benutzerdefiniert“ wechseln**: Im Dialog „Zellen formatieren“ die Registerkarte „Zahl“ auswählen und dann in der Kategorie-Liste „Benutzerdefiniert“ wählen.
4. **Benutzerdefiniertes Format eingeben**: Im Typ-Feld den Code für das benutzerdefinierte Format eingeben. Zum Beispiel:
   - Für eine 10-stellige Telefonnummer könnten Sie verwenden: `(###) ###-####`
   - Für einen Produktcode, der mit zwei Buchstaben beginnt, gefolgt von drei Zahlen: `"XX"###`
5. **Anwenden und OK**: Klicken Sie auf „OK“, um Ihr benutzerdefiniertes Format zu übernehmen.

### Tipps für benutzerdefinierte Zahlenformate

- Verwenden Sie `#` für optionale Ziffern. Excel zeigt die Ziffer an, wenn sie vorhanden ist.
- Verwenden Sie `0` für einen Platzhalter für Ziffern, der Nullen anzeigt, wenn keine Zahl an dieser Stelle vorhanden ist.
- Verwenden Sie `?`, um Platz für unwichtige Nullen zu schaffen, diese jedoch nicht anzuzeigen. Dies kann helfen, Zahlen mit Dezimalstellen auszurichten.
- Text kann in benutzerdefinierte Formate eingeschlossen werden, indem man ihn in Anführungszeichen setzt.

### Beispiel für benutzerdefinierte Formatcodes

- **Sozialversicherungsnummer (SSN)**: `000-00-0000`
- **Telefonnummer (USA)**: `(###) ###-####`
- **Produktcode**: `"PRD-"0000`
- **Datum mit Text**: `"Tag" dd "von" mmmm, yyyy`

Denken Sie daran, dass die Funktion für benutzerdefinierte Formate sehr leistungsfähig ist und eine Vielzahl von Formatierungsoptionen über einfache Zahlenformate hinaus bietet. Sie können Bedingungen, Farben und mehr kombinieren, um Ihre Daten in Excel sehr individuell darzustellen.

## **Wie man Nummern in spezielle Form in Aspose.Cells for C++ formatiert**
In Aspose.Cells for C++ beinhaltet die Formatierung von Nummern in eine spezielle Form die Verwendung des `Style`-Objekts, das mit einer Zelle verbunden ist. Das `Style`-Objekt ermöglicht es, verschiedene Formatierungsoptionen zu spezifizieren, einschließlich Zahlenformate. Spezialzahlenformate können Formate wie Daten, Zeiten, Telefonnummern, Postleitzahlen oder beliebige benutzerdefinierte Zahlenformate umfassen.

Hier ist eine Schritt-für-Schritt-Anleitung, wie man eine Nummer in eine spezielle Form in Aspose.Cells for C++ formatiert:

### Schritt 1: Fügen Sie Aspose.Cells zu Ihrem Projekt hinzu

Stellen Sie zuerst sicher, dass Aspose.Cells for C++ in Ihr Projekt aufgenommen wurde. Sie können es über den NuGet Package Manager beziehen oder direkt von der Aspose-Website herunterladen.

Wenn Sie die NuGet Package Manager Console verwenden, können Sie es durch Ausführen des Befehls installieren:

```powershell
Install-Package Aspose.Cells.Cpp
```

### Schritt 2: Erstellen Sie eine Arbeitsmappe und greifen Sie auf ein Arbeitsblatt zu
Du kannst entweder eine neue Arbeitsmappe erstellen oder eine bestehende öffnen. 

### Schritt 3: Zugriff auf oder Hinzufügen von Daten in eine Zelle
Sie müssen auf das Arbeitsblatt zugreifen, auf dem Sie Zahlen auf spezielle Weise formatieren möchten. Wenn Sie mit einer neuen Arbeitsmappe arbeiten, sind Sie wahrscheinlich im ersten Arbeitsblatt.

### Schritt 4: Formatieren Sie die Zahl auf ein spezielles Format
Um eine Zelle so zu formatieren, dass ihre Zahl in spezieller Notation angezeigt wird, müssen Sie ihr benutzerdefiniertes Format einstellen.

### Schritt 5: Arbeitsmappe speichern
Nach der Formatierung der Zellen, wie erforderlich, vergessen Sie nicht, Ihre Arbeitsmappe zu speichern. Dadurch werden die Zellen in der gewünschten wissenschaftlichen Notation gespeichert.

### Benutzerdefinierte Zahlenformate

Mit der Eigenschaft `style.Custom` können Sie benutzerdefinierte Zahlenformate definieren. Hier sind einige Beispiele:

- **Telefonnummer:** `"(###) ###-####"`
- **Postleitzahl:** `"#####-####"`
- **Sozialversicherungsnummer:** `"###-##-####"`
- **Datumsformat:** `"yyyy-mm-dd"`

Sie können nahezu jedes Zahlenformat erstellen, indem Sie die Formatzeichenfolge entsprechend Ihren Bedürfnissen angeben.

### Beispielcode

Hier ist ein Codebeispiel, das diese Schritte zeigt:
```c++
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

    // Access the cell at the first row and first column (A1)
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set the value of the cell
    cell.PutValue(1234567890); // Example value

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the custom number format
    // For example, format as a phone number
    style.SetCustom(u"(###) ###-####");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"output.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Fazit

Das Formatieren von Nummern in spezielle Formate in Aspose.Cells for C++ beinhaltet das Setzen des benutzerdefinierten Zahlenformats einer Zelle. Dies ermöglicht eine Vielzahl von Formatierungsoptionen, sodass Sie Daten genau so anzeigen können, wie Sie es benötigen. Denken Sie daran, dass der Schlüssel zu benutzerdefinierten Formaten die Formatzeichenfolge ist, die Sie angeben, welche bestimmt, wie die Nummer angezeigt wird.
