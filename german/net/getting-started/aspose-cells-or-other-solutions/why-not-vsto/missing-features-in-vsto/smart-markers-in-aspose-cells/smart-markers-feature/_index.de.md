---
title: Smart-Marker-Funktion
type: docs
weight: 30
url: /de/net/smart-markers-feature/
---
**Intelligente Markierungen** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in einer Microsoft Excel-Designertabelle platziert werden sollen. Mit intelligenten Markierungen können Sie Vorlagen erstellen, die nur bestimmte Informationen und Formatierungen enthalten.
## **Designer-Tabellenkalkulation und intelligente Markierungen**
Designer-Arbeitsblätter sind standardmäßige Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Markierungen enthalten. Sie können intelligente Markierungen enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu verwandten Kontakten. Intelligente Markierungen werden in die Zellen geschrieben, in denen Sie die Informationen wünschen.

Alle intelligenten Markierungen beginnen mit &=. Ein Beispiel für eine Datenmarkierung ist &=Party.FullName. Wenn die Datenmarkierung mehr als ein Element ergibt, z. B. eine vollständige Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für alle neuen Informationen zu schaffen. Somit können Zwischensummen und Gesamtsummen unmittelbar nach der Datenmarkierung in die Zeile eingefügt werden, um Berechnungen basierend auf den eingefügten Daten durchzuführen. Verwenden Sie dynamische Formeln, um Berechnungen für die eingefügten Zeilen durchzuführen.

 Intelligente Markierungen bestehen aus der**Datenquelle** und**Feldname**Teile für die meisten Informationen. Bei Variablen und Variablenarrays können auch spezielle Informationen übergeben werden. Variablen füllen immer nur eine Zelle, während Variablenarrays mehrere füllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete Smart-Marker werden entfernt.

Smart Marker kann auch Parameter enthalten. Mit Parametern können Sie ändern, wie die Informationen angeordnet werden. Sie werden als kommaseparierte Liste in Klammern an das Ende des Smart-Markers angehängt.
### **Smart-Marker-Optionen**
- &=Datenquelle.Feldname
- &=Datenquelle.Feldname
- &=$VariablenName
- &=$VariableArray
- &==DynamischeFormel
- &=&=DynamischeFormel wiederholen
### **Parameter**
Folgende Parameter sind erlaubt:

- noadd - Fügen Sie keine zusätzlichen Zeilen hinzu, um Daten anzupassen.
- skip:n – Überspringe n Zeilen für jede Datenzeile.
- aufsteigend:n oder absteigend:n - Daten in Smartmarkern sortieren. Wenn n 1 ist, dann ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach Verarbeitung der Datenquelle sortiert. ZB &=Tabelle1.Feld3(aufsteigend:1).
- horizontal - Schreiben Sie Daten von links nach rechts, anstatt von oben nach unten.
- Numerisch - Konvertieren Sie Text nach Möglichkeit in eine Zahl. Wird nur in der Version .NET unterstützt.
- shift - Nach unten oder rechts verschieben, wodurch zusätzliche Zeilen oder Spalten erstellt werden, um die Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Wenn Sie beispielsweise in MS Excel einen Zellbereich auswählen, klicken Sie mit der rechten Maustaste und wählen Sie Einfügen und geben Sie Zellen nach unten verschieben, Zellen nach rechts verschieben und andere Optionen an. Kurz gesagt erfüllt der Verschiebungsparameter die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smartmarker.
- copystyle – Kopiert den Stil der Basiszelle in alle Zellen in dieser Spalte.

 Die Parameter**noadd** und skip können kombiniert werden, um Daten in abwechselnden Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie in der ersten Zeile noadd hinzufügen, um zu vermeiden, dass zusätzliche Zeilen vor der alternativen Zeile eingefügt werden.
