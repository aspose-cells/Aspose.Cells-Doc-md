---
title: Datenvalidierung
type: docs
weight: 90
url: /de/net/data-validation/
description: Erfahren Sie, wie Sie die Datenvalidierung durch die Aspose.Cells for .NET API hinzufügen.
keywords: Datenvalidierung hinzufügen, Validierungswert abrufen, Ganzzahl Datenvalidierung hinzufügen, Listen Datenvalidierung hinzufügen, Datum Datenvalidierung hinzufügen, Zeit Datenvalidierung hinzufügen, Textlängen Datenvalidierung hinzufügen, Zellenbereich zur vorhandenen Validierung hinzufügen, Überprüfen, ob die Validierung in der Zelle Dropdown ist, Benutzerdefinierte Validierung hinzufügen  
---

{{% alert color="primary" %}}

Microsoft Excel bietet einige gute Funktionen zur Autofilterung oder Validierung von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Datenvalidierungs- und Autofilterfunktionen von Microsoft Excel. In diesem Artikel wird erläutert, wie Sie die Funktionen in Microsoft Excel verwenden und wie Sie sie mit Aspose.Cells codieren.

{{% /alert %}}

## **Datenvalidierungstypen und Ausführung**

Datenvalidierung ermöglicht das Festlegen von Regeln für auf einem Arbeitsblatt eingegebene Daten. Verwenden Sie beispielsweise Validierungen, um sicherzustellen, dass eine Spalte mit der Bezeichnung DATUM nur Datumsangaben enthält oder dass eine andere Spalte nur Zahlen enthält. Sie könnten sogar sicherstellen, dass eine Spalte mit der Bezeichnung DATUM nur Daten innerhalb eines bestimmten Bereichs enthält. Mit Datenvalidierungen können Sie steuern, was in Zellen im Arbeitsblatt eingegeben wird.

Microsoft Excel unterstützt verschiedene Arten von Datenvalidierungen. Jede Art wird verwendet, um zu steuern, welche Art von Daten in eine Zelle oder Zellbereich eingegeben wird. Nachfolgend werden Codeausschnitte illustriert, wie überprüft wird, dass:

- Zahlen ganzzahlig sind, d.h. keine Dezimalstellen haben.
- Dezimalzahlen die richtige Struktur aufweisen. Das Codebeispiel definiert, dass ein Zellbereich zwei Dezimalstellen haben sollte.
- Werte auf eine Liste von Werten beschränkt sind. Die Listenvalidierung definiert eine separate Liste von Werten, die auf eine Zelle oder einen Zellbereich angewendet werden können.
- Daten innerhalb eines bestimmten Bereichs liegen.
- Eine Uhrzeit innerhalb eines bestimmten Bereichs liegt.
- Ein Text eine bestimmte Zeichenlänge aufweist.

### **Datenvalidierung mit Microsoft Excel**

Um Validierungen mit Microsoft Excel zu erstellen:

1. Wählen Sie in einem Arbeitsblatt die Zellen aus, auf die Sie die Überprüfung anwenden möchten.
1. Wählen Sie im **Daten**-Menü **Validierung** aus. Der Validierungsdialog wird angezeigt.
1. Klicken Sie auf die Registerkarte **Einstellungen** und geben Sie die Einstellungen ein.

### **Datumsvalidierung mit Aspose.Cells**

Die Datenvalidierung ist eine leistungsstarke Funktion zur Überprüfung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste bereitstellen, Daten eingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.
In Aspose.Cells hat jede [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse eine [**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)-Eigenschaft, die eine Sammlung von [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)-Objekten darstellt. Um die Validierung einzurichten, setzen Sie einige der Eigenschaften der [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)-Klasse wie folgt:

- Typ – stellt den Validierungstyp dar, der durch Verwendung einer der vordefinierten Werte in der [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)-Aufzählung angegeben werden kann.
- Operator – stellt den Operator dar, der bei der Validierung verwendet werden soll und durch Verwendung eines der vordefinierten Werte in der [**OperatorType**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)-Aufzählung angegeben werden kann.
- Formel1 – stellt den Wert oder den Ausdruck dar, der mit dem ersten Teil der Datenvalidierung verbunden ist.
- Formel2 – repräsentiert den Wert oder Ausdruck, der mit dem zweiten Teil der Datenvalidierung verbunden ist.

Wenn die Eigenschaften des [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)-Objekts konfiguriert wurden, können Entwickler die [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)-Struktur verwenden, um Informationen über den Zellenbereich zu speichern, der mithilfe der erstellten Validierung überprüft wird.

#### **Arten der Datenvalidierung**

Die [**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)-Aufzählung hat die folgenden Elemente:

|**Member Name**|**Description**|
| :- | :- |
|AnyValue|Bezeichnet einen Wert jedes Typs.
|WholeNumber|Bezeichnet den Validierungstyp für ganze Zahlen.
|Decimal|Bezeichnet den Validierungstyp für Dezimalzahlen.
|List|Bezeichnet den Validierungstyp für Dropdown-Liste.
|Date|Bezeichnet den Validierungstyp für Datum.
|Time|Bezeichnet den Validierungstyp für Uhrzeit.
|TextLength|Bezeichnet den Validierungstyp für die Länge des Textes.
|Custom|Bezeichnet benutzerdefinierten Validierungstyp.

##### **Ganze Zahl Datenvalidierung**

Mit diesem Validierungstyp können Benutzer nur ganze Zahlen innerhalb eines festgelegten Bereichs in die validierten Zellen eingeben. Die nachfolgenden Codebeispiele zeigen, wie der Validierungstyp Ganzzahl implementiert wird. Das Beispiel erstellt dieselbe Datenvalidierung mit Aspose.Cells, die wir oben mithilfe von Microsoft Excel erstellt haben.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Listendatenvalidierung**

Bei dieser Art der Validierung kann der Benutzer Werte aus einer Dropdown-Liste eingeben. Es bietet eine Liste: eine Reihe von Zeilen, die Daten enthalten. Im Beispiel wird ein zweites Arbeitsblatt hinzugefügt, um die Listenquelle zu speichern. Benutzer können nur Werte aus der Liste auswählen. Der Gültigkeitsbereich ist der Zellenbereich A1:A5 im ersten Arbeitsblatt.

Es ist wichtig, dass Sie die [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)-Eigenschaft auf **true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Datum Datenvalidierung**

Bei diesem Validierungstyp gibt der Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder gemäß bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer darauf beschränkt, Daten zwischen 1970 und 1999 einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Zeit Datenvalidierung**

Bei diesem Typ der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder gemäß bestimmter Kriterien in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeiten zwischen 09:00 und 11:30 Uhr einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Textlängendatenvalidierung**

Bei diesem Validierungstyp können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Gültigkeitsbereich ist die Zelle B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Datenvalidierungsregeln**

Wenn Datenvalidierungen implementiert sind, kann die Validierung überprüft werden, indem verschiedene Werte den Zellen zugewiesen werden. [**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) kann verwendet werden, um das Validierungsergebnis zu erhalten. Das folgende Beispiel zeigt diese Funktion mit verschiedenen Werten. Die Beispieldatei kann über den folgenden Link heruntergeladen werden, um getestet zu werden:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Überprüfen Sie, ob die Validierung in der Zelle ein Dropdown ist**

Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob die Validierung ein Dropdown ist oder nicht, kann die Eigenschaft [**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) verwendet werden, um dies zu testen. Der folgende Beispielcode demonstriert die Verwendung dieser Eigenschaft. Eine Beispieldatei für Tests kann über den folgenden Link heruntergeladen werden: 

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **CellArea zur vorhandenen Validierung hinzufügen**

Es gibt möglicherweise Fälle, in denen Sie [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) zu vorhandenem [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) hinzufügen möchten. Wenn Sie [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) mit [**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea) hinzufügen, überprüft Aspose.Cells alle vorhandenen Bereiche, um zu sehen, ob der neue Bereich bereits existiert. Wenn die Datei eine große Anzahl von Validierungen enthält, wirkt sich dies negativ auf die Leistung aus. Um dies zu überwinden, bietet die API die Methode [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) an. Der Parameter *checkIntersection* gibt an, ob der Schnittpunkt eines bestimmten Bereichs mit vorhandenen Validierungsbereichen überprüft werden soll. Wenn Sie ihn auf **false** setzen, wird die Überprüfung anderer Bereiche deaktiviert. Der Parameter *checkEdge* gibt an, ob die angewendeten Bereiche überprüft werden sollen. Wenn der neue Bereich der obere linke Bereich wird, werden interne Einstellungen neu erstellt. Wenn Sie sicher sind, dass der neue Bereich nicht der obere linke Bereich ist, können Sie diesen Parameter auf **false** setzen.

Der folgende Code-Ausschnitt zeigt die Verwendung der Methode [**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) zum Hinzufügen neuer [**CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) zu vorhandenem [**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Die Quell- und Ausgabedateien sind als Referenz angehängt.

[Quelldatei](96928093.xlsx)

[Ausgabedatei](96928220.xlsx)


## **Erweiterte Themen**
- [Zellvalidierung in ODS-Dateien erhalten](/cells/de/net/get-cell-validation-in-ods-files/)
- [Validierungen auf einer Zelle abrufen](/cells/de/net/get-validation-applied-on-a-cell/)
- [Überprüfen, ob Zellwert Datenvalidierungsregeln erfüllt](/cells/de/net/verify-that-cell-value-satisfies-data-validation-rules/)
