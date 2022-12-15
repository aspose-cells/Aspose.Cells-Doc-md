---
title: Daten hinzufügen und abrufen
type: docs
weight: 20
url: /de/java/add-and-retrieve-data/
---
{{% alert color="primary" %}} 

 Im[Zugriff auf Cells eines Arbeitsblatts](/cells/de/java/accessing-cells-of-a-worksheet/)haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt besprochen. Dieser Artikel verwendet einen dieser Ansätze, um Zellen verschiedene Datentypen hinzuzufügen.

{{% /alert %}} 
## **Hinzufügen von Daten zu Cells**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

 Aspose.Cells ermöglicht es Entwicklern, Daten zu Zellen in Arbeitsblättern hinzuzufügen, indem sie die[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse'[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Eigentum. Durch die Verwendung der[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)-Eigenschaft ist es möglich, Boolean-, String-, Double-, Integer- oder Datum/Uhrzeit-Werte usw. zur Zelle hinzuzufügen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingDataToCells-AddingDataToCells.java" >}}
### **Effizienz verbessern**
{{% alert color="primary" %}} 

 Wenn Sie die verwenden[setValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Eigenschaft Um einem Arbeitsblatt eine große Datenmenge hinzuzufügen, sollten Sie den Zellen Werte hinzufügen, zuerst nach Zeilen und dann nach Spalten. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

{{% /alert %}} 

Während der Arbeit an Arbeitsblättern können Benutzer verschiedene Arten von Daten in die Zellen einfügen. Diese Datenelemente können boolesche, ganze Zahlen, Fließkomma-, Text- oder Datums-/Zeitwerte enthalten. Mit Aspose.Cells können Sie die entsprechenden Werte aus den Zellen entsprechend ihres Datentyps abrufen.
## **Abrufen von Daten von Cells**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) die eine Excel-Datei darstellt.[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

 Das[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Die Klasse stellt mehrere Eigenschaften bereit, die es Entwicklern ermöglichen, Werte aus den Zellen gemäß ihren Datentypen abzurufen. Zu diesen Eigenschaften gehören:

- [Zeichenfolgenwert](https://reference.aspose.com/cells/java/com.aspose.cells/cell#StringValue), der Zeichenfolgenwert der Zelle.
- [DoubleValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DoubleValue), gibt den Double-Wert der Zelle zurück.
- [BoolWert](https://reference.aspose.com/cells/java/com.aspose.cells/cell#BoolValue), der boolesche Wert der Zelle.
- [DateTimeValue](https://reference.aspose.com/cells/java/com.aspose.cells/cell#DateTimeValue), der Datums-/Uhrzeitwert der Zelle.
- [Gleitkommawert](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FloatValue), der Gleitkommawert der Zelle.
- [IntWert](https://reference.aspose.com/cells/java/com.aspose.cells/cell#IntValue), der ganzzahlige Wert der Zelle.

 Darüber hinaus kann die Art der in einer Zelle enthaltenen Daten auch mit überprüft werden[Typ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) Eigentum der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse. Tatsächlich ist die[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse'[Typ](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Type) Eigentum basiert auf[CellValueType](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueType)Enumeration, deren vordefinierte Werte unten aufgeführt sind:

|**Cell Werttypen**|**Beschreibung**|
|:- |:- |
|[IS_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_BOOL)|Gibt an, dass der Zellenwert boolesch ist.|
|[IST_DATUM_ZEIT](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_DATE_TIME)|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|[IS_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_ERROR)|Stellt dar, dass die Zelle einen Fehlerwert enthält|
|[IST NULL](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NULL)|Stellt eine leere Zelle dar.|
|[IS_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_NUMERIC)|Gibt an, dass der Zellenwert numerisch ist.|
|[IS_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_STRING)|Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|[IST UNBEKANNT](https://reference.aspose.com/cells/java/com.aspose.cells/cellvaluetype#IS_UNKNOWN)|Gibt an, dass der Zellenwert unbekannt ist.|
Sie können auch die oben vordefinierten Zellenwerttypen verwenden, um sie mit dem Typ der in jeder Zelle vorhandenen Daten zu vergleichen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RetrievingDataFromCells-RetrievingDataFromCells.java" >}}
