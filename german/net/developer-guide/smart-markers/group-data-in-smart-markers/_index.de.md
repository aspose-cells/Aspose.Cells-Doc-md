---
title: Wie man Daten in Smart Markern gruppiert
type: docs
weight: 30
url: /de/net/how-to-group-data-in-smart-markers/
---

## **Mögliche Verwendungsszenarien**
In einigen Excel-Berichten ist es möglicherweise erforderlich, die Daten in Gruppen aufzuteilen, um sie einfacher zu lesen und zu analysieren. Ein Hauptzweck, Daten in Gruppen aufzuteilen, besteht darin, Berechnungen (Zusammenfassungsoperationen) für jede Gruppe von Datensätzen auszuführen.

Aspose.Cells Smart Marker ermöglicht es Ihnen, Daten nach Feldern zu gruppieren und Zusammenfassungszeilen zwischen Datensätzen oder Datengruppen zu platzieren. Wenn beispielsweise die Daten nach Kunden.CustomerID gruppiert werden, können Sie jedes Mal einen Zusammenfassungsdatensatz hinzufügen, wenn sich die Gruppe ändert.

## **Gruppierungsparameter in Smart Markern**
Im Folgenden sind einige der Smart-Marker-Parameter aufgeführt, die für die Gruppierung von Daten verwendet werden.
### **group:normal/merge/repeat**
Wir unterstützen drei Arten von Gruppen, zwischen denen Sie wählen können.

- **normal** - Der Gruppenwert wird nicht für die entsprechenden Datensätze in der Spalte wiederholt; stattdessen wird er einmal pro Datengruppe gedruckt.
- **merge** - Das gleiche Verhalten wie beim normalen Parameter, außer dass die Zellen im Gruppenwert für jede Gruppeneinstellung zusammengeführt werden.
- **repeat** - Der Gruppenwert wird für die entsprechenden Datensätze wiederholt.

Zum Beispiel: &=Kunden.KundenID(group:merge)
### **skip**
Überspringt eine bestimmte Anzahl von Zeilen nach jeder Gruppe.

Zum Beispiel: &=Mitarbeiter.MitarbeiterID(group:normal,skip:1)
### **subtotalN**
Führt eine Zusammenfassungsoperation für ein spezifisches Felddatum in Bezug auf ein Gruppenfeld durch. Das N stellt Zahlen zwischen 1 und 11 dar, die die Funktion spezifizieren, die beim Berechnen von Zwischensummen innerhalb einer Liste von Daten verwendet wird. (1=DURCHSCHNITT, 2=ANZAHL, 3=ANZAHL2, 4=MAX, 5=MIN,...9=SUMME usw.) Siehe die Zwischensumme-Referenz in der Hilfe von Microsoft Excel für weitere Details.

Das Format gibt tatsächlich an:
subtotalN:Verweis, wobei Verweis sich auf die Gruppierungs-Spalte bezieht.

Zum Beispiel,

- &=Products.Units(subtotal9:Products.ProductID) legt die Zusammenfassungsfunktion auf das **Units** Feld in Bezug auf das **ProductID** Feld in der Tabelle **Products** fest.
- &=Tabx.Col3(subtotal9:Tabx.Col1) legt die Zusammenfassungsfunktion auf das **Col3** Feld gruppiert nach **Col1** in der Tabelle **Tabx** fest.
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) legt die Zusammenfassungsfunktion auf das **ColumnD** Feld gruppiert nach **ColumnA** und **ColumnB** in der Tabelle **Table1** fest.

## **Wie man Daten in Smart Markern gruppiert**

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
