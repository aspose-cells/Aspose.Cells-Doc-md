---
title: Arbeiten mit Cells GridWeb
type: docs
weight: 50
url: /de/java/working-with-cells-gridweb/
---

## **Zugriff auf Zellen im Arbeitsblatt**
In diesem Thema werden Zellen behandelt und die grundlegendste Funktion von GridWeb betrachtet: der Zugriff auf Zellen.

Jedes Arbeitsblatt enthält ein GridCells-Objekt, das eine Sammlung von GridCell-Objekten darstellt. Ein GridCell-Objekt repräsentiert eine Zelle in Aspose.Cells.GridWeb. Es ist möglich, auf jede Zelle über GridWeb zuzugreifen. Es gibt zwei bevorzugte Methoden:

- [Zugriff auf die Zelle nach Name](/cells/de/java/working-with-cells-gridweb/).
- [Zugriff auf die Zelle nach Zeilen- und Spaltenindizes](/cells/de/java/working-with-cells-gridweb/).

Im Folgenden wird jede Methode erläutert.
### **Verwendung des Zellnamens**
Alle Zellen haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridWeb ermöglicht Entwicklern den Zugriff auf beliebige gewünschte Zellen, indem sie den Zellnamen (als Index) an die GridCells-Sammlung des GridArbeitsblatts übergeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Verwendung von Zeilen- und Spaltenindizes**
Eine Zelle kann auch anhand ihrer Position in Bezug auf Zeilen- und Spaltenindizes erkannt werden. Geben Sie einfach die Zeilen- und Spaltenindizes einer Zelle an die GridCells-Sammlung des GridArbeitsblatts weiter. Dieser Ansatz ist schneller als der zuvor genannte.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Zugriff und Änderung des Werts einer Zelle**
[Zugriff auf Zellen im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) behandelt den Zugriff auf Zellen. Dieses Thema erweitert die Diskussion, um zu zeigen, wie auf Zellwerte mit Hilfe der GridWeb-API zugegriffen und diese geändert werden können.
### **Zugriff und Ändern des Zellwerts**
#### **Zeichenfolgenwerte**
Bevor Sie auf den Wert einer Zelle zugreifen und diesen ändern, müssen Sie wissen, wie Sie auf Zellen zugreifen. Für Details zu den verschiedenen Ansätzen zum Zugriff auf Zellen siehe [Zugriff auf Zellen im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Jede Zelle hat eine Eigenschaft namens getStringValue(). Sobald auf eine Zelle zugegriffen wird, können Entwickler die Methode getStringValue() aufrufen, um auf den Zeichenfolgenwert der Zelle zuzugreifen.

{{% alert color="primary" %}} 

WICHTIG: In Zellen können fünf Arten von Werten (Boolean, int, double, DateTime und String) gespeichert werden, aber die Methode(n) getValue()/setValue() kann/können nur verwendet werden, um den Objektwert zu lesen/zu ändern.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Alle Arten von Werten**
Aspose.Cells.GridWeb bietet auch eine spezielle Methode, putValue, für jede Zelle. Mit dieser Methode ist es möglich, jeden Wertetyp (Boolean, int, double, DateTime und String) in eine Zelle einzufügen oder zu ändern.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Es gibt auch eine überladene Version der putValue-Methode, die jeden beliebigen Wert in Zeichenfolgenformat akzeptieren und automatisch in einen geeigneten Datentyp konvertieren kann. Um dies zu erreichen, übergeben Sie dem putValue der Methode einen weiteren Parameter mit dem Wert true, wie im folgenden Beispiel gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Hinzufügen von Formeln zu den Zellen**
Das wertvollste Feature, das von Aspose.Cells.GridWeb angeboten wird, ist die Unterstützung von Formeln oder Funktionen. Aspose.Cells.GridWeb verfügt über seinen eigenen Formel-Engine, die die Formeln in Arbeitsblättern berechnet. Aspose.Cells.GridWeb unterstützt sowohl eingebaute als auch benutzerdefinierte Funktionen oder Formeln. Dieses Thema erläutert ausführlich, wie Formeln mithilfe der Aspose.Cells.GridWeb-API zu Zellen hinzugefügt werden.
### **Wie füge ich eine Formel hinzu und berechne sie?**
Es ist möglich, Formeln in Zellen hinzuzufügen, darauf zuzugreifen und sie zu ändern, indem Sie die Formel-Eigenschaft einer Zelle verwenden. Aspose.Cells.GridWeb unterstützt benutzerdefinierte Formeln von einfach bis komplex. Es sind jedoch auch viele eingebaute Funktionen oder Formeln (ähnlich wie in Microsoft Excel) in Aspose.Cells.GridWeb verfügbar. Eine vollständige Liste der unterstützten Funktionen finden Sie unter diesem [Liste der unterstützten Funktionen.](/cells/de/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Die Formelsyntax muss mit der Microsoft Excel-Syntax kompatibel sein. Alle Formeln müssen beispielsweise mit einem Gleichheitszeichen (=) beginnen.

Um eine Formel programmgesteuert hinzuzufügen, erkennt Aspose.Cells.GridWeb diese auch dann als Formel, wenn Sie kein **=**-Zeichen verwenden. Wenn Endbenutzer in der GUI arbeiten, müssen sie es jedoch verwenden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formel zu Zelle B3 hinzugefügt, aber nicht durch GridWeb berechnet** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

Auf dem obigen Screenshot ist zu sehen, dass eine Formel zu B3 hinzugefügt wurde, aber bisher nicht berechnet wurde. Um alle Formeln zu berechnen, rufen Sie nach dem Hinzufügen von Formeln zu Arbeitsblättern die Methode calculateFormula der GridWorksheetCollection des GridWeb-Steuerung auf, wie unten gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Benutzer können auch Formeln durch Klicken auf **Senden** berechnen.

**Klicken Sie auf die Schaltfläche Senden von GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**WICHTIG**: Wenn ein Benutzer auf die Schaltflächen **Speichern** oder **Rückgängig** oder auf die Blattregisterkarten klickt, werden alle Formeln automatisch von GridWeb berechnet.

**Formelergebnis nach Berechnung** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
### **Bezugnahme auf Zellen aus anderen Arbeitsblättern**
Mit Aspose.Cells.GridWeb ist es möglich, Werte in verschiedenen Arbeitsblättern in ihren Formeln zu referenzieren und komplexe Formeln zu erstellen.

Die Syntax zum Referenzieren eines Zellwerts aus einem anderen Arbeitsblatt lautet Arbeitsblattname!Zellenname.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Erstellen einer Datenvalidierung in einer GridCell von GridWeb**
Aspose.Cells.GridWeb ermöglicht es Ihnen, **Datenvalidierungen** mithilfe der GridWorksheet.getValidations().add() Methode hinzuzufügen. Mit dieser Methode müssen Sie den **Zellenbereich** angeben. Wenn Sie jedoch eine Datenvalidierung in einer einzelnen GridCell erstellen möchten, können Sie dies direkt mit der GridCell.createValidation() Methode tun. Ebenso können Sie eine **Datenvalidierung** aus einer GridCell mit der GridCell.removeValidation() Methode entfernen.

Der folgende Beispielcode erstellt eine **Datenvalidierung** in einer Zelle B3. Wenn Sie einen Wert eingeben, der nicht zwischen 20 und 40 liegt, wird die Zelle B3 **Validierungsfehler** in Form von **Roten XXXX** anzeigen, wie im Screenshot gezeigt.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Erstellen von benutzerdefinierten Befehlsschaltflächen**
Aspose.Cells.GridWeb enthält spezielle Schaltflächen wie Senden, Speichern und Rückgängig. All diese Schaltflächen führen spezifische Aufgaben für Aspose.Cells.GridWeb aus. Es ist auch möglich, benutzerdefinierte Schaltflächen hinzuzufügen, die benutzerdefinierte Aufgaben ausführen. In diesem Thema wird erläutert, wie diese Funktion verwendet wird.

Der folgende Beispielcode erläutert, wie eine benutzerdefinierte Befehlsschaltfläche erstellt und ihr Klickereignis behandelt wird. Sie können jedes Symbol für Ihre benutzerdefinierte Befehlsschaltfläche verwenden. Zu Illustrationszwecken haben wir dieses Bildsymbol verwendet.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

Wie Sie auf dem folgenden Screenshot sehen können, fügt der Benutzer beim Klicken auf die benutzerdefinierte Befehlsschaltfläche einen Text in Zelle A1 ein, der lautet: **"Meine benutzerdefinierte Befehlsschaltfläche wurde angeklickt."**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Eventbehandlung der benutzerdefinierten Befehlsschaltfläche**
Der folgende Beispielcode erläutert, wie die Eventbehandlung der benutzerdefinierten Befehlsschaltfläche durchgeführt wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Zellformatierung für GridWeb**
### **Mögliche Verwendungsszenarien**
GridWeb unterstützt jetzt Benutzer dabei, Zelldaten im Prozentformat wie 3% einzugeben, und die Daten in der Zelle werden automatisch als 3,00% formatiert. Sie müssen jedoch den Zellstil auf Prozentformat setzen, welches entweder GridTableItemStyle.NumberType 9 oder 10 ist. Die Nummer 9 wird 3% als 3% formatieren, aber die Nummer 10 wird 3% als 3,00% formatieren.

{{% alert color="primary" %}} 

Wenn Sie den Zellstil nicht auf Prozentformat gesetzt haben, wird die Eingabedaten 3% als 0,03 angezeigt.

{{% /alert %}} 
### **Eingabe von Zelldaten des GridWeb-Arbeitsblatts im Prozentformat**
Der folgende Beispielcode setzt die Zelle A1 GridTableItemStyle.NumberType auf 10. Daher wird die Eingabedaten 3% automatisch als 3,00% formatiert, wie im Screenshot gezeigt.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
