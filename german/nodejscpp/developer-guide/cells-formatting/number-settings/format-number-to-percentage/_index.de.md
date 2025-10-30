---
title: Wie man Nummern in Prozentsätze formatiert
type: docs
weight: 10
url: /de/nodejs-cpp/how-to-format-number-to-percentage/
description: Dieser Artikel stellt vor, wie man Zahlen in Prozent mit Aspose.Cells for Node.js via C++ API formatiert.
keywords: Eine Zahl in Prozentsatz Format umwandeln, Numerische Werte in Prozentsätze transformieren, Zahlen als Prozentsätze anzeigen, Zahlen im Prozent Format formatieren, Numerische Werte auf Prozentdarstellung anpassen, Nummer in Prozent formatieren
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen in Prozentsätze in Excel ist eine gängige Praxis aus mehreren Gründen, die die Klarheit, Genauigkeit und Interpretierbarkeit der Daten verbessern. Hier sind einige der wichtigsten Gründe, warum du Zahlen in Excel als Prozentsätze formatieren solltest:

1. **Klarheit und Lesbarkeit**: Prozentsätze sind ein universell verständliches Format, das Daten leichter lesbar und interpretierbar macht. Durch die Umwandlung eines Dezimals oder Bruchs in einen Prozentsatz wird sofort deutlich, dass es sich um einen Teil eines Ganzen handelt, was für viele Nutzer intuitiver sein kann.

2. **Konsistenz**: Bei Berichten oder Datenanalysen, die Vergleiche aufstellen, sorgt die Formatierung von Zahlen als Prozentsätze für Konsistenz. Das ist besonders wichtig, wenn Sie Verhältnisse oder Anteile in verschiedenen Datensätzen vergleichen. Konsistenz in der Datenpräsentation hilft, genauere Vergleiche und Schlussfolgerungen zu ziehen.

3. **Vereinfachung**: Prozentsätze vereinfachen komplexe Informationen. Zum Beispiel ist „50%“ für die meisten Menschen verständlicher und einfacher zu erfassen als „0,5“ oder „1/2“. Diese Vereinfachung ist entscheidend, wenn Daten einem Publikum vermittelt werden, das keinen technischen Hintergrund hat.

4. **Visualisierung**: Beim Erstellen von Diagrammen oder Grafiken können Prozentsätze die Datenvisualisierung effektiver machen. Zum Beispiel stellen Kreisdiagramme inhärent Teile eines Ganzen dar und sind intuitiver, wenn die Daten als Prozentsätze formatiert sind.

5. **Analyse und Entscheidungsfindung**: In Business und Finanzen werden Prozentsätze häufig verwendet, um Wachstum, Gewinnmargen und andere wichtige Leistungskennzahlen (KPIs) darzustellen. Die Formatierung dieser Zahlen als Prozentsätze erleichtert die Analyse und die Entscheidungsfindung anhand klarer, verständlicher Metriken.

6. **Platzersparnis**: In einigen Fällen kann die Formatierung von Zahlen als Prozentsätze Platz in Ihrem Dokument oder Ihrer Tabelle sparen und es aufgeräumter aussehen lassen. Das ist besonders nützlich bei Tabellen oder Dashboards, bei denen der Platz knapp ist.

7. **Bildungs- und Unterrichtszwecke**: In Bildungseinrichtungen kann das Formatieren von Zahlen als Prozentsätze Schülern helfen, Brüche, Verhältnisse und Proportionen besser zu verstehen. Es ist eine praktische Anwendung mathematischer Konzepte.

Um eine Zahl in Excel als Prozentsatz zu formatieren, wählen Sie einfach die Zelle(n) mit Ihren Daten aus und wählen dann die Option „Prozent“ im Format, entweder im Reiter „Start“ im Menüband oder durch Rechtsklick und „Zellen formatieren“. Excel zeigt dann die Zahlen als Prozentsätze an, indem es die ursprünglichen Dezimalwerte mit 100 multipliziert und ein Prozentzeichen hinzufügt. Diese automatische Umwandlung erleichtert die oben genannten Zwecke und macht die Datenverwaltung sowie Präsentation effizient und wirkungsvoll.

## **So formatieren Sie eine Zahl in Excel als Prozentsatz**
Die Formatierung von Zahlen als Prozentsätze in Excel ist ein unkomplizierter Vorgang, der in wenigen Schritten erledigt werden kann. Hier ist die Anleitung:

### Mit dem Menüband

1. **Zellen auswählen**: Markieren Sie zunächst die Zelle oder den Zellbereich, den Sie als Prozentsatz formatieren möchten.
2. **Zum Menüband gehen**: Oben in Excel finden Sie das Menüband. Dort gibt es einen Reiter „Start“.
3. **Prozentsatz-Button**: Im Reiter „Start“ befindet sich innerhalb der Gruppe „Zahlen“ ein Button mit dem Symbol „%“. Das ist die Schaltfläche „Prozentformat“.
4. **Prozentformat anwenden**: Klicken Sie auf den „%“-Button. Excel formatiert die ausgewählten Zellen automatisch als Prozente, multipliziert den Zellwert mit 100 und zeigt das Prozentzeichen an. Wenn Sie beispielsweise „0,1“ in eine Zelle eingeben und das Prozentformat anwenden, wird es als „10%“ angezeigt.

### Mit dem Dialogfeld „Zellen formatieren“

1. **Zellen auswählen**: Markieren Sie die Zellen, die Sie formatieren möchten.
2. **Dialog „Zellen formatieren“ öffnen**: Rechtsklicken Sie auf eine der markierten Zellen und wählen Sie „Zellen formatieren“ aus dem Kontextmenü. Alternativ können Sie die Tastenkombination `Strg + 1` verwenden, um das Dialogfeld zu öffnen.
3. **Prozent auswählen**: Im Dialog „Zellen formatieren“ klicken Sie im Reiter „Zahlen“ auf „Prozent“, falls dieser nicht bereits ausgewählt ist.
4. **Dezimalstellen anpassen**: Sie können die Anzahl der Dezimalstellen einstellen, die angezeigt werden sollen. Wenn Sie beispielsweise zwei Dezimalstellen zeigen möchten, geben Sie „2“ bei „Dezimalstellen“ ein.
5. **OK klicken**: Bestätigen Sie mit „OK“. Die ausgewählten Zellen zeigen nun die Werte als Prozentsätze an.

### Mit einer Formel

Wenn Sie eine Formel eingeben oder eine bestehende Zahl in einer Formel in einen Prozentsatz umwandeln möchten, multiplizieren Sie die Zahl einfach mit 100 und fügen das Prozentzeichen zum Format hinzu.

Zum Beispiel, wenn Sie einen Wert in Zelle A1 haben und ihn in Zelle B1 als Prozentsatz anzeigen möchten, können Sie die folgende Formel in B1 verwenden:

```excel
=A1*100 & "%"
```

Beachten Sie jedoch, dass diese Methode das Ergebnis als Text behandelt und nicht als numerischen Wert, der als Prozentsatz formatiert ist, was Auswirkungen auf weitere Berechnungen haben kann.

### Tastenkürzel

Für eine schnelle Formatänderung ohne Maus:
- Wählen Sie die Zellen aus, die Sie formatieren möchten.
- Drücken Sie `Strg + Shift + %`. Damit wird das Prozentformat auf die markierten Zellen angewendet.

Denken Sie daran, wenn Sie eine Zahl als Prozentsatz formatieren, multipliziert Excel den Zellwert im Wesentlichen mit 100. Wenn Sie Daten eingeben, die als Prozentsatz angezeigt werden sollen, müssen Sie sie als Dezimalzahl eingeben (z.B. „0,1“ für 10%).

## **Wie man Nummer in Prozent in Aspose.Cells for Node.js via C++ formatiert**
Das Formatieren von Zahlen in Prozentsätze in Aspose.Cells for Node.js via C++ ist ein einfacher Vorgang. Aspose.Cells ist eine leistungsstarke Bibliothek, mit der Sie Excel-Dateien erstellen, bearbeiten und konvertieren können, ohne Microsoft Excel auf Ihrem System installiert zu haben. Hier erfahren Sie, wie Sie Zahlen in Prozentsätze mit Aspose.Cells for Node.js via C++ formatieren:

### Schritt 1: Aspose.Cells for Node.js via C++ installieren

Stellen Sie sicher, dass Aspose.Cells for Node.js via C++ in Ihrem Projekt referenziert wird.

### Schritt 2: Erstelle eine Neue Arbeitsmappe oder öffne eine Bestehende

Du kannst entweder eine neue Arbeitsmappe erstellen oder eine bestehende öffnen. 


### Schritt 3: Zugriff auf das Arbeitsblatt

Sie müssen auf das Arbeitsblatt zugreifen, auf dem Sie Zahlen in Prozentsätze formatieren möchten. Wenn Sie mit einer neuen Arbeitsmappe arbeiten, befinden Sie sich wahrscheinlich im ersten Arbeitsblatt.

### Schritt 4: Prozentformat anwenden

Um eine Zelle oder einen Zellbereich so zu formatieren, dass Zahlen als Prozentsätze angezeigt werden, müssen Sie das Zahlenformat der Zelle oder des Bereichs auf Prozentsatz setzen. Bei einem Zellbereich würden Sie durch den Bereich iterieren und das Format bei jeder Zelle einzeln anwenden.

### Schritt 5: Arbeitsmappe speichern

Speichern Sie schließlich die Arbeitsmappe in eine Datei oder einen Stream.

### Beispielcode

Hier ist ein Codebeispiel, das diese Schritte zeigt:
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToPercentage.js" >}}

### Fazit

Wenn Sie diese Schritte befolgen, können Sie Zahlen in Aspose.Cells for Node.js via C++ leicht in Prozentsätze umwandeln. Aspose.Cells bietet eine breite Palette von Funktionen zur Manipulation von Excel-Dateien, einschließlich Zellformatierung, Arbeit mit Formeln und vielem mehr – ein mächtiges Werkzeug für Node.js-Entwickler, die mit Excel-Daten arbeiten.

{{< app/cells/assistant language="nodejs-cpp" >}}
