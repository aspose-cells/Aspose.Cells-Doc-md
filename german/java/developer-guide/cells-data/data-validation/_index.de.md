---
title: Datenvalidierung
type: docs
weight: 70
url: /de/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel bietet einige gute Funktionen zur Auto-Filterung oder Validierung von Arbeitsblattdaten.

[Datenvalidierung](/cells/de/java/data-validation/) bezieht sich auf die Möglichkeit, Regeln für die in einem Arbeitsblatt eingegebenen Daten festzulegen. Verwenden Sie beispielsweise eine Validierung, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATUM nur Datumsangaben enthält oder dass eine andere Spalte nur Zahlen enthält. Sie können sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATUM nur Daten innerhalb eines bestimmten Bereichs enthält. Mit der Datenvalidierung können Sie steuern, was in Zellen im Arbeitsblatt eingegeben wird. Aspose.Cells unterstützt vollständig die Datenvalidierung und AutoFilter-Funktionen von Microsoft Excel. Dieser Artikel erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und sie mit Aspose.Cells codieren.

{{% /alert %}} 
## **Datenvalidierungstypen und Ausführung**
Microsoft Excel unterstützt verschiedene Arten von Datenvalidierungen. Jede Art wird verwendet, um zu steuern, welche Art von Daten in eine Zelle oder Zellbereich eingegeben wird. Nachfolgend werden Codeausschnitte illustriert, wie überprüft wird, dass:

- [Zahlen ganzzahlig sind](/cells/de/java/data-validation/), also keine Nachkommastellen haben.
- [Dezimalzahlen die richtige Struktur aufweisen](/cells/de/java/data-validation/). Das Codebeispiel definiert, dass ein Zellenbereich zwei Dezimalstellen haben sollte.
- [Werte auf eine Liste von Werten beschränkt sind](/cells/de/java/data-validation/). Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder Zellenbereich angewendet werden können.
- [Daten in einen bestimmten Bereich fallen](/cells/de/java/data-validation/).
- [Zeiten innerhalb eines bestimmten Bereichs liegen](/cells/de/java/data-validation/).
- [Ein Text eine bestimmte Zeichenlänge hat](/cells/de/java/data-validation/).
### **Datenvalidierung mit Microsoft Excel**
Um Validierungen mit Microsoft Excel zu erstellen:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Überprüfung anwenden möchten.
1. Wählen Sie im **Daten**-Menü die **Validierung** aus.
   Der Validierungsdialog wird angezeigt.
1. Klicken Sie auf die Registerkarte **Einstellungen** und geben Sie die Einstellungen wie unten gezeigt ein. 

   **Datenvalidierungseinstellungen** 

![todo:image_alt_text](data-validation_1.png)
### **Datumsvalidierung mit Aspose.Cells**
Die Datenvalidierung ist eine leistungsstarke Funktion zur Überprüfung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste bereitstellen, Daten eingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
In Aspose.Cells hat jede [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) eine [Validierungen](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)-Objekt, das eine Sammlung von [Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)-Objekten darstellt. Um die Validierung einzurichten, legen Sie einige Eigenschaften der [Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)-Klasse fest:

- [Typ](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): stellt den Validierungstyp dar, der durch Verwendung eines der vordefinierten Werte in der [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)-Aufzählung angegeben werden kann.
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): stellt den Operator dar, der bei der Validierung verwendet werden soll, der durch Verwendung eines der vordefinierten Werte in der [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)-Aufzählung angegeben werden kann.
- [Formel1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): stellt den Wert oder den Ausdruck dar, der mit dem ersten Teil der Datenvalidierung verbunden ist.
- [Formel2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): stellt den Wert oder den Ausdruck dar, der mit dem zweiten Teil der Datenvalidierung verbunden ist.

Wenn die Eigenschaften des [Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)-Objekts konfiguriert wurden, können Entwickler die [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)-Struktur verwenden, um Informationen über den Zellbereich zu speichern, der unter Verwendung der erstellten Validierung überprüft wird.
#### **Arten der Datenvalidierung**
Datenvalidierung ermöglicht es Ihnen, Geschäftsregeln in jede Zelle zu integrieren, sodass falsche Eingaben zu Fehlermeldungen führen. Geschäftsregeln sind die Richtlinien und Verfahren, nach denen ein Unternehmen betrieben wird. Aspose.Cells unterstützt alle wichtigen Arten der Datenvalidierung.

Die [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)-Aufzählung hat die folgenden Elemente:

|**Member Name**|**Description**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY-VALUE)| Bezeichnet einen Wert jeglichen Typs.|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER)| Bezeichnet Validierungstyp für ganze Zahlen.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Bezeichnet den Validierungstyp für Dezimalzahlen.
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Bezeichnet den Validierungstyp für Dropdown-Listen.
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Bezeichnet den Validierungstyp für Daten.
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Bezeichnet den Validierungstyp für Zeit.
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT-LENGTH)| Bezeichnet Validierungstyp für die Länge des Textes.|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Bezeichnet den benutzerdefinierten Validierungstyp.
#### **Programmbeispiel: Validierung ganzer Zahlen**
Mit dieser Validierungsart können Benutzer nur ganze Zahlen innerhalb eines festgelegten Bereichs in die validierten Zellen eingeben. Die folgenden Codebeispiele zeigen, wie man den Validierungstyp [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE-NUMBER) implementiert. Das Beispiel erstellt die gleiche Datenvalidierung mit Aspose.Cells, die wir zuvor in Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programmbeispiel: Dezimalstellen-Validierung**
Mit diesem Typ der Validierung kann der Benutzer Dezimalzahlen in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, nur Dezimalwerte einzugeben, und der Validierungsbereich ist A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programmbeispiel: Listen-Validierung**
Dieser Typ der Validierung ermöglicht es dem Benutzer, Werte aus einer Dropdown-Liste einzugeben. Es wird eine Liste bereitgestellt: eine Reihe von Zeilen mit Daten. Benutzer können nur Werte aus der Liste auswählen. Der Validierungsbereich ist der Zellenbereich A1:A5 im ersten Arbeitsblatt.

Es ist wichtig, dass Sie die Eigenschaft [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) auf **true** setzen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programmbeispiel: Datum-Validierung**
Bei diesem Validierungstyp gibt der Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder gemäß bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer darauf beschränkt, Daten zwischen 1970 und 1999 einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programmbeispiele: Zeit-Validierung**
Bei diesem Typ der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder gemäß bestimmter Kriterien in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeiten zwischen 09:00 und 11:30 Uhr einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programmbeispiele: Textlängen-Validierung**
Bei diesem Validierungstyp können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Datenvalidierungsregeln**
Wenn Datenvalidierungen implementiert sind, kann die Validierung durch Zuweisung verschiedener Werte in den Zellen überprüft werden. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel zeigt diese Funktion mit verschiedenen Werten. Die Testdatei kann zum Testen von folgendem Link heruntergeladen werden:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Überprüfen, ob die Validierung in einer Zelle eine Dropdown-Liste ist**
Wie wir gesehen haben, gibt es viele Arten von Validierungen, die in einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob die Validierung Dropdown ist oder nicht, kann die Eigenschaft [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) verwendet werden, um dies zu testen. Der folgende Beispielcode demonstriert die Verwendung dieser Eigenschaft. Die Beispieldatei zum Testen kann über den folgenden Link heruntergeladen werden:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **CellArea zur vorhandenen Validierung hinzufügen**
Es kann Fälle geben, in denen du [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) zu einer bestehenden [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) hinzufügen möchtest. Wenn du [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) mit [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-) hinzufügst, prüft Aspose.Cells alle vorhandenen Bereiche, um festzustellen, ob der neue Bereich bereits existiert. Wenn die Datei eine große Anzahl an Validierungen enthält, kann dies die Leistung beeinträchtigen. Um dies zu umgehen, bietet die API die Methode [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-). Der Parameter *checkIntersection* gibt an, ob die Überschneidung eines Bereichs mit bestehenden Validierungsbereichen überprüft werden soll. Wenn auf **false** gesetzt, wird die Überprüfung anderer Bereiche deaktiviert. Der Parameter *checkEdge* gibt an, ob die angewandten Bereiche überprüft werden sollen. Wenn der neue Bereich der obere linke Bereich wird, werden interne Einstellungen neu aufgebaut. Wenn du sicher bist, dass der neue Bereich nicht der obere linke Bereich ist, kannst du diesen Parameter auf **false** setzen.

Das folgende Code-Snippet demonstriert die Verwendung der Methode [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea-com.aspose.cells.CellArea-boolean-boolean-) zum Hinzufügen eines neuen [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) zu einer bestehenden [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Die Quell- und Ausgabedateien sind als Referenz angehängt.

[Quelldatei](PivotTableHideAndSortSample.xlsx)

[Ausgabedatei](ValidationsSample_out.xlsx)


## **Erweiterte Themen**
- [Zellvalidierung in ODS-Dateien erhalten](/cells/de/java/get-cell-validation-in-ods-files/)
- [Validierungen auf einer Zelle abrufen](/cells/de/java/get-validation-applied-on-a-cell/)
- [Überprüfen, ob Zellwert Datenvalidierungsregeln erfüllt](/cells/de/java/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="java" >}}
