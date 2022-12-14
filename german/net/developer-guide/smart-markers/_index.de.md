---
title: Intelligentes Importieren und Platzieren von Daten mit Smart Markern
linktitle: Intelligente Markierungen
type: docs
weight: 190
url: /de/net/using-smart-markers/
description: Intelligentes Importieren und Platzieren von Daten gemäß den Excel-Vorlagendateien mit der Bibliothek Aspose.Cells.
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
- **Wechsel** - Verschieben Sie nach unten oder rechts und erstellen Sie zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Wenn Sie beispielsweise in Microsoft Excel einen Zellbereich auswählen, klicken Sie mit der rechten Maustaste und wählen Sie aus**Einfügung** und spezifizieren**Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen. Kurz gesagt, die**Wechsel** Der Parameter erfüllt die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smartmarker.
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

Die Verarbeitung der Smartmarker ist sehr einfach. Was folgt, sind zwei Codeausschnitte, einer in C# und einer in VB, die zeigen, wie es gemacht wird.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-DynamicFormulas-1.cs" >}}
## **Verwenden von Variablen-Arrays**
Der folgende Beispielcode zeigt, wie Variablen-Arrays in Smart Markern verwendet werden. Wir platzieren dynamisch eine variable Array-Markierung in der A1-Zelle des ersten Arbeitsblatts der Arbeitsmappe, die eine Zeichenfolge von Werten enthält, die wir für die Markierung festlegen, verarbeiten die Markierungen, um Daten in die Zellen gegen die Markierung zu füllen. Abschließend speichern wir die Excel-Datei.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}
## **Daten gruppieren**
In einigen Excel-Berichten müssen Sie die Daten möglicherweise in Gruppen aufteilen, um sie leichter lesen und analysieren zu können. Einer der Hauptzwecke für das Aufteilen von Daten in Gruppen ist das Ausführen von Berechnungen (Durchführen von Zusammenfassungsoperationen) für jede Gruppe von Datensätzen.

Aspose.Cells Mit intelligenten Markierungen können Sie Daten nach Feldern gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen platzieren. Wenn Sie beispielsweise Daten nach Customers.CustomerID gruppieren, können Sie jedes Mal, wenn sich die Gruppe ändert, einen Zusammenfassungsdatensatz hinzufügen.
### **Parameter**
Im Folgenden sind einige der Smart-Marker-Parameter aufgeführt, die zum Gruppieren von Daten verwendet werden.
#### **Gruppe:normal/zusammenführen/wiederholen**
Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- **normal** - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze in der Spalte nicht wiederholt; stattdessen werden sie einmal pro Datengruppe gedruckt.
- **verschmelzen** - Dasselbe Verhalten wie beim normalen Parameter, außer dass die Zellen in den Gruppieren-nach-Feldern für jeden Gruppensatz zusammengeführt werden.
- **wiederholen** - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Kunden.KundenID(Gruppe:Merge)
#### **überspringen**
Überspringt eine angegebene Anzahl von Zeilen nach jeder Gruppe.

Beispiel: &=Employees.EmployeeID(group:normal,skip:1)
#### **ZwischensummeN**
Führt eine Zusammenfassungsoperation für bestimmte Felddaten aus, die sich auf ein Gruppieren-nach-Feld beziehen. Das N steht für Zahlen zwischen 1 und 11, die die Funktion angeben, die beim Berechnen von Zwischensummen innerhalb einer Datenliste verwendet wird. (1=MITTELWERT, 2=ZAHL, 3=ZAHLA, 4=MAX, 5=MIN,...9=SUMME usw.) Weitere Einzelheiten finden Sie in der Zwischensummen-Referenz in der Excel-Hilfe Microsoft.

Das Format lautet tatsächlich wie folgt:
subtotalN:Ref wobei Ref sich auf die Gruppierung nach Spalte bezieht.

Zum Beispiel,

-  &=Products.Units(subtotal9:Products.ProductID) gibt die Zusammenfassungsfunktion an**Einheiten** Feld in Bezug auf die**Produkt ID** Feld im**Produkte** Tisch.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) gibt die Zusammenfassungsfunktion an**Spalte3** Feldgruppe nach**Spalte1** in der Tabelle**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) gibt die Zusammenfassungsfunktion an**SpalteD** Feldgruppe nach**SpalteA** und**SpalteB** in der Tabelle**Tabelle 1**.

Dieses Beispiel zeigt einige der Gruppierungsparameter in Aktion. Es verwendet die Access-Datenbank Northwind.mdb Microsoft und extrahiert Daten aus der Tabelle mit dem Namen "Bestelldetails". Wir erstellen eine Designer-Datei mit dem Namen SmartMarker_Designer.xls in Microsoft Excel und platzieren intelligente Markierungen in verschiedenen Zellen in Arbeitsblättern. Die Markierungen werden verarbeitet, um die Arbeitsblätter zu füllen. Die Daten werden durch ein Gruppenfeld platziert und organisiert.

Die Designerdatei hat zwei Arbeitsblätter. In der ersten setzen wir intelligente Markierungen mit Gruppierungsparametern, wie im folgenden Screenshot gezeigt. Drei Smart-Marker (mit Gruppierungsparametern) werden platziert:
&=[Bestelldetails].OrderID(group:merge,skip:1),
&=[Bestelldetails].Menge(Zwischensumme9:Bestelldetails.Bestell-ID) und
&=[Bestelldetails].UnitPrice(subtotal9:Order Details.OrderID) geht jeweils in A5, B5 und C5.

|**Das erste Arbeitsblatt in der Datei SmartMarker_Designer.xls, komplett mit intelligenten Markierungen**|
|:- |
|![todo: Bild_alt_Text](using-smart-markers_5.png)|
Im zweiten Arbeitsblatt der Designer-Datei setzen wir einige weitere intelligente Markierungen, wie in der Abbildung unten gezeigt. Wir setzen die folgenden Smartmarker:
&=[Bestelldetails].OrderID(group:normal),
&=[Bestelldetails].Menge,
&=[Bestelldetails].Einheitspreis,
&=&=B(r)*C(r) und
&=subtotal9:Order Details.OrderID jeweils in A5, B5, C5, D5 und C6.

|**Das zweite Arbeitsblatt der Datei SmartMarker_Designer.xls mit gemischten Smart-Markern.**|
|:- |
|![todo: Bild_alt_Text](using-smart-markers_6.png)|
Hier ist der im Beispiel verwendete Quellcode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-GroupingData-1.cs" >}}

{{% alert color="primary" %}} 

Wenn Sie Ihre eigenen benutzerdefinierten Beschriftungen zu den Zusammenfassungszeilen hinzufügen müssen oder den Feldnamen mit einer Beschriftung verketten möchten, z. B. „Zwischensumme der Bestellungen“, stellt Aspose.Cells Ihnen die Attribute „Label“ und „LabelPosition“ zur Verfügung, sodass Sie Ihre benutzerdefinierten Beschriftungen im Smart platzieren können Markierungen beim Verketten mit den Zwischensummenzeilen beim Gruppieren von Daten. Siehe das Dokument zum Hinzufügen von benutzerdefinierten Beschriftungen zum Verketten mit den Zwischensummenzeilen in intelligenten Markierungen als Referenz.

{{% /alert %}} 
## **Verwenden von anonymen Typen oder benutzerdefinierten Objekten**
Aspose.Cells unterstützt auch anonyme Typen oder benutzerdefinierte Objekte in Smartmarkern. Das folgende Beispiel zeigt, wie das funktioniert. Informationen zum Importieren von Daten aus dynamischen Objekten mithilfe von Smart Markers finden Sie im folgenden Artikel:

[Import aus dynamischem Objekt als Datenquelle](/cells/de/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}
## **Bildmarkierungen**
Aspose.Cells Intelligente Markierungen unterstützen auch Bildmarkierungen. Dieser Abschnitt zeigt Ihnen, wie Sie Bilder mit intelligenten Markierungen einfügen.
### **Bildparameter**
Smart-Marker-Parameter zum Verwalten von Bildern.

- **Bild:FitToCell** - Passen Sie das Bild automatisch an die Zeilenhöhe und Spaltenbreite der Zelle an.
- **Bild:ScaleN** - Skalieren Sie Höhe und Breite auf N Prozent.
- **Bild:Breite:Nin&Höhe:Nin** - Rendern Sie das Bild N Zoll hoch und N Zoll breit. Sie können auch die Positionen Links und Oben (in Punkten) angeben.

Hier ist der im Beispiel verwendete Quellcode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}
## **Verwenden von verschachtelten Objekten**
Aspose.Cells unterstützt verschachtelte Objekte in Smartmarkern, die verschachtelten Objekte sollten einfach sein. Wir verwenden eine einfache Vorlagendatei. Sehen Sie sich das Designer-Arbeitsblatt an, das einige verschachtelte intelligente Markierungen enthält.

|**Das erste Arbeitsblatt der Datei SM_NestedObjects.xlsx mit verschachtelten Smart-Markern.**|
|:- |
|![todo: Bild_alt_Text](using-smart-markers_7.png)|
Wie das funktioniert, zeigt das folgende Beispiel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}
## **Generische Liste als verschachteltes Objekt verwenden**
Aspose.Cells unterstützt jetzt auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der Excel-Ausgabedatei, die mit dem folgenden Code generiert wurde. Wie Sie im Screenshot sehen können, enthält ein Teacher-Objekt mehrere verschachtelte Student-Objekte.

|![todo: Bild_alt_Text](using-smart-markers_8.png)|
|:- |




{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}
## **Verwenden der HTML-Eigenschaft von Smart Markers**
 Der folgende Beispielcode erläutert die Verwendung der HTML-Eigenschaft der Smart Marker. Wenn es verarbeitet wird, wird "World" in "Hello World" aufgrund von HTML fett angezeigt<b>Schild.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

## **Nicht zeilenweise**
 Die aktuelle Standardverarbeitungsmethode besteht darin, Smartmaker Zeile für Zeile zu verarbeiten. Aber manchmal müssen die intelligenten Markierungen derselben Datentabelle zusammen verarbeitet werden, egal
Wenn sie sich in derselben Zeile befinden oder nicht, müssen Sie einen benannten Bereich „_CellsSmartMarkers“ angeben und WorkbookDesigner.LineByLine als „false“ angeben, bevor Sie die Verarbeitung aufrufen.

|![todo: Bild_alt_Text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

## **Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden**
Manchmal kann es erforderlich sein, die Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker, der verarbeitet wird, vor dem Abschluss zu erhalten. Dies kann mit der WorkbookDesigner.CallBack-Eigenschaft und ISmartMarkerCallBack erreicht werden

## **Themen vorantreiben**
- [Hinzufügen von anonymen oder benutzerdefinierten Objekten zu SmartMarkern](/cells/de/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Smart-Marker-Daten automatisch in andere Arbeitsblätter einfügen, wenn die Daten zu groß sind](/cells/de/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formatieren von intelligenten Markierungen](/cells/de/net/formatting-smart-markers/)
- [Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden](/cells/de/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Legen Sie eine benutzerdefinierte Datenquelle für WorkbookDesigner fest](/cells/de/net/set-custom-datasource-for-workbookdesigner/)
- [Führenden Apostroph in Zellen anzeigen](/cells/de/net/show-leading-apostrophe-in-cells/)
- [Verwenden des Formelparameters im Smart Marker-Feld](/cells/de/net/using-formula-parameter-in-smart-marker-field/)
- [Verwenden von Bildmarkierungen beim Gruppieren von Daten in Smart-Markierungen](/cells/de/net/using-image-markers-while-grouping-data-in-smart-markers/)


