---
title: Wie man Nummern in Bruchzahlen mit C++ formatiert
linktitle: Wie man Nummern in Bruchzahlen formatiert
type: docs
weight: 10
url: /de/cpp/how-to-format-number-to-fraction/
description: Dieser Artikel führt ein, wie man Zahlen mit der Aspose.Cells for C++ API in Bruchzahlen umwandelt.
keywords: Wandle eine Zahl in eine Bruchdarstellung um, Vorgang, bei dem eine Ziffer in deren Bruchäquivalent umgewandelt wird, Ändere eine Zahl in ihre entsprechende Bruchform, Formatieren eines numerischen Werts in einen Bruch, Eine Zahl als Bruch darstellen, Zahl zu Bruchformat konvertieren
---

## **Mögliche Verwendungsszenarien**
Die Formatierung von Zahlen als Brüche in Excel ist aus mehreren Gründen nützlich, insbesondere wenn Sie mit Daten arbeiten, die natürlicherweise in Bruchform ausgedrückt werden, oder wenn Sie Operationen ausführen müssen, die Brüche erfordern. Hier sind einige der wichtigsten Gründe, warum Sie Zahlen in Excel als Brüche formatieren möchten:

1. **Klarheit und Präzision**: Brüche können manchmal Informationen klarer und präziser vermitteln als Dezimalzahlen. Zum Beispiel sind in Rezepten oder Messungen 1/2 Tasse oder 3/4 Zoll intuitiver als 0,5 Tasse oder 0,75 Zoll. Das Formatieren von Zahlen als Brüche kann die Daten für bestimmte Zielgruppen leichter lesbar und verständlich machen.

2. **Genauigkeit**: Bei der Arbeit mit exakten Werten können Brüche Mengen genauer darstellen als Dezimalzahlen, die gerundet werden müssen. Zum Beispiel kann 1/3 nicht exakt als Dezimalzahl dargestellt werden, aber genau als Bruch ausgedrückt werden.

3. **Mathematische Operationen**: In manchen Fällen müssen Sie mathematische Operationen mit Brüchen durchführen, und die Beibehaltung der Zahlen im Bruchformat kann diese Operationen einfacher machen. Zum Beispiel ist das Addieren von 1/2 und 1/4 für viele Menschen intuitiver als das Addieren von 0,5 und 0,25, insbesondere wenn Sie die Mathematik ohne Taschenrechner machen.

4. **Bildungszwecke**: Beim Unterrichten oder Lernen über Brüche ist es vorteilhaft, mit tatsächlichen Brüchen zu arbeiten, anstatt deren Dezimaläquivalente zu verwenden. Die Fähigkeit von Excel, Zahlen als Brüche zu formatieren, ist ein wertvolles Werkzeug in Bildungseinrichtungen.

5. **Branchenstandards**: Bestimmte Branchen oder Berufe bevorzugen oder erfordern die Verwendung von Brüchen statt Dezimalzahlen. Beispielsweise verwenden Bauwesen, Tischlerarbeiten und Kochkunst oft Bruchmessungen. Die Verwendung von Brüchen in Excel kann helfen, die Konsistenz mit Branchenstandards zu bewahren.

6. **Optische Anziehungskraft**: In einigen Dokumenten oder Präsentationen sind Brüche optisch ansprechender oder passender als Dezimalzahlen. Dies ist besonders bei formellen Dokumenten, Berichten oder beim Versuch, einen bestimmten Formatstil einzuhalten, der Fall.

Excel macht es einfach, Zahlen als Brüche zu formatieren, und bietet mehrere Bruchformate zur Auswahl, einschließlich einzelner Ziffern, Brüche mit bis zu zwei Ziffern und sogar als eingegebene Brüche. Diese Flexibilität ermöglicht es den Nutzern, ihre Daten in der passendsten und verständlichsten Weise für ihre spezifischen Bedürfnisse zu präsentieren.

## **So formatieren Sie eine Zahl als Bruch in Excel**
Das Formatieren von Zahlen als Brüche in Excel ist ein unkomplizierter Vorgang, der es ermöglicht, Ihre Daten auf eine bedeutungsvollere Weise darzustellen, insbesondere wenn es sich um Mengen handelt, die keine Ganzzahlen sind. Hier erfahren Sie, wie Sie Zahlen in Excel als Bruch formatieren können:

### Mit dem Dialogfeld „Zellen formatieren“

1. **Zellen auswählen**: Wählen Sie zunächst die Zellen aus, die Sie als Brüche formatieren möchten. Sie können mehrere Zellen durch Klick und Ziehen auswählen oder auf eine einzelne Zelle klicken, wenn nur eine formatiert werden soll.

2. **Dialogfeld Zellen formatieren öffnen**: Klicken Sie mit der rechten Maustaste auf eine der ausgewählten Zellen und wählen Sie im Kontextmenü `Zellen formatieren`. Alternativ können Sie `Strg + 1` drücken, um das Dialogfeld „Zellen formatieren“ zu öffnen.

3. **Bruchformat auswählen**: Im Dialogfeld „Zellen formatieren“ gehen Sie zum Tab `Zahl`. Auf der linken Seite sehen Sie eine List der Kategorien. Wählen Sie `Bruch`.

4. **Bruchtyp wählen**: Auf der rechten Seite, unter dem Abschnitt `Typ`, sehen Sie verschiedene Bruchformate. Excel bietet mehrere vordefinierte Bruchformate, darunter:
   - Bis zu einer Ziffer (1/4)
   - Bis zu zwei Ziffern (21/25)
   - Bis zu drei Ziffern (312/943)
   - Als Halbe (1/2)
   - Als Viertel (2/4)
   - Als Achtel (4/8)
   - Als Sechzehntel (8/16)
   - Als Zehntel (3/10)
   - Als Hundertstel (30/100)

   Wählen Sie dasjenige, das am besten zu Ihren Daten passt. Wenn Sie unsicher sind, ist „Bis zu einer Ziffer (1/4)“ eine gute allgemeine Wahl für viele Anwendungen.

5. **Format anwenden**: Nach der Auswahl des gewünschten Bruchformats klicken Sie auf `OK`, um das Format auf die ausgewählten Zellen anzuwenden.

### Mit dem Menüband

Alternativ können Sie auch das Menüband verwenden, um schnell einige Bruchformate anzuwenden:

1. **Zellen auswählen**: Wählen Sie die Zellen aus, die Sie formatieren möchten.

2. **Zur Startseite Tab gehen**: Auf dem Ribbon, gehe zum `Home`-Tab.

3. **Nummerformat Dropdown öffnen**: In der Gruppe `Number` findest du ein Dropdown für Zahlenformate. Klicke darauf.

4. **Bruch wählen**: Du wirst im Dropdown einige gängige Formate sehen, einschließlich einiger Bruchoptionen. Wenn das gewünschte Bruchformat angezeigt wird, kannst du es direkt hier auswählen. Falls nicht, wähle `Weitere Zahlenformate…` am unteren Rand der Liste und folge den Schritten im Abschnitt Zellen formatieren oben.

### Tipps

- **Benutzerdefinierte Brüche**: Wenn die vordefinierten Bruchformate nicht ausreichen, kannst du ein benutzerdefiniertes Bruchformat erstellen, indem du `Benutzerdefiniert` im Dialogfeld Zellen formatieren auswählst und deinen benutzerdefinierten Formatcode eingibst.
- **Genauigkeit**: Wenn du eine Zahl als Bruch formatierst, wandelt Excel die Zahl in den nächstgelegenen Bruch um, basierend auf dem gewählten Format. Dies ist möglicherweise nicht immer perfekt genau für komplexe Brüche oder Dezimalzahlen mit vielen Stellen.

Wenn du diese Schritte befolgst, kannst du Zahlen in Excel effektiv als Brüche formatieren und deine Daten leichter lesbar und interpretierbar machen.

## **Wie man Nummern in Aspose.Cells for C++ in Brüche umwandelt**
Das Formatieren von Zahlen in Brüche in Aspose.Cells for C++ ist ein einfacher Prozess. Aspose.Cells ist eine leistungsfähige Bibliothek, die es ermöglicht, mit Excel-Dateien in C++-Anwendungen zu arbeiten, ohne Microsoft Excel installiert zu haben. Es bietet eine breite Palette an Funktionen, einschließlich der Formatierung von Zahlen als Brüche.

Hier ist eine Schritt-für-Schritt-Anleitung, wie man Zahlen in Aspose.Cells for C++ in Brüche formatiert:

### Schritt 1: Aspose.Cells for C++ installieren

Stelle zunächst sicher, dass du Aspose.Cells for C++ in deinem Projekt installiert hast. Du kannst die Bibliothek von der [Aspose.Cells for C++](https://www.aspose.com/products/cells/cpp) Website herunterladen.

### Schritt 2: Erstelle eine Neue Arbeitsmappe oder öffne eine Bestehende

Du kannst entweder eine neue Arbeitsmappe erstellen oder eine bestehende öffnen.

### Schritt 3: Zugriff auf das Arbeitsblatt

Du musst auf das Arbeitsblatt zugreifen, in dem du Zahlen als Brüche formatieren möchtest. Falls du mit einer neuen Arbeitsmappe arbeitest, wirst du wahrscheinlich mit dem ersten Arbeitsblatt arbeiten.

### Schritt 4: Anwendung des Bruch-Nummernformats

Um eine Zelle als Bruch zu formatieren, musst du ihre Eigenschaft `Style.Number` auf einen bestimmten Zahlenformatcode setzen. Aspose.Cells unterstützt verschiedene Bruchformate wie "1/2", "1/4", "2/4" usw.

### Schritt 5: Arbeitsmappe speichern

Nachdem du das Bruchformat angewendet hast, speichere die Arbeitsmappe in einer Datei:

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell you want to format
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set the cell value
    cell.PutValue(0.5);

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the number format to fraction (e.g., "# ?/?")
    style.SetCustom(u"# ?/?");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

### Zusätzliche Hinweise

- Die Eigenschaft `Custom` des Style-Objekts ermöglicht es, das genaue Bruchformat anzugeben. Zum Beispiel kann `"# ??/???"` Brüche mit bis zu drei Stellen im Nenner anzeigen.
- Aspose.Cells unterstützt eine breite Palette von Zahlenformaten, einschließlich Dezimal, Prozentsatz, Währung und mehr. Du kannst das Format an deine spezifischen Anforderungen anpassen.

Wenn du diese Schritte befolgst, kannst du Zahlen in Aspose.Cells for C++ leicht als Brüche formatieren. Dies ist besonders nützlich in Finanz-, Statistik- oder Bildungsanwendungen, bei denen präzise Bruchwerte notwendig sind.
