---
title: Exportieren Sie Daten aus dem Arbeitsblatt in .NET
linktitle: Daten aus Arbeitsblatt exportieren
type: docs
weight: 180
url: /de/net/export-data-from-worksheet/
description: In diesem Artikel wird erläutert, wie Sie mit C# Daten aus einem Arbeitsblatt in eine Datentabelle exportieren oder importieren.
keywords: C# Export Data from Worksheet, C# Export Data to DataTable, Columns Containing Strongly Typed Data, Columns Containing Non-Strongly Typed Data, C# Export Range with flag to skip column name
---
##  Überblick

In diesem Artikel wird erläutert, wie Sie Ihre Arbeitsblattdaten mit C# in DataTable exportieren. Er behandelt die folgenden Themen

 _Format_:**Excel**
- [C# Excel zu DataTable](#csharp-excel-to-datatable)
- [C# Konvertieren Sie Excel in DataTable](#csharp-convert-excel-to-datatable)
- [C# Excel in DataTable importieren](#csharp-import-excel-to-datatable)
- [C# Export nach DataTable aus Excel](#csharp-export-to-datatable-from-excel)

 _Format_:**XLS**
- [C# XLS zu DataTable](#csharp-xls-to-datatable)
- [C# Konvertieren Sie XLS in DataTable](#csharp-convert-xls-to-datatable)
- [C# XLS in DataTable importieren](#csharp-import-xls-to-datatable)
- [C# Export nach DataTable von XLS](#csharp-export-to-datatable-from-xls)

 _Format_:**XLSX**
- [C# XLSX zu DataTable](#csharp-xlsx-to-datatable)
- [C# Konvertieren Sie XLSX in DataTable](#csharp-convert-xlsx-to-datatable)
- [C# XLSX in DataTable importieren](#csharp-import-xlsx-to-datatable)
- [C# Export nach DataTable von XLSX](#csharp-export-to-datatable-from-xlsx)

 _Format_:**ODS**
- [C# ODS zu DataTable](#csharp-ods-to-datatable)
- [C# Konvertieren Sie ODS in DataTable](#csharp-convert-ods-to-datatable)
- [C# ODS in DataTable importieren](#csharp-import-ods-to-datatable)
- [C# Export nach DataTable von ODS](#csharp-export-to-datatable-from-ods)

##  **So exportieren Sie Excel-Daten mit C#**

{{% alert color="primary" %}}

In diesem Artikel werden einige Datenexporttechniken erläutert, auf die Entwickler über Aspose.Cells Zugriff haben.

{{% /alert %}}

##  **So exportieren Sie Daten aus einem Arbeitsblatt**

 Aspose.Cells erleichtert seinen Benutzern nicht nur den Import von Daten aus externen Datenquellen in Arbeitsblätter, sondern ermöglicht ihnen auch den Export ihrer Arbeitsblattdaten in eine[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) . Wie wir das wissen[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ist Teil von ADO.NET und wird zur Speicherung von Daten verwendet. Sobald die Daten in einem gespeichert sind[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Es kann je nach den Anforderungen der Benutzer beliebig verwendet werden. Entwickler können diese Daten auch speichern (gespeichert in[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ) direkt in eine Datenbank übertragen, wenn sie dies wünschen. Wir können also sehen, dass es für die Entwickler einfacher wird, Arbeitsblattdaten zu manipulieren, wenn sie in ein exportiert werden[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8).

##  **So exportieren Sie Daten mit Aspose.Cells in DataTable**

 Entwickler können ihre Arbeitsblattdaten problemlos in ein exportieren[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Objekt durch Aufruf von entweder[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) oder[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)Klasse. Beide Methoden kommen in unterschiedlichen Szenarien zum Einsatz, auf die im Folgenden näher eingegangen wird.

##  **Spalten mit stark typisierten Daten**

 Wir wissen, dass eine Tabellenkalkulation Daten als Folge von Zeilen und Spalten speichert. Wenn alle Werte in den Spalten eines Arbeitsblatts stark typisiert sind (das bedeutet, dass alle Werte in einer Spalte denselben Datentyp haben müssen), können wir den Inhalt des Arbeitsblatts exportieren, indem wir aufrufen[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse.[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Die Methode verwendet die folgenden Parameter, um Arbeitsblattdaten zu exportieren als[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)Objekt:

- *Zeilennummer**, die Zeilennummer der ersten Zelle, aus der Daten exportiert werden.
- *Spaltennummer**, die Spaltennummer der ersten Zelle, aus der die Daten exportiert werden.
- *Anzahl der Zeilen**, die Anzahl der zu exportierenden Zeilen.
- *Anzahl der Spalten**, die Anzahl der zu exportierenden Spalten.
- *Spaltennamen exportieren**, eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Arbeitsblatts als Spaltennamen exportiert werden sollen[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)oder nicht.

_Schritte: Daten nach DataTable exportieren_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Schritte:</em> Excel zu DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Schritte:</em> XLS zu DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Schritte:</em> XLSX zu DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Schritte:</em> ODS zu DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Schritte:</em> Konvertieren Sie Excel in DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Schritte:</em> Konvertieren Sie XLS in DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Schritte:</em> Konvertieren Sie XLSX in DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Schritte:</em> Konvertieren Sie ODS in DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Schritte:</em> Importieren Sie Excel in DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Schritte:</em> Importieren Sie XLS in DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Schritte:</em> Importieren Sie XLSX in DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Schritte:</em> Importieren Sie ODS in DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Schritte:</em> Export nach DataTable aus Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Schritte:</em> Export nach DataTable von XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Schritte:</em> Export nach DataTable von XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Schritte:</em> Export nach DataTable von ODS in C#</strong></a>

_Codeschritte:_

1.  Laden Sie Ihre Excel-Datei hinein[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook/) Objekt.
   - [Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook/) Das Objekt kann Excel-Dateiformate laden, z. B. XLS, XLSX, XLSM, ODS usw.
 3. Greifen Sie auf den ersten zu[Arbeitsblatt](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) in der Excel-Datei.
4. Wählen Sie Ihren Exportbereich, z. B. 7 Zeilen und 2 Spalten, beginnend mit der 1. Zelle von *DataTable**.
 5. Verwendung[ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) Methode zum Exportieren der Daten in DataTable.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

##  **Spalten mit nicht stark typisierten Daten**

 Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (das heißt, die Werte in einer Spalte können unterschiedliche Datentypen haben), können wir den Inhalt des Arbeitsblatts exportieren, indem wir aufrufen[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index) Methode der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Klasse.[**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)Die Methode verwendet denselben Parametersatz wie die[**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)Methode zum Exportieren von Arbeitsblattdaten als[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

##  **So exportieren Sie einen Bereich mit der Markierung, den Spaltennamen zu überspringen**

 Daten aus einem Bereich können exportiert werden[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) Hier steht ein Flag zum Überspringen der Kopfzeile in den exportierten Daten zur Verfügung. Der folgende Code exportiert eine Reihe von Daten nach[**Datentabelle**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) mit einem Argument[**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions) was beinhaltet[**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname) Flagge. Es ist eingestellt**WAHR** Wenn Header-Informationen vorhanden sind, werden diese nicht in die Daten aufgenommen und auf gesetzt**FALSCH** wenn kein Header vorhanden ist und alle Zeilen als Daten betrachtet werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

##  **Vorabthemen**
- [Exportieren Sie Excel-Daten ohne Formatierung in DataTable](/cells/de/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportieren Sie den String-Wert HTML von Cells in die Datentabelle](/cells/de/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportieren Sie sichtbare Zeilendaten aus dem Arbeitsblatt](/cells/de/net/export-visible-rows-data-from-worksheet/)
- [Ignorieren Sie ausgeblendete Spalten beim Exportieren von Arbeitsblattdaten in eine Datentabelle](/cells/de/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Benennen Sie doppelte Spalten beim Exportieren von Arbeitsblattdaten automatisch um](/cells/de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
