---
title: Daten hinzufügen und abrufen
type: docs
weight: 20
url: /de/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 In[Zugriff auf Cells eines Arbeitsblatts](/cells/de/cpp/accessing-cells-of-a-worksheet/)haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um Zellen verschiedene Datentypen hinzuzufügen.

{{% /alert %}} 
##  **Daten zu Cells hinzufügen**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet eine[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Jedes Element in der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Die Sammlung stellt ein Objekt dar[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)Klasse.

 Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Daten zu den Zellen in Arbeitsblättern durch Aufrufen von[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) Klasse[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) Methode. Aspose.Cells bietet überladene Versionen von[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) Methode, mit der Entwickler Zellen verschiedene Arten von Daten hinzufügen können. Mit diesen überladenen Versionen von[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Mit der Methode ist es möglich, der Zelle boolesche, Zeichenfolgen-, Doppel-, Ganzzahl- oder Datums-/Uhrzeitwerte usw. hinzuzufügen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells-new.cpp" >}}
###  **Effizienz verbessern**
 Wenn du benutzt[PutValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/)Mit dieser Methode können Sie eine große Datenmenge in ein Arbeitsblatt einfügen. Sie sollten den Zellen Werte hinzufügen, zuerst nach Zeilen und dann nach Spalten. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.
##  **Abrufen von Daten von Cells**
 Aspose.Cells bietet eine Klasse[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) das stellt eine Microsoft Excel-Datei dar. Der[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Klasse enthält eine[Arbeitsblätter](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse. Der[Arbeitsblatt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Klasse bietet a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Sammlung. Jedes Element in der[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) Die Sammlung stellt ein Objekt dar[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)Klasse.

 Der[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)Die Klasse stellt mehrere Methoden bereit, mit denen Entwickler Werte aus den Zellen entsprechend ihrem Datentyp abrufen können. Zu diesen Methoden gehören:

- [GetStringValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/), gibt den Zeichenfolgenwert der Zelle zurück.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/), gibt den doppelten Wert der Zelle zurück.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/), gibt den booleschen Wert der Zelle zurück.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/), gibt den Datums-/Uhrzeitwert der Zelle zurück.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/), gibt den Float-Wert der Zelle zurück.
- [GetIntValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/)gibt den ganzzahligen Wert der Zelle zurück.

 Wenn ein Feld nicht gefüllt ist, werden Zellen mit[GetDoubleValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) oder[GetFloatValue](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/)löst eine Ausnahme aus.

 Der Typ der in einer Zelle enthaltenen Daten kann auch mithilfe von überprüft werden[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) Klasse[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) Methode. Tatsächlich ist die[Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) Klasse[GetType](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) Die Methode basiert auf der[CellValueType](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/)Aufzählung, deren vordefinierte Werte unten aufgeführt sind:

|**Cell Werttypen**|**Beschreibung**|
| :- | :- |
|CellValueType_IsBool|Gibt an, dass der Zellenwert boolesch ist.|
|CellValueType_IsDateTime|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|CellValueType_IsNull|Stellt eine leere Zelle dar.|
|CellValueType_IsNumeric|Gibt an, dass der Zellenwert numerisch ist.|
|CellValueType_IsString|Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|CellValueType_IsUnknown|Gibt an, dass der Zellenwert unbekannt ist.|
Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem Typ der in jeder Zelle vorhandenen Daten zu vergleichen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells-new.cpp" >}}
