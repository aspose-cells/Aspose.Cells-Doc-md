---  
title: Datenvalidierung
type: docs  
weight: 90  
url: /de/nodejs-cpp/data-validation/  
description: Lernen Sie, wie man Datenvalidierungen mit der Aspose.Cells for Node.js via C++ API hinzufügt.  
keywords: Datenvalidierung in Node.js via C++, Validierungswert in Node.js via C++, Ganzezahl Datenvalidierung in Node.js via C++, Listendatenvalidierung in Node.js via C++, Datums Datenvalidierung in Node.js via C++, Zeit Datenvalidierung in Node.js via C++, Textlänge Datenvalidierung in Node.js via C++, CellArea zu bestehender Validierung in Node.js via C++, Überprüfung, ob Validierung in Zelle ein Dropdown ist, in Node.js via C++, Benutzerdefinierte Validierung in Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel bietet einige nützliche Funktionen zum automatischen Filtern oder Validieren von Arbeitsblattdaten. Aspose.Cells unterstützt vollständig die Datenvalidierungs- und AutoFilter-Funktionen von Microsoft Excel. Dieser Artikel erklärt, wie man die Funktionen in Microsoft Excel verwendet und wie man sie mithilfe von Aspose.Cells for Node.js via C++ programmiert.  
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

### **Datenvalidierung mit Aspose.Cells for Node.js via C++**  

Die Datenvalidierung ist eine leistungsstarke Funktion zur Überprüfung der in Arbeitsblätter eingegebenen Informationen. Mit der Datenvalidierung können Entwickler Benutzern eine Auswahlliste bereitstellen, Daten eingaben auf einen bestimmten Typ oder eine bestimmte Größe beschränken usw.  
In Aspose.Cells for Node.js via C++ verfügt jede [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) Klasse über eine [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) Methode, die eine Sammlung von [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) Objekten darstellt. Um die Validierung einzurichten, setzen Sie einige Eigenschaften der [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) Klasse wie folgt:  

- Typ – repräsentiert den Validierungstyp, der durch die Verwendung eines der vordefinierten Werte im [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) Enum festgelegt werden kann.  
- Operator – repräsentiert den Operator, der bei der Validierung verwendet wird, der durch eines der vordefinierten Werte im [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype) Enum festgelegt werden kann.  
- Formel1 – stellt den Wert oder den Ausdruck dar, der mit dem ersten Teil der Datenvalidierung verbunden ist.  
- Formel2 – repräsentiert den Wert oder Ausdruck, der mit dem zweiten Teil der Datenvalidierung verbunden ist.  

Wenn die Eigenschaften des [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) Objekts konfiguriert wurden, können Entwickler die [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) Struktur nutzen, um Informationen über den Zellbereich zu speichern, der mit der erstellten Validierung geprüft werden soll.  

#### **Arten der Datenvalidierung**  

Das [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) Enum hat die folgenden Mitglieder:  

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

Mit dieser Art der Validierung können Nutzer nur Ganzzahlen innerhalb eines festgelegten Bereichs in die validierten Zellen eingeben. Die folgenden Codebeispiele zeigen, wie man die WholeNumber-Validierungsart implementiert. Das Beispiel erstellt die gleiche Datenvalidierung mit Aspose.Cells for Node.js via C++, wie wir sie zuvor mit Microsoft Excel erstellt haben.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Listendatenvalidierung**  

Bei dieser Art der Validierung kann der Benutzer Werte aus einer Dropdown-Liste eingeben. Es bietet eine Liste: eine Reihe von Zeilen, die Daten enthalten. Im Beispiel wird ein zweites Arbeitsblatt hinzugefügt, um die Listenquelle zu speichern. Benutzer können nur Werte aus der Liste auswählen. Der Gültigkeitsbereich ist der Zellenbereich A1:A5 im ersten Arbeitsblatt.  

Hier ist es wichtig, dass Sie die [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-)-Eigenschaft auf **true** setzen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Datum Datenvalidierung**  

Bei diesem Validierungstyp gibt der Benutzer Datumswerte innerhalb eines bestimmten Bereichs oder gemäß bestimmten Kriterien in die validierten Zellen ein. Im Beispiel ist der Benutzer darauf beschränkt, Daten zwischen 1970 und 1999 einzugeben. Der Gültigkeitsbereich ist die Zelle B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Zeit Datenvalidierung**  

Bei diesem Typ der Validierung können Benutzer Zeiten innerhalb eines bestimmten Bereichs oder gemäß bestimmter Kriterien in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeiten zwischen 09:00 und 11:30 Uhr einzugeben. Der Gültigkeitsbereich ist die Zelle B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Textlängendatenvalidierung**  

Bei diesem Validierungstyp können Benutzer Textwerte einer bestimmten Länge in die validierten Zellen eingeben. Im Beispiel ist der Benutzer darauf beschränkt, Zeichenfolgenwerte mit nicht mehr als 5 Zeichen einzugeben. Der Gültigkeitsbereich ist die Zelle B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Datenvalidierungsregeln**  

Wenn Datenvalidierungen implementiert sind, kann die Validierung durch die Zuordnung verschiedener Werte in den Zellen überprüft werden. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) kann verwendet werden, um das Validierungsergebnis abzurufen. Das folgende Beispiel zeigt diese Funktion mit unterschiedlichen Werten. Die Beispieldatei kann zum Testen vom folgenden Link heruntergeladen werden:  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Überprüfen Sie, ob die Validierung in der Zelle ein Dropdown ist**  

Wie wir gesehen haben, gibt es viele Arten von Validierungen, die innerhalb einer Zelle implementiert werden können. Wenn Sie überprüfen möchten, ob eine Validierung ein Dropdown ist oder nicht, können Sie die [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) Methode verwenden, um dies zu testen. Der folgende Beispielcode demonstriert die Verwendung dieser Eigenschaft. Eine Beispieldatei zum Testen kann vom folgenden Link heruntergeladen werden:  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **CellArea zur vorhandenen Validierung hinzufügen**  

Es könnte Situationen geben, in denen Sie [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) zu bestehenden [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) hinzufügen möchten. Wenn Sie [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) mit [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-) hinzufügen, prüft Aspose.Cells alle bestehenden Bereiche, um zu sehen, ob der neue Bereich bereits existiert. Wenn die Datei viele Validierungen enthält, beeinträchtigt dies die Leistung. Um dies zu vermeiden, bietet die API die [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) Methode. Der *checkIntersection*-Parameter gibt an, ob die Schnittmenge eines Bereichs mit bestehenden Validierungsbereichen geprüft werden soll. Das Setzen auf **false** deaktiviert diese Überprüfung. Der *checkEdge*-Parameter prüft, ob die angewendeten Bereiche überprüft werden. Wenn der neue Bereich die obere/linke Ecke ist, werden interne Einstellungen neu aufgebaut. Wenn Sie sicher sind, dass der neue Bereich nicht die obere/linke Ecke ist, können Sie diesen Parameter auf **false** setzen.  

Der folgende Codeausschnitt zeigt, wie die [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) Methode verwendet wird, um eine neue [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) zu den bestehenden [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) hinzuzufügen.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

Die Quell- und Ausgabedateien sind als Referenz angehängt.  

[Quelldatei](96928093.xlsx)  

[Ausgabedatei](96928220.xlsx)  

## **Erweiterte Themen**  
- [Zellvalidierung in ODS-Dateien erhalten](/cells/de/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Validierungen auf einer Zelle abrufen](/cells/de/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Überprüfen, ob Zellwert Datenvalidierungsregeln erfüllt](/cells/de/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

