---
title: Datenvalidierung
type: docs
weight: 90
url: /de/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern oder Validieren von Arbeitsblattdaten. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

## **Datenvalidierungstypen und -ausführung**

Die Datenvalidierung ist die Fähigkeit, Regeln bezüglich der in ein Arbeitsblatt eingegebenen Daten festzulegen. Verwenden Sie beispielsweise die Validierung, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATE nur Datumsangaben oder eine andere Spalte nur Zahlen enthält. Sie könnten sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATE nur Daten innerhalb eines bestimmten Bereichs enthält. Mit der Datenvalidierung können Sie steuern, was in die Zellen des Arbeitsblatts eingegeben wird.

Microsoft Excel unterstützt eine Reihe verschiedener Arten der Datenvalidierung. Jeder Typ wird verwendet, um zu steuern, welcher Datentyp in eine Zelle oder einen Zellbereich eingegeben wird. Unten veranschaulichen Code-Snippets, wie dies validiert werden kann:

- Zahlen sind ganz, das heißt, sie haben keinen Dezimalteil.
- Dezimalzahlen folgen der richtigen Struktur. Das Codebeispiel definiert, dass ein Zellbereich zwei Dezimalstellen haben sollte.
- Werte sind auf eine Werteliste beschränkt. Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder einen Zellbereich angewendet werden können.
- Daten fallen in einen bestimmten Bereich.
- Eine Zeit liegt in einem bestimmten Bereich.
- Ein Text liegt innerhalb einer vorgegebenen Zeichenlänge.

### **Datenvalidierung mit Microsoft Excel**

So erstellen Sie Validierungen mit Microsoft Excel:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Validierung anwenden möchten.
1.  Von dem**Daten** Menü, auswählen**Validierung**. Der Validierungsdialog wird angezeigt.
1.  Drücke den**Einstellungen** Registerkarte und geben Sie die Einstellungen ein.

### **Datenvalidierung mit Aspose.Cells**

Die Datenvalidierung ist eine leistungsstarke Funktion zur Validierung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste zur Verfügung stellen, Dateneingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
 In Aspose.Cells, jeder[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse hat ein[**Validierungen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)Eigenschaft, die eine Sammlung von darstellt[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation) Objekte. Um die Validierung einzurichten, legen Sie einige der[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation)Klasseneigenschaften wie folgt:

- Typ – stellt den Validierungstyp dar, der durch Verwendung eines der vordefinierten Werte in angegeben werden kann[**Validierungstyp**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)Aufzählung.
-  Operator – stellt den bei der Validierung zu verwendenden Operator dar, der durch Verwendung eines der vordefinierten Werte in angegeben werden kann[**Betreibertyp**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)Aufzählung.
- Formel1 – stellt den Wert oder Ausdruck dar, der dem ersten Teil der Datenvalidierung zugeordnet ist.
- Formel2 – stellt den Wert oder Ausdruck dar, der dem zweiten Teil der Datenvalidierung zugeordnet ist.

 Wenn der[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation) Objekteigenschaften konfiguriert wurden, können Entwickler die verwenden[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)-Struktur zum Speichern von Informationen über den Zellbereich, der mithilfe der erstellten Validierung validiert wird.

#### **Arten der Datenvalidierung**

 Das[**Validierungstyp**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)Aufzählung hat folgende Mitglieder:

|**Mitgliedsname**|**Beschreibung**|
|:- |:- |
|BeliebigerWert|Bezeichnet einen Wert eines beliebigen Typs.|
|Ganze Zahl|Bezeichnet den Validierungstyp für ganze Zahlen.|
|Dezimal|Bezeichnet den Validierungstyp für Dezimalzahlen.|
|Aufführen|Gibt den Validierungstyp für die Dropdown-Liste an.|
|Datum|Bezeichnet den Validierungstyp für Datumsangaben.|
|Zeit|Gibt den Validierungstyp für die Zeit an.|
|Textlänge|Bezeichnet den Validierungstyp für die Länge des Textes.|
|Brauch|Bezeichnet den benutzerdefinierten Validierungstyp.|

##### **Ganzzahlige Datenvalidierung**

Bei dieser Art der Validierung können Benutzer nur ganze Zahlen innerhalb eines bestimmten Bereichs in die validierten Zellen eingeben. Die folgenden Codebeispiele zeigen, wie der Validierungstyp WholeNumber implementiert wird. Das Beispiel erstellt dieselbe Datenvalidierung mit Aspose.Cells, die wir oben mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Listendatenvalidierung**

Diese Art der Validierung ermöglicht es dem Benutzer, Werte aus einer Dropdown-Liste einzugeben. Es stellt eine Liste bereit: eine Reihe von Zeilen, die Daten enthalten. Im Beispiel wird ein zweites Arbeitsblatt hinzugefügt, um die Listenquelle aufzunehmen. Benutzer können nur Werte aus der Liste auswählen. Der Validierungsbereich ist der Zellbereich A1:A5 im ersten Arbeitsblatt.

 Wichtig ist hier, dass Sie die einstellen[**Validierung.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) Eigentum zu**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Datumsdatenvalidierung**

Bei dieser Art der Validierung geben Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder nach bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer auf die Eingabe von Daten zwischen 1970 und 1999 beschränkt. Hier ist der Validierungsbereich die Zelle B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Zeitdatenvalidierung**

Bei dieser Art der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder bestimmte Kriterien erfüllende Zeiten in die validierten Zellen eingeben. Im Beispiel ist der Benutzer auf die Eingabe von Zeiten zwischen 09:00 und 11:30 Uhr beschränkt. Hier ist der Validierungsbereich die B1-Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Überprüfung der Textlängendaten**

Bei dieser Art der Validierung können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Validierungsbereich ist die B1-Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Datenvalidierungsregeln**

Wenn Datenvalidierungen implementiert sind, kann die Validierung überprüft werden, indem den Zellen unterschiedliche Werte zugewiesen werden.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel demonstriert diese Funktion mit unterschiedlichen Werten. Die Beispieldatei kann zum Testen unter folgendem Link heruntergeladen werden:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Überprüfen Sie, ob die Validierung in der Zelle Dropdown ist**

 Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob die Validierung ein Dropdown-Menü ist oder nicht,[**Validierung.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) Eigenschaft kann verwendet werden, um dies zu testen. Der folgende Beispielcode veranschaulicht die Verwendung dieser Eigenschaft. Eine Beispieldatei zum Testen kann unter folgendem Link heruntergeladen werden:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **CellArea zu vorhandener Validierung hinzufügen**

 Es kann Fälle geben, in denen Sie hinzufügen möchten[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)zu bestehen[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation). Wenn Sie hinzufügen[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) verwenden[**Validierung.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells überprüft alle bestehenden Bereiche, ob der neue Bereich bereits existiert. Wenn die Datei eine große Anzahl von Validierungen hat, wird die Leistung beeinträchtigt. Um dies zu überwinden, bietet die API die[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) Methode. Das*checkKreuzung* Der Parameter gibt an, ob die Überschneidung eines bestimmten Bereichs mit bestehenden Validierungsbereichen überprüft werden soll. Einstellen auf**FALSCH** deaktiviert die Überprüfung anderer Bereiche. Das*checkEdge* Der Parameter gibt an, ob die angewendeten Bereiche überprüft werden sollen. Wenn der neue Bereich zum Bereich oben links wird, werden die internen Einstellungen neu erstellt. Wenn Sie sicher sind, dass der neue Bereich nicht der obere linke Bereich ist, können Sie diesen Parameter auf setzen**FALSCH**.

Das folgende Code-Snippet demonstriert die Verwendung von[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) Methode, um neue hinzuzufügen[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)zu bestehen[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Die Quell- und Ausgabe-Excel-Dateien sind als Referenz beigefügt.

[Quelldatei](96928093.xlsx)

[Ausgabedatei](96928220.xlsx)


## **Themen vorantreiben**
- [Holen Sie sich die Cell-Validierung in ODS-Dateien](/cells/de/net/get-cell-validation-in-ods-files/)
- [Lassen Sie sich die Validierung auf Cell anwenden](/cells/de/net/get-validation-applied-on-a-cell/)
- [Stellen Sie sicher, dass der Wert Cell die Datenvalidierungsregeln erfüllt](/cells/de/net/verify-that-cell-value-satisfies-data-validation-rules/)
