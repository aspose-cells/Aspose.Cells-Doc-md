---
title: Wie man Zahl in Zeit formatieren
type: docs
weight: 10
url: /de/nodejs-cpp/how-to-format-number-to-time/
description: Dieser Artikel zeigt, wie man Zahlen in Zeitformat mit der API Aspose.Cells for Node.js via C++ formatiert.
keywords: Numerische Werte in Zeitformat umwandeln, Ziffern in eine Zeitdarstellung transformieren, Zahlen in ein lesbares Zeitformat ändern, numerische Daten in Zeitnotierung formatieren, numerischen Input an eine Zeitstruktur anpassen, Zahl in Zeitformat
---

## **Mögliche Verwendungsszenarien**
Das Formatieren von Zahlen in Zeit in Excel ist eine gängige Praxis aus mehreren Gründen, vor allem weil es den Benutzern erlaubt, Daten auf eine verständliche und analysierbare Weise darzustellen. Hier sind einige der wichtigsten Gründe, warum Sie Zahlen in Excel in Zeit umwandeln möchten:

1. **Datenrepräsentation**: Das Zeitformat hilft dabei, Zahlen in einem vertrauten Zeitformat (Stunden, Minuten, Sekunden) darzustellen, was die Interpretation der Daten erleichtert. Zum Beispiel macht die Darstellung "6.5" als "6:30" deutlich, dass es sich um 6 Stunden und 30 Minuten handelt.

2. **Datenanalyse**: Beim Umgang mit zeitbasierten Daten wie Dauer, Arbeitszeiten oder Ereigniszeiten ermöglicht die Formatierung von Zahlen zu Zeit eine einfachere Analyse. Es erleichtert die Berechnung von Summen, Durchschnitten und Differenzen. Zum Beispiel wird die Summe von Zeitdauern für ein Projekt oder die durchschnittliche aufgewendete Zeit für Aufgaben intuitiver.

3. **Konsistenz**: Durch die Anwendung des Zeitformats wird sichergestellt, dass alle zeitbezogenen Daten im Dokument einheitlich sind, was sowohl für die Präsentation als auch für die Analyse von Vorteil ist. Konsistenz in der Datenpräsentation vermeidet Verwirrung und lässt Ihre Daten professionell aussehen.

4. **Kompatibilität mit Zeitfunktionen**: Excel bietet eine Reihe von Funktionen, die speziell für die Arbeit mit zeitformatierten Daten entwickelt wurden, wie `NETWORKDAYS`, `HOUR`, `MINUTE` und `SECOND`. Die Formatierung Ihrer Zahlen als Zeitwerte stellt die Kompatibilität mit diesen Funktionen sicher und ermöglicht komplexe zeitbasierte Berechnungen und Analysen.

5. **Visuelle Attraktivität und Klarheit**: Zeitformatierte Daten können in Verbindung mit bedingter Formatierung und Diagrammfunktionen von Excel verwendet werden, um visuell ansprechende und informative Berichte und Dashboards zu erstellen. Zum Beispiel können Sie Zeitwerte hervorheben, die einen bestimmten Schwellenwert überschreiten, oder Zeittrends über einen Zeitraum visualisieren.

6. **Fehlerreduzierung**: Durch die Formatierung von Zahlen als Zeit können Sie das Missverständnis von Daten reduzieren. Zum Beispiel weist "7:45" eindeutig auf 7 Stunden und 45 Minuten hin, während "7.75" von jemandem, der mit dem Kontext nicht vertraut ist, möglicherweise als 7 Stunden und 75 Minuten missinterpretiert wird.

7. **Einfache Eingabe**: Beim Eingeben zeitbasierter Daten ermöglicht das Formatieren der Zellen als Zeit eine natürlichere Eingabe. Benutzer können "1:30" eingeben, anstatt das Dezimaläquivalent von 1 Stunde und 30 Minuten zu berechnen, was "1.5" ist.

Zusammenfassend verbessert die Formatierung von Zahlen in Zeit in Excel die Datenrepräsentation, Analyse und Konsistenz, was die Arbeit mit zeitbasierten Daten erleichtert. Es nutzt die integrierten Funktionen von Excel für Zeitberechnungen und verbessert die allgemeine Benutzererfahrung, indem es Daten zugänglicher und verständlicher macht.

## **Wie man Zahl in Zeit in Excel formatiert**
Das Formatieren von Zahlen in Zeit in Excel kann auf verschiedene Weisen erfolgen, abhängig vom Format Ihrer Ausgangsdaten und vom gewünschten Ergebnis. Hier sind einige gängige Szenarien und wie Sie sie handhaben können:

### Szenario 1: Stunden im Dezimalformat in Zeit umwandeln

Wenn Sie eine Zahl haben, die Stunden im Dezimalformat darstellt (z.B. 1.5 für eine Stunde und dreißig Minuten), und diese in ein Zeitformat umwandeln möchten:

1. **Geben Sie Ihre Dezimalstunden** in eine Zelle ein (z.B. `1,5`).
2. **Rechtsklick** auf die Zelle und wählen Sie **Zellen formatieren**.
3. Im Dialogfeld **Zellen formatieren** gehen Sie zum Reiter **Zahlen**.
4. Wählen Sie **Uhrzeit** aus der Kategorienliste.
5. Wählen Sie ein Zeitformat, das Ihren Anforderungen entspricht, und klicken Sie auf **OK**.

Bei Dezimalstunden behandelt Excel den Wert als Bruchteil eines 24-Stunden-Tages. Also wird `1,5` als `36:00` (36 Stunden) formatiert, wenn Sie ein Format wählen, das Stunden über 24 hinaus einschließt.

### Szenario 2: Text oder Zahlen in Zeit umwandeln

Wenn Sie eine als Text oder Zahl ohne Dezimal dargestellte Zeit haben (z.B. `130` für 1:30 oder `1530` für 15:30), müssen Sie diese zunächst in eine Zeit-Seriennummer umwandeln, die Excel erkennen kann, bevor Sie ein Zeitformat anwenden.

1. **Angenommen, Ihre Zeit befindet sich in Zelle A1** und ist im Format `hhmm` (z.B. `1530`), dann können Sie die folgende Formel verwenden, um sie in eine Zeit umzuwandeln:
   ```excel
   =TIME(LEFT(A1,LEN(A1)-2), RIGHT(A1,2), 0)
   ```
   Für Formate ohne führende Nullen (z.B. `130` für 1:30) benötigen Sie möglicherweise eine leicht angepasste Formel, um die Variabilität in der Länge zu berücksichtigen:
   ```excel
   =TIME(VALUE(LEFT(A1, LEN(A1)-2)), VALUE(RIGHT(A1,2)), 0)
   ```
2. Nach Anwendung der Formel **Rechtsklick** auf die Zelle mit dem Formel-Ergebnis, wählen Sie **Zellen formatieren**, gehen Sie zum **Zahl**-Tab, wählen Sie **Uhrzeit**, wählen Sie Ihr gewünschtes Format und klicken Sie auf **OK**.

### Szenario 3: Eine Anzahl von Sekunden in das Zeitformat umwandeln

Wenn Sie eine Zahl haben, die Sekunden darstellt und diese in das Zeitformat umwandeln möchten:

1. **Geben Sie Ihre Sekunden** in eine Zelle ein (z.B. `3661` für eine Stunde, eine Minute und eine Sekunde).
2. Verwenden Sie die Formel `=A1/86400`, um Sekunden in die Seriennummer von Excel umzuwandeln (da es 86.400 Sekunden an einem Tag gibt). Ersetzen Sie `A1` durch die Zelle mit Ihren Sekunden.
3. **Rechtsklick** auf die Zelle mit der Formel, wählen Sie **Zellen formatieren**, gehen Sie zum **Zahl**-Tab, wählen Sie **Uhrzeit**, wählen Sie Ihr gewünschtes Format und klicken Sie auf **OK**.

### Zusätzliche Tipps

- Excel speichert Daten und Zeiten als Seriennummern. Für Daten zählt es die Tage ab dem 1. Januar 1900. Für Zeiten entspricht der Dezimalanteil der Zahl der Tageszeit.
- Sie können Zeitformate anpassen, indem Sie im **Zellen formatieren**-Dialog die Option **Benutzerdefiniert** wählen und Ihren eigenen Formatcode eingeben (z.B. `hh:mm:ss AM/PM`).
- Stellen Sie stets sicher, dass Ihre Daten konsistent sind, um unerwartete Ergebnisse beim Anwenden von Formeln oder Formatierungen zu vermeiden.

Indem Sie diese Schritte befolgen und je nach Ihren spezifischen Daten und Bedürfnissen anpassen, können Sie Zahlen in Excel effektiv als Zeit formatieren.

## **Wie man Zahlen in Zeit in Aspose.Cells for Node.js via C++ formatiert**
Das Formatieren von Zahlen in Zeit in Aspose.Cells for Node.js via C++ ist ein einfacher Vorgang, der das Anwenden eines benutzerdefinierten Zahlenformats auf eine Zelle oder einen Zellbereich umfasst. Aspose.Cells ist eine leistungsfähige Bibliothek, mit der Sie in Node.js-Anwendungen mit Excel-Dateien arbeiten können, ohne Microsoft Excel installiert zu haben. Hier erfahren Sie, wie es geht:

### Schritt 1: Aspose.Cells installieren

Stellen Sie sicher, dass Aspose.Cells for Node.js via C++ in Ihrem Projekt referenziert wird.

### Schritt 2: Erstelle eine Neue Arbeitsmappe oder öffne eine Bestehende

Du kannst entweder eine neue Arbeitsmappe erstellen oder eine bestehende öffnen.

### Schritt 3: Zugriff auf das Arbeitsblatt

Sie müssen auf das Arbeitsblatt zugreifen, in dem Sie Zahlen in Zeit umwandeln möchten. Wenn Sie mit einer neuen Arbeitsmappe arbeiten, befinden Sie sich wahrscheinlich im ersten Blatt.

### Schritt 4: Zeitformat auf eine Zelle anwenden

Um eine Zahl als Zeit zu formatieren, verwenden Sie das `Style`-Objekt, das mit einer Zelle verknüpft ist. Sie können das Zeitformat mit benutzerdefinierten Formatstrings festlegen. Hier ein Beispiel, um eine Zelle im Format Stunden und Minuten anzuzeigen.

### Schritt 5: Arbeitsmappe speichern

Nachdem Sie die gewünschten Formate angewendet haben, vergessen Sie nicht, Ihre Arbeitsmappe zu speichern.

### Benutzerdefinierte Zeitformate

Sie können je nach Bedarf verschiedene benutzerdefinierte Formate verwenden. Hier einige Beispiele:

- `"HH:MM"`: Stunden und Minuten
- `"HH:MM:SS"`: Stunden, Minuten und Sekunden
- `"HH:MM AM/PM"`: Stunden und Minuten mit AM oder PM

### Beispielcode

Hier ist ein Codebeispiel, das diese Schritte zeigt:
{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FormatNumberToTime.js" >}}

### Fazit

Das Formatieren von Zahlen in Zeit in Aspose.Cells for Node.js via C++ beinhaltet das Setzen eines benutzerdefinierten Zahlenformats für die Zellen, in denen die Zeit angezeigt werden soll. Wenn Sie die oben genannten Schritte befolgen, können Sie leicht Zeitformate auf Zellen in Ihren Excel-Dateien mit Aspose.Cells anwenden. Wichtig ist, das richtige benutzerdefinierte Format zu verwenden, das Ihrem gewünschten Zeitformat entspricht.

{{< app/cells/assistant language="nodejs-cpp" >}}
