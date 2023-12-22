---
title: Datenvalidierung
type: docs
weight: 90
url: /de/net/data-validation/
description: Erfahren Sie, wie Sie die Datenvalidierung über Aspose.Cells for .NET API hinzufügen.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zum automatischen Filtern oder Validieren von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Datenvalidierungs- und AutoFilter-Funktionen von Microsoft Excel. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

##  **Datenvalidierungstypen und -ausführung**

Bei der Datenvalidierung handelt es sich um die Möglichkeit, Regeln für die in ein Arbeitsblatt eingegebenen Daten festzulegen. Verwenden Sie beispielsweise die Validierung, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATE nur Datumsangaben enthält oder dass eine andere Spalte nur Zahlen enthält. Sie könnten sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATE nur Datumsangaben innerhalb eines bestimmten Bereichs enthält. Mit der Datenvalidierung können Sie steuern, was in die Zellen des Arbeitsblatts eingegeben wird.

Microsoft Excel unterstützt eine Reihe verschiedener Arten der Datenvalidierung. Jeder Typ wird verwendet, um zu steuern, welche Art von Daten in eine Zelle oder einen Zellbereich eingegeben werden. Nachfolgend veranschaulichen Codeausschnitte, wie dies validiert wird:

- Numbers sind ganze Zahlen, das heißt, sie haben keinen Dezimalteil.
- Dezimalzahlen folgen der richtigen Struktur. Das Codebeispiel definiert, dass ein Zellbereich zwei Dezimalstellen haben sollte.
- Werte sind auf eine Werteliste beschränkt. Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder einen Zellbereich angewendet werden können.
- Die Daten liegen in einem bestimmten Bereich.
- Eine Zeit liegt innerhalb eines bestimmten Bereichs.
- Ein Text liegt innerhalb einer vorgegebenen Zeichenlänge.

###  **Datenvalidierung mit Microsoft Excel**

So erstellen Sie Validierungen mit Microsoft Excel:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Validierung anwenden möchten.
1.  Von dem**Daten** Wählen Sie im Menü *Validierung**. Der Validierungsdialog wird angezeigt.
1.  Drücke den**Einstellungen** Klicken Sie auf die Registerkarte und geben Sie die Einstellungen ein.

###  **Datenvalidierung mit Aspose.Cells**

Die Datenvalidierung ist eine leistungsstarke Funktion zur Validierung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Liste mit Auswahlmöglichkeiten zur Verfügung stellen, Dateneingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
 In Aspose.Cells, jeweils[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse hat eine[**Validierungen**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) Eigenschaft, die eine Sammlung von darstellt[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation) Objekte. Um die Validierung einzurichten, legen Sie einige davon fest[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation)Klasseneigenschaften wie folgt:

- Typ – stellt den Validierungstyp dar, der mithilfe eines der vordefinierten Werte im angegeben werden kann[**Validierungstyp**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)Aufzählung.
-  Operator – stellt den bei der Validierung zu verwendenden Operator dar, der mithilfe eines der vordefinierten Werte in angegeben werden kann[**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)Aufzählung.
- Formel1 – stellt den Wert oder Ausdruck dar, der dem ersten Teil der Datenvalidierung zugeordnet ist.
- Formel2 – stellt den Wert oder Ausdruck dar, der dem zweiten Teil der Datenvalidierung zugeordnet ist.

 Wenn das[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation) Nachdem die Eigenschaften des Objekts konfiguriert wurden, können Entwickler die verwenden[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)Struktur zum Speichern von Informationen über den Zellbereich, der mithilfe der erstellten Validierung validiert wird.

####  **Arten der Datenvalidierung**

 Der[**Validierungstyp**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)Die Aufzählung hat die folgenden Mitglieder:

|**Mitgliedsname**|**Beschreibung**|
| :- | :- |
|Beliebiger Wert|Bezeichnet einen Wert beliebigen Typs.|
|Ganze Zahl|Bezeichnet den Validierungstyp für ganze Zahlen.|
|Dezimal|Bezeichnet den Validierungstyp für Dezimalzahlen.|
|Aufführen|Gibt den Validierungstyp für die Dropdown-Liste an.|
|Datum|Gibt den Validierungstyp für Datumsangaben an.|
|Zeit|Bezeichnet den Validierungstyp für die Zeit.|
|Textlänge|Gibt den Validierungstyp für die Länge des Textes an.|
|Brauch|Bezeichnet den benutzerdefinierten Validierungstyp.|

#####  **Ganzzahlige Datenvalidierung**

Bei dieser Art der Validierung können Benutzer nur ganze Zahlen innerhalb eines bestimmten Bereichs in die validierten Zellen eingeben. Die folgenden Codebeispiele zeigen, wie der WholeNumber-Validierungstyp implementiert wird. Das Beispiel erstellt die gleiche Datenvalidierung mit Aspose.Cells, die wir oben mit Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **Listendatenvalidierung**

Diese Art der Validierung ermöglicht es dem Benutzer, Werte aus einer Dropdown-Liste einzugeben. Es stellt eine Liste bereit: eine Reihe von Zeilen, die Daten enthalten. Im Beispiel wird ein zweites Arbeitsblatt hinzugefügt, um die Listenquelle aufzunehmen. Benutzer können nur Werte aus der Liste auswählen. Der Validierungsbereich ist der Zellbereich A1:A5 im ersten Arbeitsblatt.

 Wichtig hierbei ist, dass Sie die einstellen[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)Eigenschaft auf *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **Datumsdatenvalidierung**

Bei dieser Art der Validierung geben Benutzer Datumswerte, die innerhalb eines bestimmten Bereichs liegen oder bestimmte Kriterien erfüllen, in die validierten Zellen ein. Im Beispiel ist der Benutzer auf die Eingabe von Daten zwischen 1970 und 1999 beschränkt. Hier ist der Validierungsbereich die Zelle B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **Zeitdatenvalidierung**

Bei dieser Art der Validierung können Benutzer Zeiten, die innerhalb eines bestimmten Bereichs liegen oder bestimmte Kriterien erfüllen, in die validierten Zellen eingeben. Im Beispiel ist der Benutzer auf die Eingabe von Zeiten zwischen 09:00 und 11:30 Uhr beschränkt. Hier ist der Validierungsbereich die B1-Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **Validierung von Textlängendaten**

Bei dieser Art der Validierung können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Validierungsbereich ist die B1-Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **Datenvalidierungsregeln**

 Wenn Datenvalidierungen implementiert sind, kann die Validierung überprüft werden, indem den Zellen unterschiedliche Werte zugewiesen werden.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel demonstriert diese Funktion mit verschiedenen Werten. Die Beispieldatei kann zum Testen über den folgenden Link heruntergeladen werden:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **Überprüfen Sie, ob die Validierung in der Zelle ein Dropdown-Menü ist**

 Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob die Validierung eine Dropdown-Liste ist oder nicht,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)Mit der Eigenschaft kann dies getestet werden. Der folgende Beispielcode veranschaulicht die Verwendung dieser Eigenschaft. Eine Beispieldatei zum Testen kann unter folgendem Link heruntergeladen werden:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **Fügen Sie CellArea zur vorhandenen Validierung hinzu**

 Es kann Fälle geben, in denen Sie etwas hinzufügen möchten[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)zu existieren[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation). Wenn Sie hinzufügen[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) verwenden[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells prüft alle bestehenden Bereiche, um zu sehen, ob der neue Bereich bereits existiert. Wenn die Datei über eine große Anzahl an Validierungen verfügt, führt dies zu Leistungseinbußen. Um dies zu überwinden, bietet die API die[**Validation.AddAreaCellArea (cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) Methode. Der*checkIntersection* Der Parameter gibt an, ob der Schnittpunkt eines bestimmten Bereichs mit vorhandenen Validierungsbereichen überprüft werden soll. Stellen Sie es ein**FALSCH** deaktiviert die Überprüfung anderer Bereiche. Der*checkEdge*Der Parameter gibt an, ob die angewendeten Bereiche überprüft werden sollen. Wenn der neue Bereich zum Bereich oben links wird, werden die internen Einstellungen neu erstellt. Wenn Sie sicher sind, dass der neue Bereich nicht der Bereich oben links ist, können Sie diesen Parameter auf *false** setzen.

Der folgende Codeausschnitt demonstriert die Verwendung von[**Validation.AddAreaCellArea (cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) Methode zum Hinzufügen neuer[**Zellbereich**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)zu existieren[**Validierung**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Die Quell- und Ausgabe-Excel-Dateien sind als Referenz beigefügt.

[Quelldatei](96928093.xlsx)

[Ausgabedatei](96928220.xlsx)


##  **Vorabthemen**
- [Erhalten Sie die Cell-Validierung in ODS-Dateien](/cells/de/net/get-cell-validation-in-ods-files/)
- [Lassen Sie sich unter der Nummer Cell validieren](/cells/de/net/get-validation-applied-on-a-cell/)
- [Stellen Sie sicher, dass der Wert Cell den Datenvalidierungsregeln entspricht](/cells/de/net/verify-that-cell-value-satisfies-data-validation-rules/)
