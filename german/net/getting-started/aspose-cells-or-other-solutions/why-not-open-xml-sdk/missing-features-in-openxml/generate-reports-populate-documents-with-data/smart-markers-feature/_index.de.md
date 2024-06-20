---
title: Smart Markers Funktion in Aspose.Cells
type: docs
weight: 30
url: /de/net/smart-markers-feature-in-aspose-cells/
---

**Smart-Marker** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in ein Microsoft Excel-Designer-Tabellenblatt eingefügt werden sollen. Mit Smart Markers können Sie Vorlagen erstellen, die nur bestimmte Informationen und Formatierungen enthalten.
## **Designer-Tabelle & Intelligente Marker**
Designer-Tabellen sind Standard-Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Marker enthalten. Sie können intelligente Marker enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu relevanten Kontakten. Intelligente Marker werden in die Zellen geschrieben, in denen Sie die Informationen platzieren möchten.

Alle Smart Marker beginnen mit &=. Ein Beispiel für einen Datamarker ist &=Party.FullName. Wenn der Datamarker zu mehr als einem Element führt, beispielsweise einer vollständigen Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für alle neuen Informationen zu schaffen. So können Zwischensummen und Gesamtsummen in der Zeile unmittelbar nach dem Datamarker platziert werden, um Berechnungen auf Basis der eingefügten Daten durchzuführen. Verwenden Sie dynamische Formeln, um Berechnungen auf den eingefügten Zeilen durchzuführen.

Intelligente Marker bestehen aus den Teilen **Datenquelle** und **Feldname** für die meisten Informationen. Spezielle Informationen können auch mit Variablen und Variablenarrays übergeben werden. Variablen füllen immer nur eine Zelle aus, während Variablenarrays mehrere Zellen ausfüllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete intelligente Marker werden entfernt.

Smart-Marker können auch Parameter enthalten. Mit Parametern können Sie festlegen, wie die Informationen angeordnet werden sollen. Sie werden als kommagetrennte Liste in Klammern am Ende des Smart Markers angehängt.
### **Intelligente Marker-Optionen**
- &=Datenquelle.Feldname
- &=Datenquelle.Feldname
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parameter**
Folgende Parameter sind erlaubt:

- noadd - Fügen Sie keine zusätzlichen Zeilen hinzu, um die Daten anzupassen.
- skip:n - Überspringen Sie n Zeilen für jede Datensatzzeile.
- aufsteigend:n oder absteigend:n - Sortieren Sie die Daten in Smart-Markierungen.
- horizontal - Schreiben Sie die Daten von links nach rechts anstatt von oben nach unten.
- numerisch - Konvertieren Sie Text, wenn möglich, in eine Zahl.
- verschieben - Verschieben Sie nach unten oder rechts, erstellen Sie zusätzliche Zeilen oder Spalten, um die Daten anzupassen.
- kopierenstil - Kopieren Sie den Basiszellenstil in alle Zellen dieser Spalte.

Die Parameter **noadd** und skip können kombiniert werden, um Daten in abwechselnden Zeilen einzufügen.

Dieser Abschnitt umfasst die folgenden Themen

- [Gruppierung von Daten in Aspose.Cells](/cells/de/net/grouping-data-in-aspose-cells/)
- [Bildmarkierungen in Aspose.Cells](/cells/de/net/image-markers-in-aspose-cells/)
- [Verwenden von anonymen Typen oder benutzerdefinierten Objekten in Aspose.Cells](/cells/de/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Verwendung von verschachtelten Objekten in Aspose.Cells](/cells/de/net/using-nested-objects-in-aspose-cells/)
