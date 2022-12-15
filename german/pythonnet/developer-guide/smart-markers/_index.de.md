---
title: Smartes Importieren und Platzieren von Daten mit Smart Markern in Python über .Net
linktitle: Intelligente Markierungen
type: docs
weight: 190
url: /de/python-net/using-smart-markers/
description: Intelligentes Importieren und Platzieren von Daten gemäß den Excel-Vorlagendateien mit Aspose.Cells for Python über die .Net-Bibliothek.
---
## **Einführung**
**Intelligente Markierungen**werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in einer Microsoft Excel-Designertabelle platziert werden sollen. Mit intelligenten Markierungen können Sie Vorlagen erstellen, die nur bestimmte Informationen und Formatierungen enthalten.
## **Designer-Tabellenkalkulation und intelligente Markierungen**
Designer-Arbeitsblätter sind standardmäßige Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Markierungen enthalten. Sie können intelligente Markierungen enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu verwandten Kontakten. Intelligente Markierungen werden in die Zellen geschrieben, in denen Sie die Informationen wünschen.

 Alle intelligenten Markierungen beginnen mit &=. Ein Beispiel für eine Datenmarkierung ist &=Party.FullName. Wenn die Datenmarkierung mehr als ein Element ergibt, z. B. eine vollständige Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Somit können Zwischensummen und Gesamtsummen unmittelbar nach der Datenmarkierung in die Zeile eingefügt werden, um Berechnungen basierend auf den eingefügten Daten durchzuführen. Um Berechnungen für die eingefügten Zeilen durchzuführen, verwenden Sie**dynamische Formeln**.

 Intelligente Markierungen bestehen aus der**Datenquelle** und**Feldname**Teile für die meisten Informationen. Bei Variablen und Variablenarrays können auch spezielle Informationen übergeben werden. Variablen füllen immer nur eine Zelle, während Variablenarrays mehrere füllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete Smart-Marker werden entfernt.

Smart Marker kann auch Parameter enthalten. Mit Parametern können Sie die Anordnung der Informationen ändern. Sie werden als kommagetrennte Liste in Klammern an das Ende des Smart-Markers angehängt.
### **Smart-Marker-Optionen**
 &=Datenquelle.Feldname
 &=[Datenquelle].[Feldname]&=$VariablenName
 &=$VariableArray
 &==DynamischeFormel
&=&=DynamischeFormel wiederholen
### **Parameter**
Folgende Parameter sind erlaubt:

- **noadd** - Fügen Sie keine zusätzlichen Zeilen hinzu, um Daten anzupassen.
- **überspringen: n** - Überspringen Sie n Zeilen für jede Datenzeile.
- **aufsteigend: n** oder**absteigend: n** - Daten in Smartmarkern sortieren. Wenn n 1 ist, dann ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach Verarbeitung der Datenquelle sortiert. Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreiben Sie Daten von links nach rechts, anstatt von oben nach unten.
- **numerisch** - Text wenn möglich in Zahlen umwandeln.
- **Wechsel** - Verschieben Sie nach unten oder rechts und erstellen Sie zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Wenn Sie beispielsweise in Microsoft Excel einen Zellbereich auswählen, klicken Sie mit der rechten Maustaste und wählen Sie aus**Einfügung** und angeben?**Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen. Kurz gesagt, die**Wechsel** Der Parameter erfüllt die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smartmarker.
- **Kopierstil** - Kopieren Sie den Stil der Basiszelle in alle Zellen in dieser Spalte.

Die Parameter noadd und skip können kombiniert werden, um Daten abwechselnd in Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie in der ersten Zeile noadd hinzufügen, um zu vermeiden, dass zusätzliche Zeilen vor der alternativen Zeile eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie sie mit einem Komma, aber ohne Leerzeichen: ParameterA,ParameterB,ParameterC

Die folgenden Screenshots zeigen, wie Daten in jede zweite Zeile eingefügt werden.

|**Vorlagendatei**|**Ausgabedatei**|
|:- |:- |
|![todo: Bild_alt_Text](using-smart-markers_1.jpg)|![todo: Bild_alt_Text](using-smart-markers_2.jpg)|
### **Dynamische Formeln**
Mit dynamischen Formeln können Sie Excel-Formeln in Zellen einfügen, selbst wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können sich für jede eingefügte Zeile wiederholen oder nur die Zelle verwenden, in der die Datenmarkierung platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r - Aktuelle Zeilennummer.
- 2, -1 - Versatz zur aktuellen Zeilennummer.

Zum Beispiel:

{{< highlight "java" >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

In der dynamischen Formelmarkierung bezeichnet "-1" den Versatz zur aktuellen Zeile in den B- bzw. C-Spalten, der für die Divisionsoperation eingestellt wird, der Skip-Parameter ist eine Zeile. Außerdem sollten wir das folgende Zeichen angeben:

{{< highlight "java" >}}

 "~"

{{< /highlight >}}

als Trennzeichen, um weitere Parameter in dynamische Formeln zu übernehmen.

Die folgenden Screenshots veranschaulichen eine sich wiederholende dynamische Formel und das resultierende Excel-Arbeitsblatt.

|**Vorlagendatei**|**Ausgabedatei**|
|:- |:- |
|![todo: Bild_alt_Text](using-smart-markers_3.jpg)|![todo: Bild_alt_Text](using-smart-markers_4.jpg)|
 Cell "C1" enthält die Formel**= A1*B1** , Zelle "C2" enthält**= A2*B2** und Zelle "C3" enthält**= A3*B3**.

Die Verarbeitung der Smartmarker ist sehr einfach. Was folgt, ist ein Codeschnipsel in Python über .Net, das zeigt, wie es gemacht wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


