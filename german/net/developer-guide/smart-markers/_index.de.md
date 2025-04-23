---
title: Intelligentes Importieren und Platzieren von Daten mit intelligenten Markern
linktitle: Intelligente Marker
type: docs
weight: 190
url: /de/net/using-smart-markers/
description: Intelligentes Importieren und Platzieren von Daten gemäß den Vorlagen Excel Dateien mit der Aspose.Cells Bibliothek.
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
- **shift** - Verschiebt nach unten oder rechts und erstellt zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert auf die gleiche Weise wie in Microsoft Excel. Zum Beispiel, wenn Sie in Microsoft Excel einen Bereich von Zellen auswählen, mit der rechten Maustaste darauf klicken und **Einfügen** auswählen und **Zellen nach unten verschieben** oder **Zellen nach rechts verschieben** oder andere Optionen angeben. Kurz gesagt, der **shift**-Parameter erfüllt die gleiche Funktion für vertikale/übliche (von oben nach unten) oder horizontale (von links nach rechts) intelligente Markierungen.
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

Es ist sehr einfach, die Smart Marker zu verarbeiten. Im folgenden Beispielcode wird gezeigt, wie dynamische Formeln in Smart Markers verwendet werden. Wir laden die [Template-Datei](templateDynamicFormulas.xlsx) und erstellen Testdaten, um die Marker zu verarbeiten, um Daten in die Zellen gegen den Marker einzufügen. 

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}

## **Verwendung von Variablen Arrays**
Im folgenden Beispielcode wird gezeigt, wie Variable Arrays in Smart Markers verwendet werden. Wir platzieren einen Variablen-Array-Marker in Zelle A1 des ersten Arbeitsblatts der Arbeitsmappe dynamisch, der einen String von Werten enthält, die wir für den Marker festlegen, verarbeiten die Marker, um Daten in die Zellen gegen den Marker einzufügen. Schließlich speichern wir die Excel-Datei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Daten gruppieren**
In einigen Excel-Berichten ist es möglicherweise erforderlich, die Daten in Gruppen aufzuteilen, um sie einfacher zu lesen und zu analysieren. Ein Hauptzweck, Daten in Gruppen aufzuteilen, besteht darin, Berechnungen (Zusammenfassungsoperationen) für jede Gruppe von Datensätzen auszuführen.

Aspose.Cells Smart Marker ermöglicht es Ihnen, Daten nach Feldern zu gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen zu platzieren. Wenn beispielsweise die Daten nach Kunden.CustomerID gruppiert werden, können Sie jedes Mal einen Zusammenfassungsdatensatz hinzufügen, wenn sich die Gruppe ändert.
### **Parameter**
Im Folgenden sind einige der Smart-Marker-Parameter aufgeführt, die für die Gruppierung von Daten verwendet werden.
#### **group:normal/merge/repeat**
Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- **normal** - Der Gruppenwert wird nicht für die entsprechenden Datensätze in der Spalte wiederholt; stattdessen wird er einmal pro Datengruppe gedruckt.
- **merge** - Das gleiche Verhalten wie beim normalen Parameter, außer dass die Zellen im Gruppenwert für jede Gruppeneinstellung zusammengeführt werden.
- **repeat** - Der Gruppenwert wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Kunden.KundenID(group:merge)
#### **skip**
Überspringt eine bestimmte Anzahl von Zeilen nach jeder Gruppe.

Zum Beispiel: &=Mitarbeiter.MitarbeiterID(group:normal,skip:1)
#### **subtotalN**
Führt eine Zusammenfassungsoperation für ein spezifisches Felddatum in Bezug auf ein Gruppenfeld durch. Das N stellt Zahlen zwischen 1 und 11 dar, die die Funktion spezifizieren, die beim Berechnen von Zwischensummen innerhalb einer Liste von Daten verwendet wird. (1=DURCHSCHNITT, 2=ANZAHL, 3=ANZAHL2, 4=MAX, 5=MIN,...9=SUMME usw.) Siehe die Zwischensumme-Referenz in der Hilfe von Microsoft Excel für weitere Details.

Das Format gibt tatsächlich an:
subtotalN:Verweis, wobei Verweis sich auf die Gruppierungs-Spalte bezieht.

Zum Beispiel,

- &=Products.Units(subtotal9:Products.ProductID) legt die Zusammenfassungsfunktion auf das **Units** Feld in Bezug auf das **ProductID** Feld in der Tabelle **Products** fest.
- &=Tabx.Col3(subtotal9:Tabx.Col1) legt die Zusammenfassungsfunktion auf das **Col3** Feld gruppiert nach **Col1** in der Tabelle **Tabx** fest.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) legt die Zusammenfassungsfunktion auf das **ColumnD** Feld gruppiert nach **ColumnA** und **ColumnB** in der Tabelle **Table1** fest.

Dieses Beispiel zeigt einige der Gruppierungsparameter in Aktion. Es verwendet die Microsoft Access-Datenbank Northwind.mdb und extrahiert Daten aus der Tabelle "Order Details". Wir erstellen eine Designer-Datei namens SmartMarker_Designer.xls in Microsoft Excel und fügen Smart Marker in verschiedene Zellen in Arbeitsblättern ein. Die Marker werden verarbeitet, um die Arbeitsblätter auszufüllen. Die Daten werden anhand eines Gruppenfelds platziert und organisiert.

Die Designer-Datei hat zwei Arbeitsblätter. Im ersten Arbeitsblatt fügen wir Smart Marker mit Gruppierungsparametern gemäß dem untenstehenden Screenshot ein. Drei Smart Marker (mit Gruppierungsparametern) werden platziert:
&=[Order Details].OrderID(group:merge,skip:1),
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), und
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) gehen in A5, B5 und C5 jeweils.

|**Das erste Arbeitsblatt in der Datei SmartMarker_Designer.xls, komplett mit Smart Markern**|
| :- |
|![todo:image_alt_text](using-smart-markers_5.png)|
Im zweiten Arbeitsblatt der Designer-Datei fügen wir einige weitere Smart Marker ein, wie in der Abbildung unten gezeigt. Wir platzieren die folgenden Smart Marker:
&=[Order Details].OrderID(group:normal),
&=[Order Details].Quantity,
&=[Order Details].UnitPrice,
&=&=B(r)*C(r), und
&=subtotal9:Order Details.OrderID in A5, B5, C5, D5 und C6 jeweils.

|**Das zweite Arbeitsblatt der Datei SmartMarker_Designer.xls, zeigt gemischte Smart Marker.**|
| :- |
|![todo:image_alt_text](using-smart-markers_6.png)|
Hier ist der im Beispiel verwendete Quellcode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie eigene benutzerdefinierte Bezeichnungen zu den Zwischensummenzeilen hinzufügen möchten oder das Feld mit einer Bezeichnung verketten möchten, z.B. "Gesamtsumme der Bestellungen", bietet Aspose.Cells die Attribute Label und LabelPosition, damit Sie Ihre benutzerdefinierten Bezeichnungen in den Smart Markern platzieren können, während Sie mit den Zwischensummenzeilen in Gruppendaten verketten. Lesen Sie das Dokument, wie benutzerdefinierte Bezeichnungen hinzugefügt werden können, um mit den Zwischensummenzeilen in Smart Markern zu verketten, als Referenz.

{{% /alert %}} 
## **Verwendung anonymer Typen oder benutzerdefinierter Objekte**
Aspose.Cells unterstützt auch anonyme Typen oder benutzerdefinierte Objekte in Smart Markern. Das folgende Beispiel zeigt, wie dies funktioniert. Für den Import von Daten aus dynamischen Objekten mithilfe von Smart Markern besuchen Sie den folgenden Artikel:

[Importieren aus dynamischem Objekt als Datenquelle](/cells/de/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Bildmarkierungen**
Aspose.Cells Smart Marker unterstützt auch Bild-Marker. In diesem Abschnitt wird gezeigt, wie Sie Bilder mithilfe von Smart Markern einfügen.
### **Bildparameter**
Smart Marker-Parameter zur Verwaltung von Bildern.

- **Bild:PassendZurZelle** - Das Bild automatisch an die Zeilenhöhe und Spaltenbreite der Zelle anpassen.
- **Bild:Skalierung N** - Höhe und Breite auf N Prozent skalieren.
- **Bild:Breite:Nin&Höhe:Nin** - Das Bild N Zoll hoch und N Zoll breit darstellen. Sie können auch die Positionen Links und Oben angeben (in Punkten).

Hier ist der im Beispiel verwendete Quellcode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Verwendung von verschachtelten Objekten**
Aspose.Cells unterstützt verschachtelte Objekte in Smart Markern, die verschachtelten Objekte sollten einfach sein. Wir verwenden eine einfache Vorlagendatei. Sehen Sie die Designer-Tabelle, die einige verschachtelte Smart Marker enthält.

|**Die erste Arbeitsmappe der SM_NestedObjects.xlsx Datei zeigt verschachtelte Smart Marker.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
Das folgende Beispiel zeigt, wie dies funktioniert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}

## **Verwendung von JSON-Daten**
Aspose.Cells unterstützt JSON-Daten in Smart Markern, JSON-Daten können hierarchisch verschachtelt sein. Bitte überprüfen Sie [Vorlagendatei](smartmarker.xlsx), [JSON-Datei](smartmarker.json) und den Screenshot der Ausgabedatei im Excel-Format, die mit dem folgenden Code generiert wurde.

|**Das erste Arbeitsblatt der Datei smartmarker.xlsx zeigt Smart Marker.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**Screenshot der Ausgabedatei im Excel-Format.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Die JSON-Daten sind wie folgt:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
Das folgende Beispiel zeigt, wie dies funktioniert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}

## **Verwendung von generischer Liste als verschachteltes Objekt**
Aspose.Cells unterstützt nun auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der generierten Ausgabee Excel-Datei mit dem folgenden Code. Wie im Screenshot zu sehen ist, enthält ein Lehrerobjekt mehrere verschachtelte Schülerobjekte.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Verwendung der HTML-Eigenschaften von Smart Markern**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Nicht Zeile für Zeile**
Die derzeitige Standardverarbeitungsmethode besteht darin, Smartmaker Zeile für Zeile zu verarbeiten. Manchmal müssen jedoch die Smart Marker derselben Datentabelle zusammen verarbeitet werden, unabhängig 
Wenn sie sich in der gleichen Zeile befinden oder nicht, müssen Sie einen benannten Bereich "_CellsSmartMarkers" angeben und WorkbookDesigner.LineByLine als falsch festlegen, bevor Sie die Verarbeitung aufrufen.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten**
Manchmal ist es erforderlich, Benachrichtigungen über den Zellenverweis oder den speziellen Smart Marker zu erhalten, der vor Abschluss verarbeitet wird. Dies kann mit der Eigenschaft WorkbookDesigner.CallBack und ISmartMarkerCallBack erreicht werden.

## **Erweiterte Themen**
- [Anonymes oder benutzerdefiniertes Objekt zu SmartMarkern hinzufügen](/cells/de/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Automatisches Ausfüllen von Smart Marker-Daten in anderen Arbeitsblättern, wenn die Daten zu groß sind](/cells/de/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatierung von Smart Markers](/cells/de/net/formatting-smart-markers/)
- [Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten](/cells/de/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Benutzerdefinierte Datenquelle für WorkbookDesigner festlegen](/cells/de/net/set-custom-datasource-for-workbookdesigner/)
- [Führende Apostrophzeichen in Zellen anzeigen](/cells/de/net/show-leading-apostrophe-in-cells/)
- [Verwenden des Formelparameters im Smart Marker-Feld](/cells/de/net/using-formula-parameter-in-smart-marker-field/)
- [Verwenden von Bildmarkern beim Gruppieren von Daten in Smart Markern](/cells/de/net/using-image-markers-while-grouping-data-in-smart-markers/)


{{< app/cells/assistant language="csharp" >}}
