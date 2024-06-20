---
title: Intelligentes Importieren und Platzieren von Daten mit intelligenten Markern in Python über .Net
linktitle: Intelligente Marker
type: docs
weight: 190
url: /de/python-net/using-smart-markers/
description: Intelligentes Importieren und Platzieren von Daten entsprechend den Vorlagen Excel Dateien mit Aspose.Cells für Python über die .Net Bibliothek.
---

## **Einführung**
**Intelligente Marker** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in eine Microsoft Excel-Designer-Tabelle eingegeben werden sollen. Intelligente Marker ermöglichen es Ihnen, Vorlagen zu erstellen, die nur bestimmte Informationen und Formatierungen enthalten.
## **Designer-Tabelle & Intelligente Marker**
Designer-Tabellen sind Standard-Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Marker enthalten. Sie können intelligente Marker enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu relevanten Kontakten. Intelligente Marker werden in die Zellen geschrieben, in denen Sie die Informationen platzieren möchten.

Alle intelligenten Marker beginnen mit &=. Ein Beispiel für einen Datenmarker ist &=Party.FullName. Wenn der Datenmarker zu mehr als einem Element führt, beispielsweise einer vollständigen Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Somit können Zwischensummen und Summen in die Zeile unmittelbar nach dem Datenmarker platziert werden, um Berechnungen auf Basis der eingefügten Daten durchzuführen. Um Berechnungen auf den eingefügten Zeilen durchzuführen, verwenden Sie **dynamische Formeln**.

Intelligente Marker bestehen aus den Teilen **Datenquelle** und **Feldname** für die meisten Informationen. Spezielle Informationen können auch mit Variablen und Variablenarrays übergeben werden. Variablen füllen immer nur eine Zelle aus, während Variablenarrays mehrere Zellen ausfüllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete intelligente Marker werden entfernt.

Intelligente Marker können auch Parameter enthalten. Parameter ermöglichen es Ihnen, zu ändern, wie die Informationen dargestellt werden. Sie werden am Ende des intelligenten Markers in Klammern als durch Kommas getrennte Liste angehängt.
### **Intelligente Marker-Optionen**
&=Datenquelle.Feldname 
&=[Datenquelle].[Feldname] 
&=$Variablenname 
&=$VariablenArray 
&==DynamischeFormel 
&=&=WiederholendeDynamischeFormel
### **Parameter**
Folgende Parameter sind erlaubt:

- **noadd** - Füge keine zusätzlichen Zeilen hinzu, um Daten anzupassen.
- **skip:n** - Überspringe n Zeilen für jede Datensatzzeile.
- **ascending:n** oder **descending:n** - Sortiere Daten in Smart-Markern. Wenn n 1 ist, ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach der Verarbeitung der Datenquelle sortiert. Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreibe Daten von links nach rechts anstatt von oben nach unten.
- **numeric** - Konvertiere Text in eine Zahl, wenn möglich.
- **shift** - Verschiebe nach unten oder rechts und erstelle zusätzliche Zeilen oder Spalten, um Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Beispiel: Wenn Sie in Microsoft Excel einen Zellbereich auswählen, mit der rechten Maustaste klicken und **Einfügen** auswählen und dabei?**Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen angeben. Kurz gesagt, der **shift**-Parameter erfüllt die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smart-Marker.
- **copystyle** - Kopiere den Zellstil der Basiszelle in alle Zellen dieser Spalte.

Die Parameter noadd und skip können kombiniert werden, um Daten in alternierende Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie noadd in der ersten Zeile hinzufügen, um zu verhindern, dass zusätzliche Zeilen vor der alternierenden Zeile eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie diese mit Kommas, aber ohne Leerzeichen: parameterA,parameterB,parameterC.

Die folgenden Screenshots zeigen, wie Daten in jeder zweiten Zeile eingefügt werden.

|**Vorlagendatei**|**Ausgabedatei**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|
### **Dynamische Formeln**
Dynamische Formeln ermöglichen es Ihnen, Excel-Formeln in Zellen einzufügen, auch wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können für jede eingefügte Zeile wiederholt werden oder nur die Zelle verwenden, in der der Datenmarker platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r - Aktuelle Zeilennummer.
- 2, -1 - Versatz zur aktuellen Zeilennummer.

Zum Beispiel:

{{< highlight java >}}

 &=&=B{-1}/C{-1}~(skip:1)

{{< /highlight >}}

Im dynamischen Formelmarker steht "-1" für den Versatz zur aktuellen Zeile in den Spalten B und C, die für die Divisionsoperation festgelegt werden, der Überspringparameter beträgt eine Zeile. Darüber hinaus sollten wir das folgende Zeichen angeben:

{{< highlight java >}}

 "~"

{{< /highlight >}}

als Trennzeichen, um weitere Parameter in dynamischen Formeln anzuwenden.

Die folgenden Screenshots veranschaulichen eine wiederholende dynamische Formel und das resultierende Excel-Arbeitsblatt.

|**Vorlagendatei**|**Ausgabedatei**|
| :- | :- |
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|
Die Zelle "C1" enthält die Formel **= A1*B1**, die Zelle "C2" enthält **= A2*B2** und die Zelle "C3" enthält **= A3*B3**.

Es ist sehr einfach, die Smart-Marker zu verarbeiten. Im Folgenden finden Sie einen Code-Schnipsel in Python über .Net, der zeigt, wie dies gemacht wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "SmartMarker-SimpleProcess.py" >}}


