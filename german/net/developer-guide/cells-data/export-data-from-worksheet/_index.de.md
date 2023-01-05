---
title: Exportieren Sie Daten aus dem Arbeitsblatt in .NET
linktitle: Daten aus Arbeitsblatt exportieren
type: docs
weight: 180
url: /de/net/export-data-from-worksheet/
description: In diesem Artikel wird erläutert, wie Sie mit C# Daten aus einem Arbeitsblatt in eine Datentabelle exportieren oder importieren.
---
## Überblick

In diesem Artikel wird erläutert, wie Sie Ihre Arbeitsblattdaten mit C# in DataTable exportieren. Er behandelt die folgenden Themen

_Format_: **Excel**
- [C# Excel zu DataTable](#csharp-excel-to-datatable)
- [C# Konvertieren Sie Excel in DataTable](#csharp-convert-excel-to-datatable)
- [C# Excel in DataTable importieren](#csharp-import-excel-to-datatable)
- [C# Export nach DataTable aus Excel](#csharp-export-to-datatable-from-excel)

_Format_: **XLS**
- [C# XLS zu DataTable](#csharp-xls-to-datatable)
- [C# Konvertieren Sie XLS in DataTable](#csharp-convert-xls-to-datatable)
- [C# Importieren Sie XLS in DataTable](#csharp-import-xls-to-datatable)
- [C# Export in DataTable von XLS](#csharp-export-to-datatable-from-xls)

_Format_: **XLSX**
- [C# XLSX zu DataTable](#csharp-xlsx-to-datatable)
- [C# Konvertieren Sie XLSX in DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importieren Sie XLSX in DataTable](#csharp-import-xlsx-to-datatable)
- [C# Export in DataTable von XLSX](#csharp-export-to-datatable-from-xlsx)

_Format_: **ODS**
- [C# ODS zu DataTable](#csharp-ods-to-datatable)
- [C# Konvertieren Sie ODS in DataTable](#csharp-convert-ods-to-datatable)
- [C# Importieren Sie ODS in DataTable](#csharp-import-ods-to-datatable)
- [C# Export in DataTable von ODS](#csharp-export-to-datatable-from-ods)

## **C# Excel-Daten exportieren**

{{% alert color="primary" %}}

In diesem Artikel werden einige Datenexporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

{{% /alert %}}

## **Daten aus Arbeitsblatt exportieren**

 Aspose.Cells erleichtert seinen Benutzern nicht nur den Import von Daten in Arbeitsblätter aus externen Datenquellen, sondern ermöglicht ihnen auch den Export ihrer Arbeitsblattdaten in a[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Wie wir das kennen[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ist Teil von ADO.NET und dient zum Speichern von Daten. Sobald die Daten in a gespeichert sind[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) , es kann auf beliebige Weise gemäß den Anforderungen der Benutzer verwendet werden. Entwickler können diese Daten auch speichern (gespeichert in[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) auf Wunsch direkt in eine Datenbank. Wir können also sehen, dass es für die Entwickler einfacher wird, Arbeitsblattdaten zu manipulieren, wenn sie in eine exportiert werden[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

## **Exportieren von Daten in DataTable mit Aspose.Cells**

 Entwickler können ihre Arbeitsblattdaten einfach in eine[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Objekt durch Aufrufen von entweder[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) oder[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse. Beide Methoden werden in unterschiedlichen Szenarien verwendet, auf die weiter unten näher eingegangen wird.

## **Spalten mit stark typisierten Daten**

Wir wissen, dass eine Tabelle Daten als eine Folge von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Arbeitsblatts stark typisiert sind (d. h. alle Werte in einer Spalte müssen denselben Datentyp haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) -Methode verwendet die folgenden Parameter, um Arbeitsblattdaten als zu exportieren[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)Objekt:

- **Zeilennummer**, die Zeilennummer der ersten Zelle, aus der Daten exportiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, aus der die Daten exportiert werden.
- **Anzahl der Reihen**, die Anzahl der zu exportierenden Zeilen.
- **Anzahl der Spalten**, die Anzahl der zu exportierenden Spalten.
- **Spaltennamen exportieren** , eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Arbeitsblatts als Spaltennamen der exportiert werden sollen[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)oder nicht.

_Schritte: Exportieren von Daten in DataTable_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Schritte:</em> Excel zu DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Schritte:</em> XLS zu DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Schritte:</em> XLSX zu DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Schritte:</em> ODS zu DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Schritte:</em> Konvertieren Sie Excel in DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Schritte:</em>Konvertieren Sie XLS in DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Schritte:</em>Konvertieren Sie XLSX in DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Schritte:</em>Konvertieren Sie ODS in DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Schritte:</em> Importieren Sie Excel in DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Schritte:</em> Importieren Sie XLS in DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Schritte:</em> Importieren Sie XLSX in DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Schritte:</em> Importieren Sie ODS in DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Schritte:</em> Export nach DataTable aus Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Schritte:</em> Export nach DataTable von XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Schritte:</em> Export nach DataTable von XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Schritte:</em> Export nach DataTable von ODS in C#</strong></a>

_Codeschritte:_

1.  Laden Sie Ihre Excel-Datei in[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook/) Objekt.
   - [Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook/) Objekt kann Excel-Dateiformate laden, z. B. XLS, XLSX, XLSM, ODS usw.
 3. Greifen Sie auf die erste zu[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) in der Excel-Datei.
 4. Wählen Sie Ihren Exportbereich zB 7 Zeilen und 2 Spalten ab 1. Zelle aus**Datentabelle**.
 5. Verwenden[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) Methode zum Exportieren der Daten in DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Spalten mit nicht stark typisierten Daten**

 Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (d. h. die Werte in einer Spalte können unterschiedliche Datentypen haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir die aufrufen[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-Methode verwendet denselben Satz von Parametern wie die der[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)Methode zum Exportieren von Arbeitsblattdaten als[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Exportbereich mit Flag zum Überspringen des Spaltennamens**

Daten aus einem Bereich können exportiert werden[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) wo ein Flag verfügbar ist, um Kopfzeilen in den exportierten Daten zu überspringen. Der folgende Code exportiert eine Reihe von Daten nach[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) mit Argument[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) was beinhaltet[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) Flagge. Es ist eingestellt**wahr** Wenn Header-Informationen vorhanden sind, werden sie daher nicht in die Daten aufgenommen und auf gesetzt**FALSCH** wenn kein Header vorhanden ist und alle Zeilen als Daten betrachtet werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Themen vorantreiben**
- [Exportieren Sie Excel-Daten ohne Formatierung in DataTable](/cells/de/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportieren Sie den HTML-Zeichenfolgenwert von Cells in die DataTable](/cells/de/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportieren Sie sichtbare Zeilendaten aus dem Arbeitsblatt](/cells/de/net/export-visible-rows-data-from-worksheet/)
- [Ausgeblendete Spalten beim Exportieren von Arbeitsblattdaten in eine Datentabelle ignorieren](/cells/de/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um](/cells/de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
