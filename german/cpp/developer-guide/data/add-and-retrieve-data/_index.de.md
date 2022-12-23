---
title: Daten hinzufügen und abrufen
type: docs
weight: 20
url: /de/cpp/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 In[Zugriff auf Cells eines Arbeitsblatts](/cells/de/cpp/accessing-cells-of-a-worksheet/)haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt besprochen. Dieser Artikel verwendet einen dieser Ansätze, um Zellen verschiedene Datentypen hinzuzufügen.

{{% /alert %}} 
## **Hinzufügen von Daten zu Cells**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält eine[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet eine[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Jeder Artikel in der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung stellt ein Objekt der[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Klasse.

Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Daten zu den Zellen in Arbeitsblättern durch Aufrufen von[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Klasse[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) Methode. Aspose.Cells bietet überladene Versionen der[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9) Methode, mit der Entwickler Zellen verschiedene Arten von Daten hinzufügen können. Die Verwendung dieser überladenen Versionen der[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)-Methode ist es möglich, der Zelle einen Boolean-, String-, Double-, Integer- oder Datums-/Zeitwert usw. hinzuzufügen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-AddingDataToCells.cpp" >}}
### **Effizienz verbessern**
 Wenn du benutzt[PutValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4a5f4b8cdd54eccb4eb2ea51babcbca9)Um große Datenmengen in ein Arbeitsblatt einzufügen, sollten Sie den Zellen Werte hinzufügen, zuerst zeilenweise und dann spaltenweise. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.
## **Abrufen von Daten von Cells**
 Aspose.Cells bietet eine Klasse[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) das stellt eine Microsoft Excel-Datei dar. Das[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Klasse enthält eine[IArbeitsblätter](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse. Das[IArbeitsblatt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) Klasse bietet a[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung. Jeder Artikel in der[IZellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Sammlung stellt ein Objekt der[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)Klasse.

 Das[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)-Klasse stellt mehrere Methoden bereit, mit denen Entwickler Werte aus den Zellen gemäß ihren Datentypen abrufen können. Zu diesen Methoden gehören:

- [GetStringValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac048c664985e2cadc2404840599d7ac3), gibt den Zeichenfolgenwert der Zelle zurück.
- [GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a), gibt den doppelten Wert der Zelle zurück.
- [GetBoolValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ac61870c4b1d6a68077092fb043bf8741), gibt den booleschen Wert der Zelle zurück.
- [GetDateTimeValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7932b40c41141f716b096cc521113a61), gibt den Datums-/Uhrzeitwert der Zelle zurück.
- [GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44), gibt den Gleitkommawert der Zelle zurück.
- [GetIntValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7acc93c97c062cbd60a7f1ab00a022d8), gibt den ganzzahligen Wert der Zelle zurück.

 Wenn ein Feld nicht ausgefüllt ist, werden Zellen mit[GetDoubleValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a5f21cd4c755da84135176c74425f230a) oder[GetFloatValue](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a4e36c4be4c76447f54f8032b17cecf44)wirft eine Ausnahme.

 Die Art der in einer Zelle enthaltenen Daten kann auch mit überprüft werden[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Klasse[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) Methode. Tatsächlich ist die[ICell](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) Klasse[GetType](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a36708b1bad0bbf45cbf9577ccab101ba) Methode basiert auf der[CellValueType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a745bf00b4815ec8dcf1bd11922fa4b62)Enumeration, deren vordefinierte Werte unten aufgeführt sind:

|**Cell Werttypen**|**Beschreibung**|
|:- |:- |
|CellValueType_IsBool|Gibt an, dass der Zellenwert boolesch ist.|
|CellValueType_IsDateTime|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|CellValueType_IsNull|Stellt eine leere Zelle dar.|
|CellValueType_IsNumeric|Gibt an, dass der Zellenwert numerisch ist.|
|CellValueType_IsString|Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|CellValueType_IsUnknown|Gibt an, dass der Zellenwert unbekannt ist.|
Sie können auch die oben vordefinierten Zellenwerttypen verwenden, um sie mit dem Typ der in jeder Zelle vorhandenen Daten zu vergleichen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-AddAndRetrieveData-RetrievingDataFromCells.cpp" >}}
