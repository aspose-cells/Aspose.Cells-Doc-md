---
title: Verwenden von Smart-Markern
type: docs
weight: 40
url: /de/java/using-smart-markers/
---
## **Einführung**

{{% alert color="primary" %}}

**Intelligente Markierungen** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in einem Microsoft-Excel abgelegt werden sollen[Designer-Tabelle](/cells/de/java/what-is-a-designer-spreadsheet/). Mit intelligenten Markierungen können Sie Vorlagen erstellen, die nur relevante Informationen und Formatierungen enthalten.

{{% /alert %}}

## **Designer-Tabellenkalkulation und intelligente Markierungen**

Designer-Arbeitsblätter sind standardmäßige Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Markierungen enthalten. Sie können intelligente Markierungen enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu verwandten Kontakten. Intelligente Markierungen werden in die Zellen geschrieben, in denen Sie Informationen wünschen.

 Alle intelligenten Markierungen beginnen mit &=. Ein Beispiel für eine Datenmarkierung ist &=Party.FullName. Wenn die Datenmarkierung mehr als ein Element ergibt, z. B. eine vollständige Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Somit können Zwischensummen und Gesamtsummen unmittelbar nach der Datenmarkierung in der Zeile platziert werden, um Berechnungen auf der Grundlage der eingefügten Daten durchzuführen. Um Berechnungen für die eingefügten Zeilen durchzuführen, verwenden Sie[dynamische Formeln](/cells/de/java/using-smart-markers/#dynamic-formulas).

 Intelligente Markierungen bestehen aus der**Datenquelle** und**Feldname**Teile für die meisten Informationen. Bei Variablen und Variablenarrays können auch spezielle Informationen übergeben werden. Variablen füllen immer nur eine Zelle, während Variablenarrays mehrere füllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete Smart-Marker werden entfernt.

Ein Smart-Marker kann auch Parameter enthalten. Mit Parametern können Sie die Anordnung der Informationen ändern. Sie werden als kommaseparierte Liste in Klammern an das Ende des Smart-Markers angehängt.

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
- *aufsteigend:n oder absteigend:n - Daten in Smartmarkern sortieren. Wenn n 1 ist, dann ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach Verarbeitung der Datenquelle sortiert. Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreiben Sie Daten von links nach rechts, anstatt von oben nach unten.
- **numerisch** - Text wenn möglich in Zahlen umwandeln.
- **Schicht** - Verschieben Sie nach unten oder rechts und erstellen Sie zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Wenn Sie beispielsweise in Microsoft Excel einen Zellbereich auswählen, klicken Sie mit der rechten Maustaste und wählen Sie aus**Einfügung** und spezifizieren**Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen. Kurz gesagt erfüllt der Verschiebungsparameter die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smartmarker.
- **Bohne** - Gibt an, dass die Datenquelle ein einfaches POJO ist. Nur unterstützt in der Java API.

Die Parameter noadd und skip können kombiniert werden, um Daten abwechselnd in Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie in der ersten Zeile noadd hinzufügen, um zu vermeiden, dass zusätzliche Zeilen vor der alternativen Zeile eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie sie mit einem Komma, aber ohne Leerzeichen: ParameterA,ParameterB,ParameterC

Die folgenden Screenshots zeigen, wie Daten in jede zweite Zeile eingefügt werden.

![todo: Bild_alt_Text](using-smart-markers_1.png)

**wird...**

![todo: Bild_alt_Text](using-smart-markers_2.png)

### **Dynamische Formeln**

Mit dynamischen Formeln können Sie Excel-Formeln in Zellen einfügen, selbst wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können sich für jede eingefügte Zeile wiederholen oder nur die Zelle verwenden, in der die Datenmarkierung platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r - Aktuelle Zeilennummer.
- 2, -1 - Versatz zur aktuellen Zeilennummer.

Das Folgende veranschaulicht eine sich wiederholende dynamische Formel und das resultierende Excel-Arbeitsblatt.

![todo: Bild_alt_Text](using-smart-markers_3.png)

**wird…**

![todo: Bild_alt_Text](using-smart-markers_4.png)

Cell C1 enthält die Formel =A1*B1, C2 enthält = A2*B2 und C3 = A3*B3.

Die Verarbeitung der Smartmarker ist sehr einfach. Das folgende Code-Snippet zeigt, wie es gemacht wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Verwenden von Variablen-Arrays**

Der folgende Beispielcode zeigt, wie Variablen-Arrays in Smart Markers verwendet werden. Wir platzieren dynamisch eine variable Array-Markierung in der A1-Zelle des ersten Arbeitsblatts der Arbeitsmappe, die eine Reihe von Werten enthält, die wir für die Markierung festlegen, und verarbeiten die Markierungen, um Daten in die Zellen gegen die Markierung zu füllen. Abschließend speichern wir die Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Daten gruppieren**

In einigen Excel-Berichten müssen Sie die Daten möglicherweise in Gruppen aufteilen, um sie leichter lesen und analysieren zu können. Einer der Hauptzwecke für das Aufteilen von Daten in Gruppen ist das Ausführen von Berechnungen (Durchführen von Zusammenfassungsoperationen) für jede Gruppe von Datensätzen.

Aspose.Cells Mit intelligenten Markierungen können Sie Daten nach Feldern gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen platzieren. Wenn Sie beispielsweise Daten nach Customers.CustomerID gruppieren, können Sie jedes Mal, wenn sich die Gruppe ändert, einen Zusammenfassungsdatensatz hinzufügen.

### **Parameter**

Im Folgenden sind einige Smart-Marker-Parameter aufgeführt, die zum Gruppieren von Daten verwendet werden.

#### **Gruppe:normal/zusammenführen/wiederholen**

Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- **normal** - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze in der Spalte nicht wiederholt; stattdessen werden sie einmal pro Datengruppe gedruckt.
- **verschmelzen** - Dasselbe Verhalten wie beim normalen Parameter, außer dass die Zellen in den Gruppieren-nach-Feldern für jeden Gruppensatz zusammengeführt werden.
- **wiederholen** - Der Gruppieren-nach-Feld(er)-Wert wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Kunden.KundenID(Gruppe:Merge)

#### **überspringen**

Überspringt eine bestimmte Anzahl von Zeilen nach jeder Gruppe.

Zum Beispiel &=Employees.EmployeeID(group:normal,skip:1)

#### **ZwischensummeN**

Führt eine Zusammenfassungsoperation für bestimmte Felddaten aus, die sich auf ein Gruppieren-nach-Feld beziehen. Das N steht für Zahlen zwischen 1 und 11, die die Funktion angeben, die beim Berechnen von Zwischensummen innerhalb einer Datenliste verwendet wird. (1=MITTELWERT, 2=ZAHL, 3=ZAHLA, 4=MAX, 5=MIN,...9=SUMME usw.) Weitere Einzelheiten finden Sie in der Zwischensummen-Referenz in der Excel-Hilfe Microsoft.

Das Format lautet tatsächlich wie folgt:
subtotalN:Ref wobei Ref sich auf die Gruppierung nach Spalte bezieht.

Zum Beispiel,

-  &=Products.Units(subtotal9:Products.ProductID) gibt die Zusammenfassungsfunktion an**Einheiten** Feld in Bezug auf die**Produkt ID** Feld im**Produkte** Tisch.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) gibt die Zusammenfassungsfunktion an**Spalte3** Feldgruppe nach**Spalte1** in der Tabelle**Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) gibt die Zusammenfassungsfunktion an**SpalteD** Feldgruppe nach**SpalteA** und**SpalteB** im Tisch**Tabelle 1**.

## **Verwenden von verschachtelten Objekten**

Aspose.Cells unterstützt verschachtelte Objekte in Smartmarkern, die verschachtelten Objekte sollten einfach sein.

Wir verwenden eine einfache Vorlagendatei. Sehen Sie sich das Designer-Arbeitsblatt an, das einige verschachtelte intelligente Markierungen enthält.

**Das erste Arbeitsblatt der Designer-Datei mit verschachtelten Smart-Markern.**

![todo: Bild_alt_Text](using-smart-markers_5.png)

Wie das funktioniert, zeigt das folgende Beispiel. Das Ausführen des folgenden Codes führt zu der folgenden Ausgabe.

**Das erste Arbeitsblatt der Ausgabedatei mit den resultierenden Daten.**

![todo: Bild_alt_Text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Generische Liste als verschachteltes Objekt verwenden**

Aspose.Cells unterstützt jetzt auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der Excel-Ausgabedatei, die mit dem folgenden Code generiert wurde. Wie Sie im Screenshot sehen können, enthält ein Lehrerobjekt mehrere verschachtelte Schülerobjekte.

![todo: Bild_alt_Text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Verwendung der Eigenschaft HTML von Smart Markers**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft HTML der Smart Markers. Wenn es verarbeitet wird, wird "World" in "Hello World" wegen HTML fett angezeigt \<b> Schild.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden**

 Manchmal kann es erforderlich sein, die Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker, der verarbeitet wird, vor dem Abschluss zu erhalten. Dies kann mit der erreicht werden[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)Eigentum und[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Beispielcode und ausführliche Erläuterungen finden Sie in diesem Artikel.

- [Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden](/cells/de/java/getting-notifications-while-merging-data-with-smart-markers/)
