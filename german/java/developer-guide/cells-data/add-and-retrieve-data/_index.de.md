---
title: Daten hinzufügen und abrufen
type: docs
weight: 20
url: /de/java/add-and-retrieve-data/
---

{{% alert color="primary" %}} 

In [Zugriff auf Zellen einer Arbeitsmappe](/cells/de/java/accessing-cells-of-a-worksheet/) haben wir grundlegende Ansätze zum Zugriff auf Zellen in einer Arbeitsmappe erörtert. Dieser Artikel verwendet einen dieser Ansätze, um verschiedene Arten von Daten zu Zellen hinzuzufügen.

{{% /alert %}} 
## **Hinzufügen von Daten zu Zellen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung repräsentiert ein Objekt der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse.

Mit Aspose.Cells können Entwickler Daten zu Zellen in Arbeitsmappen hinzufügen, indem sie die [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse und die Eigenschaft [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) aufrufen. Durch Verwendung der Eigenschaft [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) ist es möglich, boolesche, Zeichenfolgen, Gleitkommazahlen, ganze Zahlen oder Datum/Uhrzeit usw. Werte der Zelle hinzuzufügen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Effizienz verbessern**
{{% alert color="primary" %}} 

Wenn Sie die Eigenschaft [setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) verwenden, um eine große Menge an Daten zu einer Arbeitsmappe hinzuzufügen, sollten Sie die Werte zuerst nach Zeilen und dann nach Spalten zu den Zellen hinzufügen. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

{{% /alert %}} 

Bei der Arbeit mit Arbeitsmappen können Benutzer verschiedene Arten von Daten in den Zellen hinzufügen. Diese Datenelemente können boolesche, ganze Zahlen, Gleitkommazahlen, Texte oder Datum/Uhrzeitwerte enthalten. Sie können die entsprechenden Werte aus den Zellen gemäß ihren Datentypen mithilfe von Aspose.Cells abrufen.
## **Abrufen von Daten aus Zellen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)die eine Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse stellt eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung bereit. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung repräsentiert ein Objekt der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse.

Die [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse bietet mehrere Eigenschaften, die Entwicklern ermöglichen, Werte aus den Zellen gemäß ihrer Datentypen abzurufen. Diese Eigenschaften umfassen:

- [StringValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), der Zeichenfolgenwert der Zelle.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), gibt den Double-Wert der Zelle zurück.
- [BoolValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), der Boolscher Wert der Zelle.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), der Datum/Uhrzeit-Wert der Zelle.
- [FloatValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), der Float-Wert der Zelle.
- [IntValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), der Ganzzahl-Wert der Zelle.

Darüber hinaus kann der Datentyp, der in einer Zelle enthalten ist, auch mithilfe der [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) Eigenschaft der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse überprüft werden. Tatsächlich basiert die [Type](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) Eigenschaft der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse auf der [CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType) Aufzählung, deren vordefinierte Werte unten aufgeführt sind:

|**Zellwerttypen**|**Beschreibung**|
| :- | :- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Gibt an, dass der Zellenwert boolesch ist.
|[IS_DATE_TIME](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Stellt dar, dass die Zelle einen Fehlerwert enthält.
|[IS_NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Stellt eine leere Zelle dar.
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Gibt an, dass der Zellenwert numerisch ist.
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Gibt an, dass der Zellenwert eine Zeichenfolge ist.
|[IS_UNKNOWN](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Gibt an, dass der Zellenwert unbekannt ist.
Sie können auch die oben genannten vordefinierten Zellwerttypen verwenden, um den Typ der Daten in jeder Zelle zu vergleichen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
