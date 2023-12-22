---
title: Verwenden von Smart Markern
type: docs
weight: 40
url: /de/java/using-smart-markers/
---
##  **Einführung**

{{% alert color="primary" %}}

**Intelligente Markierungen** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in ein Microsoft Excel eingefügt werden sollen[Designer-Tabelle](/cells/de/java/what-is-a-designer-spreadsheet/). Mit intelligenten Markierungen können Sie Vorlagen erstellen, die nur relevante Informationen und Formatierungen enthalten.

{{% /alert %}}

##  **Designer-Tabelle und intelligente Marker**

Designer-Tabellen sind Standard-Excel-Dateien, die visuelle Formatierungen, Formeln und intelligente Markierungen enthalten. Sie können intelligente Markierungen enthalten, die auf eine oder mehrere Datenquellen verweisen, z. B. Informationen aus einem Projekt und Informationen zu zugehörigen Kontakten. Intelligente Markierungen werden in die Zellen geschrieben, in denen Sie Informationen wünschen.

Alle Smart Marker beginnen mit &=. Ein Beispiel für einen Datenmarker ist &=Party.FullName. Wenn die Datenmarkierung zu mehr als einem Element führt, beispielsweise zu einer vollständigen Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Somit können Zwischensummen und Gesamtsummen direkt nach der Datenmarkierung in der Zeile platziert werden, um Berechnungen auf der Grundlage der eingefügten Daten durchzuführen. Um Berechnungen für die eingefügten Zeilen durchzuführen, verwenden Sie[dynamische Formeln](/cells/de/java/using-smart-markers/#dynamic-formulas).

 Intelligente Marker bestehen aus**Datenquelle** Und**Feldname** Teile für die meisten Informationen. Mit Variablen und Variablenarrays können auch spezielle Informationen übergeben werden. Variablen füllen immer nur eine Zelle, während Variablenarrays mehrere ausfüllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete Smart Marker werden entfernt.

Ein Smart Marker kann auch Parameter enthalten. Mithilfe von Parametern können Sie die Anordnung der Informationen ändern. Sie werden als durch Kommas getrennte Liste in Klammern an das Ende des Smart Markers angehängt.

###  **Smart-Marker-Optionen**

&=DataSource.FieldName
&=[Datenquelle].[Feldname]
&=$Variablenname
&=$VariableArray
&==DynamischeFormel
&=&=RepeatDynamicFormula

###  **Parameter**

Folgende Parameter sind erlaubt:

- **noadd** - Fügen Sie keine zusätzlichen Zeilen hinzu, um die Daten anzupassen.
- **überspringen:n** - Überspringen Sie n Zeilen für jede Datenzeile.
- *aufsteigend:n oder absteigend:n – Daten in Smart Markern sortieren. Wenn n 1 ist, ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach der Verarbeitung der Datenquelle sortiert. Zum Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreiben Sie Daten von links nach rechts statt von oben nach unten.
- **numerisch** - Wandeln Sie Text nach Möglichkeit in eine Zahl um.
- **Schicht** - Nach unten oder rechts verschieben, um zusätzliche Zeilen oder Spalten für die Daten zu erstellen. Der Verschiebungsparameter funktioniert auf die gleiche Weise wie in Microsoft Excel. Wenn Sie beispielsweise in Microsoft Excel einen Zellbereich auswählen, klicken Sie mit der rechten Maustaste und wählen Sie aus**Einfügen** und angeben**Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen. Kurz gesagt erfüllt der Verschiebungsparameter die gleiche Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) Smart Markers.
- **Bohne** – Gibt an, dass die Datenquelle ein einfaches POJO ist. Wird nur in der Version Java API unterstützt.

Die Parameter „noadd“ und „skip“ können kombiniert werden, um Daten in abwechselnden Zeilen einzufügen. Da die Vorlage von unten nach oben verarbeitet wird, sollten Sie noadd in der ersten Zeile hinzufügen, um zu verhindern, dass vor der alternativen Zeile zusätzliche Zeilen eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie diese durch ein Komma, aber ohne Leerzeichen: ParameterA,ParameterB,ParameterC

Die folgenden Screenshots zeigen, wie Sie Daten in jede zweite Zeile einfügen.

![todo:image_alt_text](using-smart-markers_1.png)

**wird...**

![todo:image_alt_text](using-smart-markers_2.png)

###  **Dynamische Formeln**

Mit dynamischen Formeln können Sie Excel-Formeln in Zellen einfügen, selbst wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können für jede eingefügte Zeile wiederholt werden oder nur die Zelle verwenden, in der die Datenmarkierung platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r – Aktuelle Zeilennummer.
- 2, -1 – Offset zur aktuellen Zeilennummer.

Im Folgenden werden eine sich wiederholende dynamische Formel und das daraus resultierende Excel-Arbeitsblatt veranschaulicht.

![todo:image_alt_text](using-smart-markers_3.png)

**wird…**

![todo:image_alt_text](using-smart-markers_4.png)

Cell C1 enthält die Formel =A1*B1, C2 enthält = A2*B2 und C3 = A3*B3.

 Die Verarbeitung der Smart Marker ist sehr einfach. Der folgende Beispielcode zeigt, wie dynamische Formeln in Smart Markers verwendet werden. Wir laden die[Vorlagendatei](templateDynamicFormulas.xlsx) und Testdaten erstellen, die Markierungen verarbeiten, um Daten in die Zellen gegenüber der Markierung zu füllen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

##  **Verwenden von Variablenarrays**

Der folgende Beispielcode zeigt, wie Variablenarrays in Smart Markers verwendet werden. Wir platzieren dynamisch einen variablen Array-Marker in der Zelle A1 des ersten Arbeitsblatts der Arbeitsmappe, der eine Zeichenfolge von Werten enthält, die wir für den Marker festlegen, und verarbeiten die Marker, um Daten in die Zellen gegenüber dem Marker zu füllen. Abschließend speichern wir die Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

##  **Daten gruppieren**

In einigen Excel-Berichten müssen Sie die Daten möglicherweise in Gruppen aufteilen, um das Lesen und Analysieren zu erleichtern. Einer der Hauptzwecke der Aufteilung von Daten in Gruppen besteht darin, Berechnungen (Zusammenfassungsoperationen) für jede Datensatzgruppe durchzuführen.

Mit den intelligenten Markierungen Aspose.Cells können Sie Daten nach Feldsätzen gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen platzieren. Wenn Sie beispielsweise Daten nach „Customers.CustomerID“ gruppieren, können Sie bei jeder Änderung der Gruppe einen zusammenfassenden Datensatz hinzufügen.

###  **Parameter**

Im Folgenden sind einige Smart-Marker-Parameter aufgeführt, die zum Gruppieren von Daten verwendet werden.

####  **Gruppe:normal/zusammenführen/wiederholen**

Wir unterstützen drei Gruppentypen, zwischen denen Sie wählen können.

- **normal** – Der Wert der Gruppierung nach Feld(ern) wird für die entsprechenden Datensätze in der Spalte nicht wiederholt. Stattdessen werden sie einmal pro Datengruppe gedruckt.
- **verschmelzen** – Dasselbe Verhalten wie für den normalen Parameter, außer dass die Zellen in den Gruppierungsfeldern für jeden Gruppensatz zusammengeführt werden.
- **wiederholen** – Der Wert der Gruppierung nach Feld(ern) wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Customers.CustomerID(group:merge)

####  **überspringen**

Überspringt nach jeder Gruppe eine bestimmte Anzahl von Zeilen.

Zum Beispiel &=Employees.EmployeeID(group:normal,skip:1)

####  **ZwischensummeN**

Führt eine Zusammenfassungsoperation für bestimmte Felddaten durch, die sich auf ein Gruppierungsfeld beziehen. Das N stellt Zahlen zwischen 1 und 11 dar, die die Funktion angeben, die bei der Berechnung von Zwischensummen innerhalb einer Datenliste verwendet wird. (1=DURCHSCHNITT, 2=ANZAHL, 3=ANZAHL, 4=MAX, 5=MIN,...9=SUMME usw.) Weitere Einzelheiten finden Sie in der Referenz zur Zwischensumme in der Excel-Hilfe von Microsoft.

Das Format lautet tatsächlich wie folgt:
subtotalN:Ref, wobei sich Ref auf die Gruppierungsspalte bezieht.

Zum Beispiel,

-  &=Products.Units(subtotal9:Products.ProductID) gibt die Zusammenfassungsfunktion an**Einheiten** Feld in Bezug auf die**Produkt ID** Feld in der**Produkte** Tisch.
-  &=Tabx.Col3(subtotal9:Tabx.Col1) gibt die Zusammenfassungsfunktion für an**Spalte3** Feldgruppe nach**Spalte1** in der Tabelle *Tabx**.
-  &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) gibt die Zusammenfassungsfunktion an**SpalteD** Feldgruppe nach**SpalteA** Und**SpalteB** in der Tabelle *Tabelle1**.

##  **Verwendung verschachtelter Objekte**

Aspose.Cells unterstützt verschachtelte Objekte in Smart Markern. Die verschachtelten Objekte sollten einfach sein.

Wir verwenden eine einfache Vorlagendatei. Sehen Sie sich die Designer-Tabelle an, die einige verschachtelte Smart Marker enthält.

**Das erste Arbeitsblatt der Designerdatei mit verschachtelten Smart Markern.**

![todo:image_alt_text](using-smart-markers_5.png)

Das folgende Beispiel zeigt, wie das funktioniert. Das Ausführen des folgenden Codes führt zur folgenden Ausgabe.

**Das erste Arbeitsblatt der Ausgabedatei mit den resultierenden Daten.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

##  **Verwendung einer generischen Liste als verschachteltes Objekt**

Aspose.Cells unterstützt jetzt auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der mit dem folgenden Code generierten Excel-Ausgabedatei. Wie Sie im Screenshot sehen können, enthält ein Lehrerobjekt mehrere verschachtelte Schülerobjekte.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

##  **Verwendung der Eigenschaft HTML von Smart Markers**

Der folgende Beispielcode erläutert die Verwendung der Eigenschaft HTML der Smart Markers. Bei der Verarbeitung wird „Welt“ in „Hello World“ fett angezeigt, da HTML \<b> Etikett.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

##  **Erhalten von Benachrichtigungen beim Zusammenführen von Daten mit Smart Markers**

 Manchmal kann es erforderlich sein, vor dem Abschluss Benachrichtigungen über die Zellreferenz oder den jeweiligen Smart Marker zu erhalten, der verarbeitet wird. Dies kann mit der erreicht werden[**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)Eigentum und[**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)

Beispielcode und ausführliche Erläuterungen finden Sie in diesem Artikel.

- [Erhalten von Benachrichtigungen beim Zusammenführen von Daten mit Smart Markers](/cells/de/java/getting-notifications-while-merging-data-with-smart-markers/)
