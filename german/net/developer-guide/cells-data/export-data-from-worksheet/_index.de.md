---
title: Daten aus Arbeitsblatt in .NET exportieren
linktitle: Daten aus Arbeitsblatt exportieren
type: docs
weight: 180
url: /de/net/export-data-from-worksheet/
description: In diesem Artikel wird erklärt, wie Daten aus einem Arbeitsblatt in eine DataTable in C# exportiert oder importiert werden können.
keywords: C# Daten aus Arbeitsblatt exportieren, C# Daten in DataTable exportieren, Spalten mit stark typisierten Daten, Spalten mit nicht stark typisierten Daten, C# Bereich mit Flag zum Überspringen des Spaltennamens exportieren, C# Bereich mit Kopfzeile exportieren.
---

## Übersicht

In diesem Artikel wird erläutert, wie Sie Ihre Arbeitsblattdaten mit C# in eine DataTable exportieren können. Dabei werden die folgenden Themen behandelt

_Format_: **Excel**
- [C# Excel zu DataTable](#csharp-excel-to-datatable)
- [C# Konvertiere Excel zu DataTable](#csharp-convert-excel-to-datatable)
- [C# Importiere Excel zu DataTable](#csharp-import-excel-to-datatable)
- [C# Exportiere DataTable von Excel](#csharp-export-to-datatable-from-excel)

_Format_: **XLS**
- [C# XLS zu DataTable](#csharp-xls-to-datatable)
- [C# Konvertiere XLS zu DataTable](#csharp-convert-xls-to-datatable)
- [C# Importiere XLS zu DataTable](#csharp-import-xls-to-datatable)
- [C# Exportiere DataTable von XLS](#csharp-export-to-datatable-from-xls)

_Format_: **XLSX**
- [C# XLSX zu DataTable](#csharp-xlsx-to-datatable)
- [C# Konvertiere XLSX zu DataTable](#csharp-convert-xlsx-to-datatable)
- [C# Importiere XLSX zu DataTable](#csharp-import-xlsx-to-datatable)
- [C# Exportiere DataTable von XLSX](#csharp-export-to-datatable-from-xlsx)

 _Format_: **ODS** 
- [C# ODS zu DataTable](#csharp-ods-to-datatable)
- [C# Konvertiere ODS zu DataTable](#csharp-convert-ods-to-datatable)
- [C# Importiere ODS zu DataTable](#csharp-import-ods-to-datatable)
- [C# Exportiere DataTable von ODS](#csharp-export-to-datatable-from-ods)

## **Wie man Excel-Daten mit C# exportiert**

{{% alert color="primary" %}}

Dieser Artikel behandelt einige Techniken zum Datenexport, auf die Entwickler über Aspose.Cells zugreifen können.

{{% /alert %}}

## **Wie man Daten aus einem Arbeitsblatt exportiert**

Aspose.Cells erleichtert seinen Benutzern nicht nur das Importieren von Daten aus externen Datenquellen in Arbeitsblätter, sondern erlaubt es ihnen auch, ihre Arbeitsblattdaten in ein [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) zu exportieren. Da wir wissen, dass [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) ein Teil von ADO.NET ist und zum Halten von Daten verwendet wird. Sobald die Daten in einem [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) gespeichert sind, können sie nach den Anforderungen der Benutzer verwendet werden. Entwickler können diese Daten (die in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) gespeichert sind) auch direkt in einer Datenbank speichern, wenn sie möchten. So wird es für die Entwickler einfacher, Arbeitsblattdaten zu manipulieren, wenn sie in ein [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) exportiert werden.

## **Wie man Daten mit Aspose.Cells in ein DataTable exportiert**

Entwickler können ihre Arbeitsblattdaten leicht in ein [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)-Objekt exportieren, indem sie entweder die [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)- oder [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-Methode der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Klasse aufrufen. Beide Methoden werden in verschiedenen Szenarien verwendet, die im Folgenden ausführlicher erläutert werden.

## **Spalten mit stark typisierten Daten**

Wir wissen, dass in einem Arbeitsblatt Daten als Folge von Zeilen und Spalten gespeichert werden. Wenn alle Werte in den Spalten eines Arbeitsblatts stark typisiert sind (das bedeutet, dass alle Werte in einer Spalte den gleichen Datentyp haben müssen), können wir den Arbeitsblattinhalt exportieren, indem wir die [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)-Methode der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Klasse aufrufen. Die [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)-Methode verwendet die folgenden Parameter, um Arbeitsblattdaten als [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)-Objekt zu exportieren:

- **Zeilennummer**, die Zeilennummer, von der die Daten der ersten Zelle exportiert werden.
- **Spaltennummer**, die Spaltennummer der ersten Zelle, aus der die Daten exportiert werden.
- **Anzahl der Zeilen**, die Anzahl der zu exportierenden Zeilen.
- **Anzahl der Spalten**, die Anzahl der zu exportierenden Spalten.
- **Spaltennamen exportieren**, eine boolesche Eigenschaft, die angibt, ob die Daten in der ersten Zeile des Arbeitsblatts als Spaltennamen des [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) exportiert werden sollen oder nicht.

_Schritte: Daten in DataTable exportieren_

- <a name="csharp-excel-to-datatable" id="csharp-excel-to-datatable"><strong><em>Schritte:</em> Excel to DataTable in C#</strong></a>
  - <a name="csharp-xls-to-datatable" id="csharp-xls-to-datatable"><strong><em>Schritte:</em> XLS to DataTable in C#</strong></a>
  - <a name="csharp-xlsx-to-datatable" id="csharp-xlsx-to-datatable"><strong><em>Schritte:</em> XLSX to DataTable in C#</strong></a>
  - <a name="csharp-ods-to-datatable" id="csharp-ods-to-datatable"><strong><em>Schritte:</em> ODS to DataTable in C#</strong></a>
- <a name="csharp-convert-excel-to-datatable" id="csharp-convert-excel-to-datatable"><strong><em>Schritte:</em> Convert Excel to DataTable in C#</strong></a>
  - <a name="csharp-convert-xls-to-datatable" id="csharp-convert-xls-to-datatable"><strong><em>Schritte:</em> Convert XLS to DataTable in C#</strong></a>
  - <a name="csharp-convert-xlsx-to-datatable" id="csharp-convert-xlsx-to-datatable"><strong><em>Schritte:</em> Convert XLSX to DataTable in C#</strong></a>
  - <a name="csharp-convert-ods-to-datatable" id="csharp-convert-ods-to-datatable"><strong><em>Schritte:</em> Convert ODS to DataTable in C#</strong></a>
- <a name="csharp-import-excel-to-datatable" id="csharp-import-excel-to-datatable"><strong><em>Schritte:</em> Import Excel to DataTable in C#</strong></a>
  - <a name="csharp-import-xls-to-datatable" id="csharp-import-xls-to-datatable"><strong><em>Schritte:</em> Import XLS to DataTable in C#</strong></a>
  - <a name="csharp-import-xlsx-to-datatable" id="csharp-import-xlsx-to-datatable"><strong><em>Schritte:</em> Import XLSX to DataTable in C#</strong></a>
  - <a name="csharp-import-ods-to-datatable" id="csharp-import-ods-to-datatable"><strong><em>Schritte:</em> Import ODS to DataTable in C#</strong></a>
- <a name="csharp-export-to-datatable-from-excel" id="csharp-export-to-datatable-from-excel"><strong><em>Schritte:</em> Export to DataTable from Excel in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xls" id="csharp-export-to-datatable-from-xls"><strong><em>Schritte:</em> Export to DataTable from XLS in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-xlsx" id="csharp-export-to-datatable-from-xlsx"><strong><em>Schritte:</em> Export to DataTable from XLSX in C#</strong></a>
  - <a name="csharp-export-to-datatable-from-ods" id="csharp-export-to-datatable-from-ods"><strong><em>Schritte:</em> Export to DataTable from ODS in C#</strong></a>

_Code Schritte:_

1. Laden Sie Ihre Excel-Datei im [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-Objekt.
   - [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)-Objekt kann Excel-Dateiformate wie z.B. XLS, XLSX, XLSM, ODS usw. laden.
3. Greifen Sie auf das erste [Worksheet](https://reference.aspose.com/cells/net/aspose.cells/worksheet/) in der Excel-Datei zu.
4. Wählen Sie Ihren Exportbereich z.B. 7 Zeilen und 2 Spalten ab dem 1. Zelle des **DataTable**.
5. Verwenden Sie die Methode [ExportDataTable](https://reference.aspose.com/cells/net/aspose.cells/cells/exportdatatable/) um die Daten in ein DataTable zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingStronglyTypedData-1.cs" >}}

## **Spalten mit nicht stark typisierten Daten**

Wenn alle Werte in den Spalten eines Arbeitsblatts nicht stark typisiert sind (das bedeutet, dass die Werte in einer Spalte verschiedene Datentypen haben können), dann können wir den Inhalt des Arbeitsblatts exportieren, indem wir die [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-Methode der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)-Klasse aufrufen. Die [**ExportDataTableAsString**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatableasstring/index)-Methode nimmt dieselben Parameter wie die [**ExportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index)-Methode entgegen, um die Arbeitsblattdaten als [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8)-Objekt zu exportieren.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportColumnContainingNonStronglyTypedData-1.cs" >}}

## **Wie man einen Bereich mit Kopfzeile exportiert**

Daten aus einem Bereich können in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) exportiert werden, wobei ein Flag vorhanden ist, um die Kopfzeile in den exportierten Daten zu überspringen. Der folgende Code exportiert einen Datenbereich in [**DataTable**](https://docs.microsoft.com/en-gb/dotnet/api/system.data.datatable?view=netframework-4.8) mit einem Argument [**ExportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions), der [**ExportColumnName**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/exportcolumnname)-Flag enthält. Es ist auf **true** gesetzt, wenn Kopfzeilendaten vorhanden sind, daher werden sie nicht in die Daten aufgenommen, und auf **false** gesetzt, wenn keine Kopfzeile vorhanden ist und alle Zeilen als Daten betrachtet werden sollen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-ExportRangeWithFlagToSkipColumnHeader-1.cs" >}}

## **Erweiterte Themen**
- [Exportieren Sie Excel-Daten in eine DataTable ohne jegliche Formatierung](/cells/de/net/export-excel-data-to-datatable-without-any-formatting/)
- [Exportieren Sie den HTML-Stringwert der Zellen in die DataTable](/cells/de/net/export-html-string-value-of-the-cells-to-the-datatable/)
- [Exportieren Sie sichtbare Zeilendaten aus dem Arbeitsblatt](/cells/de/net/export-visible-rows-data-from-worksheet/)
- [Ignorieren Sie ausgeblendete Spalten beim Exportieren von Arbeitsblattdaten in die Datenbank](/cells/de/net/ignore-hidden-columns-while-exporting-worksheet-data-to-data-table/)
- [Benennen Sie doppelte Spalten automatisch um, während Sie Arbeitsblattdaten exportieren](/cells/de/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/)
{{< app/cells/assistant language="csharp" >}}
