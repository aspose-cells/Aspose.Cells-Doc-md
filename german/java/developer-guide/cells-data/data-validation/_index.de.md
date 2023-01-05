---
title: Datenvalidierung
type: docs
weight: 70
url: /de/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern oder Validieren von Arbeitsblattdaten.

[Datenvalidierung](/cells/de/java/data-validation/) ist die Möglichkeit, Regeln bezüglich der in ein Arbeitsblatt eingegebenen Daten festzulegen. Verwenden Sie beispielsweise die Validierung, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATE nur Datumsangaben oder eine andere Spalte nur Zahlen enthält. Sie könnten sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATE nur Daten innerhalb eines bestimmten Bereichs enthält. Mit der Datenvalidierung können Sie steuern, was in die Zellen des Arbeitsblatts eingegeben wird. Aspose.Cells unterstützt die Datenvalidierungs- und Autofilterfunktionen von Microsoft Excel vollständig. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}} 
## **Datenvalidierungstypen und -ausführung**
Microsoft Excel unterstützt eine Reihe verschiedener Arten der Datenvalidierung. Jeder Typ wird verwendet, um zu steuern, welcher Datentyp in eine Zelle oder einen Zellbereich eingegeben wird. Unten veranschaulichen Code-Snippets, wie dies validiert werden kann:

- [Numbers sind ganz](/cells/de/java/data-validation/)das heißt, dass sie keinen Dezimalteil haben.
- [Dezimalzahlen folgen der richtigen Struktur](/cells/de/java/data-validation/). Das Codebeispiel definiert, dass ein Zellbereich zwei Dezimalstellen haben sollte.
- [Werte sind auf eine Werteliste beschränkt](/cells/de/java/data-validation/). Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder einen Zellbereich angewendet werden können.
- [Daten fallen in einen bestimmten Bereich](/cells/de/java/data-validation/).
- [Die Zeit liegt in einem bestimmten Bereich](/cells/de/java/data-validation/).
- [Ein Text liegt innerhalb einer vorgegebenen Zeichenlänge](/cells/de/java/data-validation/).
### **Datenvalidierung mit Microsoft Excel**
So erstellen Sie Validierungen mit Microsoft Excel:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Validierung anwenden möchten.
1. Von dem**Daten**Menü, auswählen**Validierung**.
 Der Validierungsdialog wird angezeigt.
1. Drücke den**Einstellungen**Registerkarte und geben Sie die Einstellungen wie unten gezeigt ein.

   **Datenvalidierungseinstellungen** 

![todo: Bild_alt_Text](data-validation_1.png)
### **Datenvalidierung mit Aspose.Cells**
Die Datenvalidierung ist eine leistungsstarke Funktion zur Validierung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste zur Verfügung stellen, Dateneingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
 In Aspose.Cells, jeder[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Klasse hat ein[Validierungen](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)Objekt, das eine Sammlung von darstellt[Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)Objekte. Um die Validierung einzurichten, legen Sie einige der[Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)Klasseneigenschaften:

- [Typ](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): stellt den Validierungstyp dar, der durch Verwendung eines der vordefinierten Werte in angegeben werden kann[Validierungstyp](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)Aufzählung.
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): stellt den bei der Validierung zu verwendenden Operator dar, der durch Verwendung eines der vordefinierten Werte in angegeben werden kann[Betreibertyp](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)Aufzählung.
- [Formel 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): stellt den Wert oder Ausdruck dar, der dem ersten Teil der Datenvalidierung zugeordnet ist.
- [Formel2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): stellt den Wert oder Ausdruck dar, der dem zweiten Teil der Datenvalidierung zugeordnet ist.

Wenn die[Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)Objekteigenschaften konfiguriert wurden, können Entwickler die verwenden[Zellbereich](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)-Struktur zum Speichern von Informationen über den Zellbereich, der mithilfe der erstellten Validierung validiert wird.
#### **Arten der Datenvalidierung**
Die Datenvalidierung ermöglicht es Ihnen, Geschäftsregeln in jede Zelle einzubauen, sodass falsche Eingaben zu Fehlermeldungen führen. Geschäftsregeln sind die Richtlinien und Verfahren, die die Funktionsweise eines Unternehmens regeln. Aspose.Cells unterstützt alle wichtigen Arten der Datenvalidierung.

Das[Validierungstyp](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)Aufzählung hat folgende Mitglieder:

|**Mitgliedsname**|**Beschreibung**|
|:- |:- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Bezeichnet einen Wert eines beliebigen Typs.|
|[GANZE ZAHL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Bezeichnet den Validierungstyp für ganze Zahlen.|
|[DEZIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Bezeichnet den Validierungstyp für Dezimalzahlen.|
|[AUFFÜHREN](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Gibt den Validierungstyp für die Dropdown-Liste an.|
|[DATUM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Bezeichnet den Validierungstyp für Datumsangaben.|
|[ZEIT](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Bezeichnet den Validierungstyp für Zeit.|
|[TEXT_LÄNGE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Bezeichnet den Validierungstyp für die Länge des Textes.|
|[BRAUCH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Bezeichnet den benutzerdefinierten Validierungstyp.|
#### **Programmierbeispiel: Ganzzahlige Datenvalidierung**
Bei dieser Art der Validierung können Benutzer nur ganze Zahlen innerhalb eines bestimmten Bereichs in die validierten Zellen eingeben. Die folgenden Codebeispiele zeigen, wie die implementiert wird[GANZE ZAHL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)Validierungstyp. Das Beispiel erstellt dieselbe Datenvalidierung mit Aspose.Cells, die wir oben mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Programmierbeispiel: Dezimaldatenvalidierung**
Bei dieser Art der Validierung kann der Benutzer Dezimalzahlen in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, nur Dezimalwerte einzugeben, und der Validierungsbereich ist A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Programmierbeispiel: Validierung von Listendaten**
Diese Art der Validierung ermöglicht es dem Benutzer, Werte aus einer Dropdown-Liste einzugeben. Es stellt eine Liste bereit: eine Reihe von Zeilen, die Daten enthalten. Benutzer können nur Werte aus der Liste auswählen. Der Validierungsbereich ist der Zellbereich A1:A5 im ersten Arbeitsblatt.

Wichtig ist hier, dass Sie die einstellen[Validierung.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) Eigentum zu**wahr**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Programmierbeispiel: Datumsdatenvalidierung**
Bei dieser Art der Validierung geben Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder nach bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer auf die Eingabe von Daten zwischen 1970 und 1999 beschränkt. Hier ist der Validierungsbereich die Zelle B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Programmierbeispiele: Zeitdatenvalidierung**
Bei dieser Art der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder bestimmte Kriterien erfüllende Zeiten in die validierten Zellen eingeben. Im Beispiel ist der Benutzer auf die Eingabe von Zeiten zwischen 09:00 und 11:30 Uhr beschränkt. Hier ist der Validierungsbereich die B1-Zelle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Programmierbeispiele: Validierung von Textlängendaten**
Bei dieser Art der Validierung können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Validierungsbereich ist die B1-Zelle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Datenvalidierungsregeln**
Wenn Datenvalidierungen implementiert sind, kann die Validierung überprüft werden, indem den Zellen unterschiedliche Werte zugewiesen werden.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel demonstriert diese Funktion mit unterschiedlichen Werten. Die Beispieldatei kann zum Testen unter folgendem Link heruntergeladen werden:

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Überprüfen Sie, ob die Validierung in einer Zelle Dropdown ist**
 Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob die Validierung ein Dropdown-Menü ist oder nicht,[Validierung.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) Eigenschaft kann verwendet werden, um dies zu testen. Der folgende Beispielcode demonstriert die Verwendung dieser Eigenschaft. Die Beispieldatei zum Testen kann unter folgendem Link heruntergeladen werden:

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **CellArea zu vorhandener Validierung hinzufügen**
Es kann Fälle geben, in denen Sie hinzufügen möchten[Zellbereich](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)zu bestehen[Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Wenn Sie hinzufügen[Zellbereich](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)verwenden[Validierung.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells überprüft alle bestehenden Bereiche, ob der neue Bereich bereits existiert. Wenn die Datei eine große Anzahl von Validierungen hat, wird die Leistung beeinträchtigt. Um dies zu überwinden, bietet die API die[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) Methode. Das*checkKreuzung*Der Parameter gibt an, ob die Überschneidung eines bestimmten Bereichs mit bestehenden Validierungsbereichen überprüft werden soll. Einstellen auf**FALSCH**deaktiviert die Überprüfung anderer Bereiche. Das*checkEdge*Der Parameter gibt an, ob die angewendeten Bereiche überprüft werden sollen. Wenn der neue Bereich zum Bereich oben links wird, werden die internen Einstellungen neu erstellt. Wenn Sie sicher sind, dass der neue Bereich nicht der obere linke Bereich ist, können Sie diesen Parameter auf setzen**FALSCH**.

Das folgende Code-Snippet demonstriert die Verwendung von[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\))-Methode zum Hinzufügen neuer[Zellbereich](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)zu bestehen[Validierung](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Die Quell- und Ausgabe-Excel-Dateien sind als Referenz beigefügt.

[Quelldatei](PivotTableHideAndSortSample.xlsx)

[Ausgabedatei](ValidationsSample_out.xlsx)


## **Themen vorantreiben**
- [Holen Sie sich die Cell-Validierung in ODS-Dateien](/cells/de/java/get-cell-validation-in-ods-files/)
- [Lassen Sie sich die Validierung auf Cell anwenden](/cells/de/java/get-validation-applied-on-a-cell/)
- [Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt](/cells/de/java/verify-that-cell-value-satisfies-data-validation-rules/)
