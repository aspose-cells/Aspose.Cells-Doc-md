---
title: Verwendung von Smart Markern
type: docs
weight: 40
url: /de/java/using-smart-markers/
---

## **Einführung**

{{% alert color="primary" %}}

**Smart Marker** werden verwendet, um Aspose.Cells mitzuteilen, welche Informationen in einer Microsoft Excel [designer spreadsheet](/cells/de/java/what-is-a-designer-spreadsheet/) platziert werden sollen. Smart Marker ermöglichen es Ihnen, Vorlagen zu erstellen, die nur relevante Informationen und Formatierungen enthalten.

{{% /alert %}}

## **Designer-Tabelle & Intelligente Marker**

Designer-Tabellenkalkulationen sind standardmäßige Excel-Dateien, die visuelles Formatieren, Formeln und intelligente Markierungen enthalten. Sie können intelligente Markierungen enthalten, die auf eine oder mehrere Datenquellen verweisen, wie Informationen aus einem Projekt und Informationen zu verwandten Kontakten. Intelligente Markierungen werden in die Zellen geschrieben, in denen Sie Informationen wünschen.

Alle intelligente Markierungen beginnen mit &=. Ein Beispiel für eine Datenmarkierung ist &=Party.FullName. Wenn die Datenmarkierung zu mehr als einem Element führt, z. B. einer vollständigen Zeile, werden die folgenden Zeilen automatisch nach unten verschoben, um Platz für die neuen Informationen zu schaffen. Dadurch können Zwischensummen und Gesamtsummen in der Zeile unmittelbar nach der Datenmarkierung platziert werden, um Berechnungen basierend auf eingefügten Daten durchzuführen. Um Berechnungen auf den eingefügten Zeilen durchzuführen, verwenden Sie [Dynamische Formeln](/cells/de/java/using-smart-markers/#dynamic-formulas).

Intelligente Marker bestehen aus den Teilen **Datenquelle** und **Feldname** für die meisten Informationen. Spezielle Informationen können auch mit Variablen und Variablenarrays übergeben werden. Variablen füllen immer nur eine Zelle aus, während Variablenarrays mehrere Zellen ausfüllen können. Verwenden Sie nur einen Datenmarker pro Zelle. Nicht verwendete intelligente Marker werden entfernt.

Eine intelligente Markierung kann auch Parameter enthalten. Parameter ermöglichen es Ihnen, die Anordnung der Informationen zu modifizieren. Sie werden als kommaseparierte Liste am Ende der intelligenten Markierung in Klammern angehängt.

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
- *aufsteigend:n oder absteigend:n - Sortiert Daten in intelligenten Markierungen. Wenn n gleich 1 ist, dann ist die Spalte der erste Schlüssel des Sortierers. Die Daten werden nach der Bearbeitung der Datenquelle sortiert. Zum Beispiel: &=Tabelle1.Feld3(aufsteigend:1).
- **horizontal** - Schreibe Daten von links nach rechts anstatt von oben nach unten.
- **numeric** - Konvertiere Text in eine Zahl, wenn möglich.
- **shift** - Verschiebt nach unten oder rechts und erstellt zusätzliche Zeilen oder Spalten, um die Daten anzupassen. Der Shift-Parameter funktioniert genauso wie in Microsoft Excel. Zum Beispiel in Microsoft Excel, wenn Sie einen Zellenbereich auswählen, mit der rechten Maustaste klicken und **Einfügen** wählen und **Zellen nach unten verschieben**, **Zellen nach rechts verschieben** und andere Optionen angeben. Kurz gesagt erfüllt der Shift-Parameter dieselbe Funktion für vertikale/normale (von oben nach unten) oder horizontale (von links nach rechts) intelligente Markierungen.
- **bean** - Gibt an, dass die Datenquelle ein einfaches POJO ist. Nur im Java API unterstützt.

Die Parameter noadd und skip können kombiniert werden, um Daten in wechselnden Zeilen einzufügen. Da die Vorlage von unten nach oben bearbeitet wird, sollten Sie noadd in der ersten Zeile hinzufügen, um zu vermeiden, dass zusätzliche Zeilen vor der alternierenden Zeile eingefügt werden.

Wenn Sie mehrere Parameter haben, trennen Sie diese mit einem Komma, aber ohne Leerzeichen: ParameterA,ParameterB,ParameterC

Die folgenden Screenshots zeigen, wie Daten in jeder zweiten Zeile eingefügt werden.

![todo:image_alt_text](using-smart-markers_1.png)

**wird zu...**

![todo:image_alt_text](using-smart-markers_2.png)

### **Dynamische Formeln**

Dynamische Formeln ermöglichen es Ihnen, Excel-Formeln in Zellen einzufügen, auch wenn die Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Dynamische Formeln können für jede eingefügte Zeile wiederholt werden oder nur die Zelle verwenden, in der der Datenmarker platziert ist.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- r - Aktuelle Zeilennummer.
- 2, -1 - Versatz zur aktuellen Zeilennummer.

Das folgende illustriert eine wiederholte dynamische Formel und das resultierende Excel-Arbeitsblatt.

![todo:image_alt_text](using-smart-markers_3.png)

**wird zu...**

![todo:image_alt_text](using-smart-markers_4.png)

Zelle C1 enthält die Formel =A1*B1, C2 enthält = A2*B2 und C3 = A3*B3.

Es ist sehr einfach, die Smart Marker zu verarbeiten. Im folgenden Beispielcode wird gezeigt, wie dynamische Formeln in Smart Markers verwendet werden. Wir laden die [Template-Datei](templateDynamicFormulas.xlsx) und erstellen Testdaten, um die Marker zu verarbeiten, um Daten in die Zellen gegen den Marker einzufügen. 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-DynamicFormulas-DynamicFormulas.java" >}}

## **Verwendung von Variablen Arrays**

Das folgende Beispiel zeigt, wie variable Arrays in Smart Markers verwendet werden. Wir platzieren einen variablen Array-Marker in die Zelle A1 des ersten Arbeitsblatts der Arbeitsmappe dynamisch, der eine Zeichenfolge von Werten enthält, die wir für die Markierung festlegen. Wir verarbeiten die Markierungen, um Daten in die Zellen gegen die Markierung einzufügen. Schließlich speichern wir die Excel-Datei.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingVariableArray-UsingVariableArray.java" >}}

## **Daten gruppieren**

In einigen Excel-Berichten ist es möglicherweise erforderlich, die Daten in Gruppen aufzuteilen, um sie einfacher zu lesen und zu analysieren. Ein Hauptzweck, Daten in Gruppen aufzuteilen, besteht darin, Berechnungen (Zusammenfassungsoperationen) für jede Gruppe von Datensätzen auszuführen.

Aspose.Cells Smart Markers ermöglichen es Ihnen, Daten nach Feldern zu gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen zu platzieren. Wenn Sie z. B. Daten nach Kunden.CustomerID gruppieren, können Sie jedes Mal, wenn sich die Gruppe ändert, einen Zusammenfassungseintrag hinzufügen.

### **Parameter**

Nachfolgend einige intelligente Markierungsparameter, die zur Gruppierung von Daten verwendet werden.

#### **group:normal/merge/repeat**

Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- **normal** - Der Gruppenwert wird nicht für die entsprechenden Datensätze in der Spalte wiederholt; stattdessen wird er einmal pro Datengruppe gedruckt.
- **merge** - Das gleiche Verhalten wie beim normalen Parameter, außer dass die Zellen im Gruppenwert für jede Gruppeneinstellung zusammengeführt werden.
- **repeat** - Der Gruppenwert wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Kunden.KundenID(group:merge)

#### **skip**

Überspringt eine bestimmte Anzahl von Zeilen nach jeder Gruppe.

Zum Beispiel &=Mitarbeiter.MitarbeiterID(group:normal,skip:1)

#### **subtotalN**

Führt eine Zusammenfassungsoperation für ein spezifisches Felddatum in Bezug auf ein Gruppenfeld durch. Das N stellt Zahlen zwischen 1 und 11 dar, die die Funktion spezifizieren, die beim Berechnen von Zwischensummen innerhalb einer Liste von Daten verwendet wird. (1=DURCHSCHNITT, 2=ANZAHL, 3=ANZAHL2, 4=MAX, 5=MIN,...9=SUMME usw.) Siehe die Zwischensumme-Referenz in der Hilfe von Microsoft Excel für weitere Details.

Das Format gibt tatsächlich an:
subtotalN:Verweis, wobei Verweis sich auf die Gruppierungs-Spalte bezieht.

Zum Beispiel,

- &=Products.Units(subtotal9:Products.ProductID) legt die Zusammenfassungsfunktion auf das **Units** Feld in Bezug auf das **ProductID** Feld in der Tabelle **Products** fest.
- &=Tabx.Col3(subtotal9:Tabx.Col1) legt die Zusammenfassungsfunktion auf das **Col3** Feld gruppiert nach **Col1** in der Tabelle **Tabx** fest.
- &=Tabelle1.SpalteD(subtotal9:Tabelle1.SpalteA&Tabelle1.SpalteB) gibt die Zusammenfassungsfunktion für das Feld **SpalteD** gruppiert nach **SpalteA** und **SpalteB** in Tabelle **Tabelle1** an.

## **Verwendung von verschachtelten Objekten**

Aspose.Cells unterstützt verschachtelte Objekte in intelligenten Markierungen. Die verschachtelten Objekte sollten einfach sein.

Wir verwenden eine einfache Vorlagendatei. Siehe die Designer-Arbeitsmappe, die einige verschachtelte Smart-Markierungen enthält.

**Das erste Arbeitsblatt der Designer-Datei zeigt verschachtelte Smart Marker.**

![todo:image_alt_text](using-smart-markers_5.png)

Das folgende Beispiel zeigt, wie das funktioniert. Wenn der folgende Code ausgeführt wird, ergibt sich unten stehende Ausgabe.

**Das erste Arbeitsblatt der Ausgabedatei zeigt die resultierenden Daten.**

![todo:image_alt_text](using-smart-markers_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingNestedObjects-UsingNestedObjects.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Individual-Individual.java" >}}

## **Verwendung von generischer Liste als verschachteltes Objekt**

Aspose.Cells unterstützt jetzt auch die Verwendung einer generischen Liste als verschachteltes Objekt. Bitte überprüfen Sie den Screenshot der Ausgabedatei, die mit folgendem Code generiert wurde. Wie Sie im Screenshot sehen können, enthält ein Teacher-Objekt mehrere verschachtelte Studentenobjekte.

![todo:image_alt_text](using-smart-markers_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingGenericList-UsingGenericList.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Teacher-Teacher.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-Person-Person.java" >}}

## **Verwendung der HTML-Eigenschaften von Smart Markern**

The following sample code explains the use of the HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML \<b> tag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-SmartMarkers-UsingHTMLProperty-UsingHTMLProperty.java" >}}

## **Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten**

Manchmal ist es erforderlich, Benachrichtigungen über den Zellenverweis oder den bestimmten Smart Marker zu erhalten, der vor Abschluss verarbeitet wird. Dies kann mit der [**WorkbookDesigner.CallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack)-Eigenschaft und [**ISmartMarkerCallBack**](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) erreicht werden

Für Beispielcode und detaillierte Erklärung sehen Sie bitte diesen Artikel.

- [Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten](/cells/de/java/getting-notifications-while-merging-data-with-smart-markers/)
{{< app/cells/assistant language="java" >}}
