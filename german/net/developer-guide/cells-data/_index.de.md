---
title: Daten von Excel-Dateien verwalten
linktitle: Cells Daten
type: docs
weight: 110
url: /de/net/view-and-edit-excel-data/
description: In diesem Artikel wird beschrieben, wie Sie Daten von Excel-Dateien mit der Bibliothek Aspose.Cells anzeigen und bearbeiten.
keywords: Aspose.Cells C# Manage data of Excel file, add data to Excel file, get data from excel file, How to Improve Efficiency of adding data, manage cells data, update cells data, get cells data, insert cells data
---
{{% alert color="primary" %}}

 In[Zugriff auf Cells eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/)haben wir grundlegende Ansätze für den Zugriff auf Zellen in einem Arbeitsblatt besprochen. In diesem Artikel wird einer dieser Ansätze verwendet, um Zellen verschiedene Datentypen hinzuzufügen.

{{% /alert %}}

##  **So fügen Sie Daten zu Cells hinzu**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Microsoft Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Daten zu den Zellen in Arbeitsblättern durch Aufrufen von[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse'[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Methode. Aspose.Cells bietet überladene Versionen von[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) Methode, mit der Entwickler Zellen verschiedene Arten von Daten hinzufügen können. Mit diesen überladenen Versionen von[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Mit der Methode ist es möglich, der Zelle boolesche, Zeichenfolgen-, Doppel-, Ganzzahl- oder Datums-/Uhrzeitwerte usw. hinzuzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-AddingDataToCells-1.cs" >}}

##  **So verbessern Sie die Effizienz**

 Wenn du benutzt[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Wenn Sie mit dieser Methode eine große Datenmenge in ein Arbeitsblatt einfügen möchten, sollten Sie Werte zu den Zellen hinzufügen, zuerst nach Zeilen und dann nach Spalten. Dieser Ansatz verbessert die Effizienz Ihrer Anwendungen erheblich.

##  **So rufen Sie Daten von Cells ab**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf Arbeitsblätter in der Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Die Klasse stellt mehrere Eigenschaften bereit, die es Entwicklern ermöglichen, Werte aus den Zellen entsprechend ihrem Datentyp abzurufen. Zu diesen Eigenschaften gehören:

- [**StringValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/stringvalue): Gibt den String-Wert der Zelle zurück.
- [**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue): Gibt den doppelten Wert der Zelle zurück.
- [**BoolWert**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/boolvalue): Gibt den booleschen Wert der Zelle zurück.
- [**DateTimeValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/datetimevalue): Gibt den Datums-/Uhrzeitwert der Zelle zurück.
- [**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue): Gibt den Float-Wert der Zelle zurück.
- [**IntValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/intvalue): Gibt den ganzzahligen Wert der Zelle zurück.

 Wenn ein Feld nicht gefüllt ist, werden Zellen mit[**DoubleValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/doublevalue) oder[**FloatValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/floatvalue)löst eine Ausnahme aus.

 Der Typ der in einer Zelle enthaltenen Daten kann auch mithilfe von überprüft werden[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) Eigentum. Tatsächlich ist die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse'[**Typ**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/type) Die Eigenschaft basiert auf der[**CellValueType**](https://reference.aspose.com/cells/net/aspose.cells/cellvaluetype)Aufzählung, deren vordefinierte Werte unten aufgeführt sind:

|**Cell Werttypen**|**Beschreibung**|
| :- | :- |
|IsBool|Gibt an, dass der Zellenwert boolesch ist.|
|IsDateTime|Gibt an, dass der Zellenwert Datum/Uhrzeit ist.|
|Ist Null|Stellt eine leere Zelle dar.|
|IsNumeric|Gibt an, dass der Zellenwert numerisch ist.|
|IsString|Gibt an, dass der Zellenwert eine Zeichenfolge ist.|
|Ist unbekannt|Gibt an, dass der Zellenwert unbekannt ist.|

Sie können auch die oben vordefinierten Zellwerttypen verwenden, um sie mit dem in jeder Zelle vorhandenen Datentyp zu vergleichen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-RetrievingDataFromCells-1.cs" >}}

{{% alert color="primary" %}}

Während der Arbeit an Arbeitsblättern können Benutzer den Zellen verschiedene Arten von Daten hinzufügen. Diese Datentypen können boolesche, ganzzahlige, Gleitkomma-, Text- oder Datums-/Uhrzeitwerte umfassen. Mit Aspose.Cells können Sie entsprechend ihrem Datentyp die entsprechenden Werte aus den Zellen abrufen.

{{% /alert %}}

##  **Vorabthemen**
- [Zugriff auf Cells eines Arbeitsblatts](/cells/de/net/accessing-cells-of-a-worksheet/)
- [Konvertieren Sie numerische Textdaten in Zahlen](/cells/de/net/convert-text-numeric-data-to-number/)
- [Zwischensummen erstellen](/cells/de/net/creating-subtotals/)
- [Datenfilterung](/cells/de/net/data-filtering/)
- [Datensortierung](/cells/de/net/sort-data-of-excel/)
- [Datenvalidierung](/cells/de/net/data-validation/)
- [Daten aus Arbeitsblatt exportieren](/cells/de/net/export-data-from-worksheet/)
- [Daten suchen oder suchen](/cells/de/net/find-or-search-data/)
- [Erhalten Sie den String-Wert Cell mit und ohne Formatierung](/cells/de/net/get-cell-string-value-with-and-without-formatting/)
- [Hinzufügen von HTML Rich Text innerhalb der Cell](/cells/de/net/adding-html-rich-text-inside-the-cell/)
- [Fügen Sie Hyperlinks in Excel oder OpenOffice ein](/cells/de/net/insert-hyperlinks-to-excel/)
- [Daten in Arbeitsblatt importieren](/cells/de/net/import-data-into-worksheet/)
- [Wie und wo Enumeratoren verwendet werden](/cells/de/net/how-and-where-to-use-enumerators/)
- [Messen Sie die Breite und Höhe des Werts Cell in der Einheit Pixel](/cells/de/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Cell-Werte in mehreren Threads gleichzeitig lesen](/cells/de/net/reading-cell-values-in-multiple-threads-simultaneously/)
- [Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex](/cells/de/net/names-and-indices/)
- [Füllen Sie die Daten zuerst nach Zeile und dann nach Spalte aus](/cells/de/net/populate-data-first-by-row-then-by-column/)
- [Behalten Sie das einfache Anführungszeichen-Präfix des Werts oder Bereichs Cell bei](/cells/de/net/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Greifen Sie auf die Rich-Text-Teile von Cell zu und aktualisieren Sie sie](/cells/de/net/access-and-update-the-portions-of-rich-text-of-cell/)



