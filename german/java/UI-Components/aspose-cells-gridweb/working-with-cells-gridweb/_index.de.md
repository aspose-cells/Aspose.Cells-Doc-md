---
title: Arbeiten mit Cells GridWeb
type: docs
weight: 50
url: /de/java/working-with-cells-gridweb/
---
##  **Zugriff auf Cells im Arbeitsblatt**
In diesem Thema werden Zellen besprochen und dabei die grundlegendste Funktion von GridWeb betrachtet: der Zugriff auf Zellen.

Jedes Arbeitsblatt enthält ein GridCells-Objekt, eine Sammlung von GridCell-Objekten. Ein GridCell-Objekt repräsentiert eine Zelle in Aspose.Cells.GridWeb. Mit GridWeb ist es möglich, auf jede beliebige Zelle zuzugreifen. Es gibt zwei bevorzugte Methoden:

- [Zugriff auf die Zelle über den Namen](/cells/de/java/working-with-cells-gridweb/).
- [Zugriff auf die Zelle über Zeilen- und Spaltenindizes](/cells/de/java/working-with-cells-gridweb/).

Im Folgenden wird jeder Ansatz besprochen.
###  **Verwenden Sie den Namen Cell**
Alle Zellen haben einen eindeutigen Namen. Zum Beispiel A1, A2, B1, B2 usw. Aspose.Cells.GridWeb ermöglicht Entwicklern den Zugriff auf jede gewünschte Zelle über den Zellennamen. Übergeben Sie einfach den Zellennamen (als Index) an die GridCells-Sammlung des GridWorksheets.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyname-Accessingcellbyname.jsp" >}}


###  **Verwenden von Zeilen- und Spaltenindizes**
Eine Zelle kann auch anhand ihrer Position anhand der Zeilen- und Spaltenindizes erkannt werden. Übergeben Sie einfach die Zeilen- und Spaltenindizes einer Zelle an die GridCells-Sammlung des GridWorksheets. Dieser Ansatz ist schneller als der obige.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-Accessingcellbyrowandcolumnindices-Accessingcellbyrowandcolumnindices.jsp" >}}
##  **Auf den Wert einer Cell zugreifen und ihn ändern**
[Zugriff auf Cells im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet) den Zugriff auf Zellen besprochen. Dieses Thema erweitert diese Diskussion, um zu zeigen, wie man mit GridWeb API auf Zellwerte zugreift und diese ändert.
###  **Auf den Wert einer Cell zugreifen und ihn ändern**
####  **String-Werte**
 Bevor Sie auf den Wert einer Zelle zugreifen und diesen ändern, müssen Sie wissen, wie Sie auf Zellen zugreifen. Einzelheiten zu den verschiedenen Ansätzen für den Zugriff auf Zellen finden Sie unter[Zugriff auf Cells im Arbeitsblatt](/cells/de/java/working-with-cells-gridweb/#workingwithcellsgridweb-accessingcellsintheworksheet).

Jede Zelle verfügt über eine Eigenschaft namens getStringValue(). Sobald auf eine Zelle zugegriffen wird, können Entwickler auf die Methode getStringValue() zugreifen, um auf den Zeichenfolgewert der Zelle zuzugreifen.

{{% alert color="primary" %}} 

WICHTIG: Fünf Arten von Werten (Boolean, int, double, DateTime und string) können in Zellen gespeichert werden, aber die Methode(n) getValue()/setValue() kann/können nur zum Zugreifen auf/Ändern von Objektwerten verwendet werden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellStringValue-AccessingModifyingCellStringValue.jsp" >}}
####  **Alle Arten von Werten**
Aspose.Cells.GridWeb stellt außerdem für jede Zelle eine spezielle Methode, putValue, bereit. Mit dieser Methode ist es möglich, beliebige Wertetypen (Boolean, int, double, DateTime und string) in eine Zelle einzufügen oder zu ändern.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCell-AccessingModifyingCell.jsp" >}}



Es gibt auch eine überladene Version der putValue-Methode, die beliebige Werte im String-Format annehmen und automatisch in einen geeigneten Datentyp konvertieren kann. Um dies zu erreichen, übergeben Sie den booleschen Wert true an einen anderen Parameter der putValue-Methode, wie unten im Beispiel gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessingModifyingCellAllTypeValue-AccessingModifyingCellAllTypeValue.jsp" >}}
##  **Hinzufügen von Formeln zur Cells**
Die wertvollste Funktion von Aspose.Cells.GridWeb ist die Unterstützung von Formeln oder Funktionen. Aspose.Cells.GridWeb verfügt über eine eigene Formel-Engine, die die Formeln in Arbeitsblättern berechnet. Aspose.Cells.GridWeb unterstützt sowohl integrierte als auch benutzerdefinierte Funktionen oder Formeln. In diesem Thema wird das Hinzufügen von Formeln zu Zellen mithilfe von Aspose.Cells.GridWeb API im Detail erläutert.
###  **Wie füge ich eine Formel hinzu und berechne sie?**
 Mithilfe der Formeleigenschaft einer Zelle ist es möglich, Formeln in Zellen hinzuzufügen, darauf zuzugreifen und sie zu ändern. Aspose.Cells.GridWeb unterstützt benutzerdefinierte Formeln von einfach bis komplex. Allerdings werden mit Aspose.Cells.GridWeb auch zahlreiche integrierte Funktionen bzw. Formeln (ähnlich Microsoft Excel) mitgeliefert. Die vollständige Liste der integrierten Funktionen finden Sie hier[Liste der unterstützten Funktionen.](/cells/de/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

Die Formelsyntax sollte mit der Excel-Syntax Microsoft kompatibel sein. Beispielsweise müssen alle Formeln mit einem Gleichheitszeichen (=) beginnen.

Um eine Formel programmgesteuert hinzuzufügen, erkennt Aspose.Cells.GridWeb sie als Formel, auch wenn Sie kein *=*-Zeichen verwenden, aber wenn Endbenutzer, die in der GUI arbeiten, es verwenden müssen.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AddingFormulastoCells-AddingFormulastoCells.jsp" >}}



**Formel zur B3-Zelle hinzugefügt, aber nicht von GridWeb berechnet** 

![todo:image_alt_text](working-with-cells-gridweb_1.png)

Im obigen Screenshot können Sie sehen, dass B3 eine Formel hinzugefügt, aber noch nicht berechnet wurde. Um alle Formeln zu berechnen, rufen Sie die Methode „calculeFormula“ der GridWorksheetCollection des GridWeb-Steuerelements auf, nachdem Sie Formeln zu Arbeitsblättern hinzugefügt haben, wie unten gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CalculateFormula-CalculateFormula.jsp" >}}

Benutzer können Formeln auch berechnen, indem sie auf *Senden** klicken.

**Klicken Sie auf die Schaltfläche „Senden“ von GridWeb** 

![todo:image_alt_text](working-with-cells-gridweb_2.png)

**WICHTIG**: Wenn ein Benutzer auf **Speichern** oder**Rückgängig machen** Alle Formeln werden von GridWeb automatisch berechnet.

**Formelergebnis nach der Berechnung** 

![todo:image_alt_text](working-with-cells-gridweb_3.png)
###  **Verweisen auf Cells aus anderen Arbeitsblättern**
Mit Aspose.Cells.GridWeb ist es möglich, in ihren Formeln auf in verschiedenen Arbeitsblättern gespeicherte Werte zu verweisen und so komplexe Formeln zu erstellen.

Die Syntax zum Verweisen auf einen Zellenwert aus einem anderen Arbeitsblatt lautet SheetName!CellName.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-ReferencingCellsfromOtherWorksheets-ReferencingCellsfromOtherWorksheets.jsp" >}}
##  **Erstellen Sie eine Datenvalidierung in einer GridCell von GridWeb**
 Aspose.Cells.GridWeb ermöglicht das Hinzufügen**Datenvalidierung** mit der Methode GridWorksheet.getValidations().add(). Bei dieser Methode müssen Sie angeben**Cell Bereich**. Wenn Sie jedoch eine Datenvalidierung in einer einzelnen GridCell erstellen möchten, können Sie dies direkt mit der Methode GridCell.createValidation() tun. Ebenso können Sie **Datenvalidierung entfernen** aus einer GridCell mit der Methode GridCell.removeValidation().

 Der folgende Beispielcode erstellt eine**Datenvalidierung** in einer Zelle B3. Wenn Sie einen Wert eingeben, der nicht zwischen 20 und 40 liegt, wird Zelle B3 angezeigt**Validierungsfehler** in Form von**Rot XXXX** wie in diesem Screenshot gezeigt.

![todo:image_alt_text](working-with-cells-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreateDataValidationinGridCellofGridWeb-CreateDataValidationinGridCellofGridWeb.jsp" >}}
##  **Erstellen benutzerdefinierter Befehlsschaltflächen**
Aspose.Cells.GridWeb enthält spezielle Schaltflächen wie Senden, Speichern und Rückgängig. Alle diese Schaltflächen führen spezifische Aufgaben für Aspose.Cells.GridWeb aus. Es ist auch möglich, benutzerdefinierte Schaltflächen hinzuzufügen, die benutzerdefinierte Aufgaben ausführen. In diesem Thema wird erläutert, wie Sie diese Funktion verwenden.

Der folgende Beispielcode erklärt, wie Sie eine benutzerdefinierte Befehlsschaltfläche erstellen und wie das Klickereignis behandelt wird. Sie können jedes beliebige Symbol für Ihre benutzerdefinierte Befehlsschaltfläche verwenden. Zur Veranschaulichung haben wir dieses Bildsymbol verwendet.

![todo:image_alt_text](working-with-cells-gridweb_5.png)

 Wie Sie im folgenden Screenshot sehen können, fügt der Benutzer, wenn er auf die benutzerdefinierte Befehlsschaltfläche klickt, einen Text in Zelle A1 hinzu:**„Meine benutzerdefinierte Befehlsschaltfläche wurde angeklickt.“**

![todo:image_alt_text](working-with-cells-gridweb_6.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-CreatingCustomCommandButtons-CreatingCustomCommandButtons.jsp" >}}
###  **Ereignisbehandlung der benutzerdefinierten Befehlsschaltfläche**
Der folgende Beispielcode erklärt, wie die Ereignisbehandlung einer benutzerdefinierten Befehlsschaltfläche durchgeführt wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EventHandlingofCustomCommandButton-EventHandlingofCustomCommandButton.jsp" >}}
##  **Zellen für GridWeb formatieren**
###  **Mögliche Nutzungsszenarien**
GridWeb unterstützt Benutzer jetzt bei der Eingabe von Zelldaten im Prozentformat wie 3 %, und die Daten in der Zelle werden automatisch als 3,00 % formatiert. Allerdings müssen Sie den Zellenstil auf „Prozentformat“ einstellen, das entweder „GridTableItemStyle.NumberType“ oder „9“ oder „10“ ist. Die Zahl 9 formatiert 3 % als 3 %, aber die Zahl 10 formatiert 3 % als 3,00 %.

{{% alert color="primary" %}} 

Wenn Sie den Zellenstil nicht auf „Prozentformat“ eingestellt haben, werden die Eingabedaten 3 % als 0,03 angezeigt.

{{% /alert %}} 
###  **Geben Sie Cell Daten des GridWeb-Arbeitsblatts im Prozentformat ein**
Der folgende Beispielcode setzt die Zelle A1 GridTableItemStyle.NumberType auf 10, daher werden die Eingabedaten 3 % automatisch als 3,00 % formatiert, wie im Screenshot gezeigt.

![todo:image_alt_text](working-with-cells-gridweb_7.png)
###  **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}
