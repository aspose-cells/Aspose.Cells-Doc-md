---
title: Arbeiten mit Cells GridWeb
type: docs
weight: 50
url: /de/java/working-with-cells-gridweb/
---
## **Zugriff auf Cells im Arbeitsblatt**
In diesem Thema werden Zellen behandelt, wobei die grundlegendste Funktion von GridWeb betrachtet wird: der Zugriff auf Zellen.

Jedes Arbeitsblatt enthält ein GridCells-Objekt, eine Sammlung von GridCell-Objekten. Ein GridCell-Objekt repräsentiert eine Zelle in Aspose.Cells.GridWeb. Mit GridWeb kann auf jede Zelle zugegriffen werden. Es gibt zwei bevorzugte Methoden:

- [Zugriff auf die Zelle über den Namen](/cells/de/java/working-with-cells-gridweb/).
- [Zugriff auf die Zelle nach Zeilen- und Spaltenindizes](/cells/de/java/working-with-cells-gridweb/).

Nachfolgend wird jeder Ansatz diskutiert.
### **Verwendung des Namens Cell**
Alle Zellen haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridWeb ermöglicht Entwicklern den Zugriff auf jede gewünschte Zelle, indem sie den Zellennamen verwenden. Übergeben Sie einfach den Zellennamen (als Index) an die GridCells-Auflistung des GridWorksheet.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


### **Verwenden von Zeilen- und Spaltenindizes**
Eine Zelle kann auch anhand ihrer Position in Bezug auf Zeilen- und Spaltenindizes erkannt werden. Übergeben Sie einfach die Zeilen- und Spaltenindizes einer Zelle an die GridCells-Auflistung des GridWorksheet. Dieser Ansatz ist schneller als der obige.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
## **Zugreifen auf und Ändern des Werts von Cell**
[Zugriff auf Cells im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) den Zugriff auf Zellen besprochen. Dieses Thema erweitert diese Diskussion, um zu zeigen, wie Sie mit GridWeb API auf Zellwerte zugreifen und diese ändern.
### **Zugriff auf und Änderung des Werts von Cell**
#### **Zeichenfolgenwerte**
 Bevor Sie auf den Wert einer Zelle zugreifen und diesen ändern können, müssen Sie wissen, wie Sie auf Zellen zugreifen. Einzelheiten zu den verschiedenen Ansätzen für den Zugriff auf Zellen finden Sie unter[Zugriff auf Cells im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Jede Zelle hat eine Eigenschaft namens getStringValue(). Sobald auf eine Zelle zugegriffen wird, können Entwickler auf die Methode getStringValue() zugreifen, um auf den Stringwert der Zelle zuzugreifen.

{{% alert color="primary" %}} 

WICHTIG: Fünf Arten von Werten (Boolean, Int, Double, DateTime und String) können in Zellen gespeichert werden, aber die getValue()/setValue()-Methode(n) können nur verwendet werden, um auf den Objektwert zuzugreifen/zu ändern.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
#### **Alle Arten von Werten**
Aspose.Cells. GridWeb bietet auch eine spezielle Methode, putValue, für jede Zelle. Mit dieser Methode ist es möglich, jede Art von Wert (Boolean, Int, Double, DateTime und String) in eine Zelle einzufügen oder zu ändern.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Es gibt auch eine überladene Version der putValue-Methode, die jede Art von Wert im String-Format annehmen und automatisch in einen geeigneten Datentyp konvertieren kann. Um dies zu erreichen, übergeben Sie den booleschen Wert true an einen anderen Parameter der putValue-Methode, wie unten im Beispiel gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
## **Hinzufügen von Formeln zu Cells**
Das wertvollste Feature, das Aspose.Cells.GridWeb bietet, ist die Unterstützung von Formeln oder Funktionen. Aspose.Cells. GridWeb hat eine eigene Formel-Engine, die die Formeln in Arbeitsblättern berechnet. Aspose.Cells. GridWeb unterstützt sowohl eingebaute als auch benutzerdefinierte Funktionen oder Formeln. In diesem Thema wird das Hinzufügen von Formeln zu Zellen mithilfe von Aspose.Cells. GridWeb API im Detail erläutert.
### **Wie fügt man eine Formel hinzu und berechnet sie?**
 Es ist möglich, Formeln in Zellen hinzuzufügen, darauf zuzugreifen und sie zu ändern, indem Sie die Formeleigenschaft einer Zelle verwenden. Aspose.Cells.GridWeb unterstützt benutzerdefinierte Formeln von einfach bis komplex. Aber auch eine Vielzahl eingebauter Funktionen oder Formeln (ähnlich Microsoft Excel) werden mit Aspose.Cells.GridWeb mitgeliefert. Die vollständige Liste der integrierten Funktionen finden Sie hier[Liste der unterstützten Funktionen.](/cells/de/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Die Formelsyntax sollte mit der Excel-Syntax Microsoft kompatibel sein. Beispielsweise müssen alle Formeln mit einem Gleichheitszeichen (=) beginnen.

Um eine Formel programmgesteuert hinzuzufügen, erkennt Aspose.Cells.GridWeb sie als Formel, auch wenn Sie kein **=**-Zeichen verwenden, aber wenn Endbenutzer, die in der GUI arbeiten, es verwenden müssen.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formel zur B3-Zelle hinzugefügt, aber nicht von GridWeb berechnet** 

![todo: Bild_alt_Text](working-with-cells-gridweb_1.png)

Im obigen Screenshot sehen Sie, dass eine Formel zu B3 hinzugefügt, aber noch nicht berechnet wurde. Um alle Formeln zu berechnen, rufen Sie die Methode computeFormula der GridWorksheetCollection des GridWeb-Steuerelements auf, nachdem Sie Formeln wie unten gezeigt zu Arbeitsblättern hinzugefügt haben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

 Benutzer können Formeln auch durch Klicken berechnen**Einreichen**.

**Klicken Sie auf die Schaltfläche Senden von GridWeb** 

![todo: Bild_alt_Text](working-with-cells-gridweb_2.png)

**WICHTIG** : Wenn ein Benutzer auf die klickt**Speichern** oder**Rückgängig machen** Schaltflächen oder die Blattregisterkarten werden alle Formeln von GridWeb automatisch berechnet.

**Formelergebnis nach Berechnung** 

![todo: Bild_alt_Text](working-with-cells-gridweb_3.png)
### **Verweis auf Cells aus anderen Arbeitsblättern**
Mit Aspose.Cells.GridWeb ist es möglich, auf in verschiedenen Arbeitsblättern gespeicherte Werte in ihren Formeln zu verweisen und komplexe Formeln zu erstellen.

Die Syntax zum Verweisen auf einen Zellenwert aus einem anderen Arbeitsblatt lautet SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
## **Datenvalidierung in einer GridCell von GridWeb erstellen**
 Aspose.Cells.GridWeb ermöglicht das Hinzufügen**Datenvalidierung** mit der Methode GridWorksheet.getValidations().add(). Bei dieser Methode müssen Sie die angeben**Cell Bereich** . Wenn Sie jedoch eine Datenvalidierung in einer einzelnen GridCell erstellen möchten, können Sie dies direkt mit der Methode GridCell.createValidation() tun. Ebenso können Sie entfernen**Datenvalidierung** aus einer GridCell mit der Methode GridCell.removeValidation().

 Der folgende Beispielcode erstellt a**Datenvalidierung** in einer Zelle B3. Wenn Sie einen Wert eingeben, der nicht zwischen 20 und 40 liegt, wird die Zelle B3 angezeigt**Validierungsfehler** in Form von**Rot XXXX** wie in diesem Screenshot gezeigt.

![todo: Bild_alt_Text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
## **Erstellen von benutzerdefinierten Befehlsschaltflächen**
Aspose.Cells.GridWeb enthält spezielle Schaltflächen wie Senden, Speichern und Rückgängig. Alle diese Schaltflächen führen bestimmte Aufgaben für Aspose.Cells.GridWeb aus. Es ist auch möglich, benutzerdefinierte Schaltflächen hinzuzufügen, die benutzerdefinierte Aufgaben ausführen. In diesem Thema wird die Verwendung dieser Funktion erläutert.

Der folgende Beispielcode erläutert, wie eine benutzerdefinierte Befehlsschaltfläche erstellt und ihr Click-Ereignis behandelt wird. Sie können ein beliebiges Symbol für Ihre benutzerdefinierte Befehlsschaltfläche verwenden. Zur Veranschaulichung haben wir dieses Bildsymbol verwendet.

![todo: Bild_alt_Text](working-with-cells-gridweb_5.png)

 Wie Sie im folgenden Screenshot sehen können, fügt der Benutzer, wenn er auf die benutzerdefinierte Befehlsschaltfläche klickt, einen Text in Zelle A1 hinzu, der besagt**"Auf meine benutzerdefinierte Befehlsschaltfläche wurde geklickt."**

![todo: Bild_alt_Text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
### **Ereignisbehandlung der benutzerdefinierten Befehlsschaltfläche**
Der folgende Beispielcode erläutert, wie die Ereignisbehandlung einer benutzerdefinierten Befehlsschaltfläche durchgeführt wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
## **Zellen für GridWeb formatieren**
### **Mögliche Nutzungsszenarien**
GridWeb unterstützt jetzt Benutzer bei der Eingabe von Zellendaten im Prozentformat wie 3 %, und die Daten in der Zelle werden automatisch als 3,00 % formatiert. Sie müssen den Zellenstil jedoch auf das Prozentformat festlegen, das entweder GridTableItemStyle.NumberType a 9 oder 10 ist. Die Zahl 9 formatiert 3 % als 3 %, aber die Zahl 10 formatiert 3 % als 3,00 %.

{{% alert color="primary" %}} 

Wenn Sie den Zellenstil nicht auf Prozentformat eingestellt haben, werden die Eingabedaten 3 % als 0,03 angezeigt.

{{% /alert %}} 
### **Geben Sie Cell Daten des GridWeb-Arbeitsblatts im Prozentformat ein**
Der folgende Beispielcode legt die Zelle A1 GridTableItemStyle.NumberType auf 10 fest, daher werden die Eingabedaten 3 % automatisch als 3,00 % formatiert, wie im Screenshot gezeigt.

![todo: Bild_alt_Text](working-with-cells-gridweb_7.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
