---
title: So formatieren Sie Zahlen als Buchhaltung mit C++
linktitle: So formatieren Sie Zahlen als Buchhaltung
type: docs
weight: 10
url: /de/cpp/how-to-format-number-to-accounting/
description: Dieser Artikel zeigt, wie man Zahlen mithilfe der Aspose.Cells for C++ API in die Buchhaltungsformate umwandelt.
keywords: Numerische Werte in ein Buchhaltungsformat umwandeln, Buchhaltungsformat auf numerische Daten anwenden, Zahlen in eine buchhalterische Darstellung umwandeln, Zahlen gemäß Buchhaltungsstandards formatieren, Numerische Einträge an das Buchhaltungsformat anpassen, Zahlen in Buchhaltung
---

## **Mögliche Verwendungsszenarien**
Zahlenformatierung in Excel in das Buchhaltungsformat ist eine gängige Praxis, insbesondere in Geschäfts-, Finanz- und Buchhaltungsbereichen. Dieses Format bietet eine standardisierte Art der Darstellung numerischer Daten, was das Lesen, Verstehen und Vergleichen erleichtert. Hier sind einige Hauptgründe, warum Sie Zahlen in Excel in das Buchhaltungsformat umwandeln sollten:

1. **Einheitlichkeit und Professionalität**: Das Buchhaltungsformat richtet Währungszeichen und Dezimalpunkte in einer Spalte aus und sorgt für einen sauberen, professionellen Eindruck. Diese Einheitlichkeit hilft, finanzielle Daten in einer strukturierteren und ansprechenderen Weise darzustellen, was für Berichte und Präsentationen wesentlich ist.

2. **Klarheit und Präzision**: Durch die Anzeige von Zahlen in einem einheitlichen Format, einschließlich der Verwendung von Kommas für Tausende und der Angabe der Dezimalstellen, erhöht das Buchhaltungsformat die Klarheit und Präzision. Dies ist besonders wichtig bei Finanzanalysen und Entscheidungsfindungen, bei denen Genauigkeit oberste Priorität hat.

3. **Negative Zahlen**: Das Buchhaltungsformat stellt negative Zahlen in Klammern dar, anstatt ein Minuszeichen zu verwenden. Diese Konvention ist in der Buchhaltung und im Finanzwesen weit verbreitet, um negative Werte deutlicher hervorzuheben und das Übersehen zu verringern.

4. **Nullwerte**: Im Buchhaltungsformat werden Nullwerte häufig als Bindestrich (-) dargestellt, anstelle der Zahl 0. Dies kann helfen, zwischen Nullwerten und leeren oder nicht ausgefüllten Zellen zu unterscheiden, was die Datenklarheit verbessert.

5. **Währungssymbol**: Das Buchhaltungsformat erlaubt die direkte Einbindung eines Währungssymbols in die Zelle mit der Zahl. Dies ist in Finanzdokumenten besonders nützlich, um die Währung der Beträge anzugeben, insbesondere in internationalen Kontexten mit mehreren Währungen.

6. **Vergleichbarkeit**: Wenn Finanzdaten konsequent im Buchhaltungsformat formatiert werden, ist es einfacher, Zahlen in verschiedenen Zeilen, Spalten oder sogar in verschiedenen Dokumenten zu vergleichen. Dies unterstützt die Analyse von Trends, Prognosen und die Erkennung von Diskrepanzen.

7. **Einhaltung von Standards**: In vielen Fällen ist die Verwendung des Buchhaltungsformats keine reine Präferenz, sondern eine Anforderung. Bestimmte Finanzberichtsstandards und -praktiken verlangen die Verwendung dieses Formats für die Darstellung von Finanzberichten und anderen Buchhaltungsdokumenten.

Zusammenfassend ist das Formatieren von Zahlen in Excel in das Buchhaltungsformat eine wichtige Praxis für jeden, der mit Finanzdaten arbeitet. Es verbessert die Präsentation, Klarheit und Nutzbarkeit numerischer Informationen, was für eine effektive Analyse, Berichterstattung und Entscheidungsfindung im Geschäfts- und Finanzbereich unerlässlich ist.

## **So formatieren Sie Zahlen in Excel in das Buchhaltungsformat**
Das Formatieren von Zahlen in das Buchhaltungsformat in Excel ist ein einfacher Prozess. Das Buchhaltungsformat richtet Währungszeichen und Dezimalpunkte in einer Spalte aus und macht es so einfacher, Finanzberichte zu lesen. Es zeigt auch negative Zahlen in Klammern an. So formatieren Sie Zahlen in Excel in das Buchhaltungsformat:

### Mit dem Menüband

1. **Zellen auswählen**: Wählen Sie zunächst die Zellen oder den Zellbereich aus, den Sie formatieren möchten.
2. **Zellenformatierungsdialog öffnen**: 
   - Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie `Zellen formatieren`, oder
   - Gehen Sie im Menüband auf die Registerkarte `Start`, suchen Sie die Gruppe `Zahl` und klicken Sie auf den kleinen Pfeil in der rechten unteren Ecke, um das Dialogfeld `Zellen formatieren` zu öffnen. Alternativ können Sie `Strg + 1` drücken, um das Dialogfeld direkt zu öffnen.
3. **Buchhaltungsformat auswählen**:
   - In der `Zellen formatieren`-Dialogbox, klicken Sie auf die Registerkarte `Zahl`.
   - Wählen Sie in der Liste auf der linken Seite `Buchhaltung`.
   - Sie können dann die gewünschten Einstellungen auswählen, z.B. das Symbol für Ihre Währung und die Anzahl der Dezimalstellen, die angezeigt werden sollen.
   - Klicken Sie auf `OK`, um die Formatierung anzuwenden.

### Verwendung der Schnellzugriffsschaltflächen im Menüband

Für eine schnellere Methode können Sie auch die Schnellzugriffsschaltflächen im Menüband verwenden:

1. **Zellen auswählen**: Markieren Sie die Zellen, die Sie formatieren möchten.
2. **Zum Start-Tab wechseln**: Im Menüband auf dem `Start`-Tab sehen Sie in der Gruppe `Zahl` ein Dropdown für Zahlenformate.
3. **Buchhaltungsformat auswählen**: Klicken Sie auf das Dropdown und wählen Sie `Buchhaltungszahlformat`. Dies wendet automatisch das Standard-Buchhaltungsformat auf die ausgewählten Zellen an.

### Anpassung des Buchhaltungsformats

Wenn Sie eine bestimmte Art von Buchhaltungsformat benötigen (zum Beispiel ohne Währungssymbol oder mit einer anderen Anzahl an Dezimalstellen), können Sie es anpassen:

1. **Zellen formatieren-Dialog öffnen**: Folgen Sie den oben genannten Schritten, um den `Zellen formatieren`-Dialog zu öffnen.
2. **Buchhaltung auswählen und anpassen**: Nach der Auswahl von `Buchhaltung`, passen Sie die Dezimalstellen an oder wählen Sie ein anderes Symbol. Wenn Sie kein Symbol möchten, wählen Sie `Keine`.

### Verwendung des Buchhaltungsformats in Excel vs. benutzerdefiniertes Zahlenformat

Während das Buchhaltungsformat für Finanzberichte geeignet ist und die Währungssymbole sowie Dezimalstellen ausrichtet, benötigen Sie manchmal mehr Anpassungsmöglichkeiten. In solchen Fällen können Sie das `Benutzerdefiniert`-Zahlenformat (im `Zellen formatieren`-Dialog unter der Registerkarte `Zahl`) verwenden. Damit können Sie ein Format erstellen, das genau Ihren Anforderungen entspricht, allerdings erfordert dies Grundkenntnisse der benutzerdefinierten Excel-Formatcodes.

### Fazit

Das Nummern im Buchhaltungsformat in Excel zu formatieren, hilft, Finanzdaten klarer und professioneller zu präsentieren. Egal ob bei der Erstellung von Finanzberichten oder der Budgetverwaltung, das Buchhaltungsformat kann Ihre Daten leichter lesbar und verständlich machen.

## **Wie man Nummern in Aspose.Cells for C++ im Buchhaltungsformat formatiert**
Um Nummern in Aspose.Cells for C++ im Buchhaltungsformat zu formatieren, können Sie das `Stil`-Objekt verwenden, das einer Zelle oder einem Zellbereich zugeordnet ist. Das `Stil`-Objekt ermöglicht die Einstellung verschiedener Formatierungsoptionen, einschließlich Zahlenformate. Das Buchhaltungsformat hat typischerweise einen Formatcode, der je nach Anforderungen variieren kann (z.B. Anzeige von Währungssymbolen, Dezimalstellen usw.).

Hier ein einfaches Beispiel, wie man ein Buchhaltungszahlformat auf eine Zelle in Aspose.Cells for C++ anwendet:

1. **Referenzieren Sie Aspose.Cells**: Stellen Sie sicher, dass Sie Aspose.Cells for C++ in Ihrem Projekt referenzieren. Sie können es über NuGet oder die Aspose-Website erhalten.

2. **Erstellen oder öffnen Sie eine Arbeitsmappe**: Beginnen Sie mit der Erstellung einer neuen Arbeitsmappe oder dem Öffnen einer bestehenden.

3. **Zugriff auf die gewünschte Zelle**: Identifizieren und greifen Sie auf die Zelle oder den Zellbereich zu, den Sie formatieren möchten.

4. **Anwenden des Buchhaltungsformats**: Legen Sie das Zahlenformat des Zellenstils auf ein Buchhaltungsformat fest.

4. **Beispielcode**: Hier ein Codeausschnitt, der diese Schritte demonstriert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook or load an existing one
    Workbook workbook;

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access a specific cell, for example, cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Put some numeric value in the cell
    cell.PutValue(1234.56);

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the number format to accounting.
    // The format code "_(\$* #,##0.00_);_(\$* (#,##0.00);_(\$* \"-\"??_);_(@_)" is an example for US currency.
    // You might need to adjust the format code according to your specific requirements and locale.
    style.SetCustom(u"_($* #,##0.00_);_($* (#,##0.00);_($* \"-\"??_);_(@_)");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"FormattedWorkbook.xlsx");

    std::cout << "Workbook formatted and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Dieses Beispiel zeigt, wie man eine einzelne Zelle so formatiert, dass Zahlen im US-Dollar-Buchhaltungsformat angezeigt werden. Der Formatstring kann angepasst werden, um verschiedene Währungssymbole oder Buchhaltungsformate zu erfüllen. Der Schlüssel liegt im `style.Custom`-Eigenschaft, wo Sie den benutzerdefinierten Zahlformatcode für Buchhaltung angeben.

Denken Sie daran, dass der genaue Formatstring je nach Locale und den spezifischen Anforderungen an das Buchhaltungsformat angepasst werden muss (z.B. Verwendung eines anderen Währungssymbols, mehr oder weniger Dezimalstellen anzeigen usw.).
