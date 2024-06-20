---
title: Daten hinzufügen und abrufen
type: docs
weight: 20
url: /de/cpp/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Zugriff auf Zellen eines Arbeitsblatts](/cells/de/cpp/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um verschiedene Arten von Daten zu Zellen hinzuzufügen.

{{% /alert %}} 
## **Hinzufügen von Daten zu Zellen**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse stellt eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung bereit. Jedes Element in der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse.

Aspose.Cells ermöglicht es Entwicklern, Daten den Zellen in Arbeitsblättern hinzuzufügen, indem sie die [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode der [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse aufrufen. Aspose.Cells bietet überladene Versionen der [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode, die es Entwicklern ermöglichen, verschiedene Arten von Daten zu Zellen hinzuzufügen. Mit diesen überladenen Versionen der [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode ist es möglich, einen booleschen Wert, einen String, einen Double, einen Integer oder ein Datum/Zeit usw. den Zellen hinzuzufügen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
### **Effizienz verbessern**
Wenn Sie die [PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)-Methode verwenden, um eine große Menge von Daten in ein Arbeitsblatt einzufügen, sollten Sie zuerst Werte zeilenweise und dann spaltenweise hinzufügen. Dieser Ansatz verbessert erheblich die Effizienz Ihrer Anwendungen.
## **Abrufen von Daten aus Zellen**
Aspose.Cells bietet eine Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)-Klasse enthält eine [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Klasse stellt eine [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung bereit. Jedes Element in der [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse.

Die [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)-Klasse bietet mehrere Methoden, mit denen Entwickler Werte aus den Zellen entsprechend ihrer Datentypen abrufen können. Diese Methoden umfassen:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), gibt den Zeichenfolgenwert der Zelle zurück.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), gibt den Dezimalwert der Zelle zurück.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), gibt den booleschen Wert der Zelle zurück.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), gibt den Datum/Uhrzeit-Wert der Zelle zurück.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), gibt den Float-Wert der Zelle zurück.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/), gibt den Ganzzahl-Wert der Zelle zurück.

Wenn ein Feld nicht ausgefüllt ist, lösen Zellen mit [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) oder [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) eine Ausnahme aus.

Der Datentyp, der in einer Zelle enthalten ist, kann auch mit Hilfe der Methode [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) der Klasse [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) überprüft werden. Tatsächlich basiert die Methode [GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) der Klasse [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) auf der Enumeration [CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|CellValueType_IsBool| Gibt an, dass der Zellwert boolesch ist.
|CellValueType_IsDateTime| Gibt an, dass der Zellwert Datum/Uhrzeit ist.
|CellValueType_IsNull| Stellt eine leere Zelle dar.
|CellValueType_IsNumeric| Gibt an, dass der Zellwert numerisch ist.
|CellValueType_IsString| Gibt an, dass der Zellwert ein String ist.
|CellValueType_IsUnknown| Gibt an, dass der Zellwert unbekannt ist.
Sie können auch die oben definierten Zellwerttypen verwenden, um mit dem Typ der Daten in jeder Zelle zu vergleichen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
