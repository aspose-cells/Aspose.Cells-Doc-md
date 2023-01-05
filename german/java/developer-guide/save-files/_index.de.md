---
title: Speichern von Excel-Dateien in CSV, PDF und anderen Formaten
linktitle: Daten abspeichern
type: docs
weight: 20
url: /de/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells** ermöglicht Entwicklern, Excel-Dateien mit dem flexiblen API von Grund auf neu zu erstellen. Sobald Sie Excel-Dateien erstellt haben, müssen Sie auch Ihre Arbeitsmappe (Datei) speichern. Aspose.Cells bietet verschiedene Möglichkeiten, diese Dateien zu speichern. In diesem Thema werden wir all diese Möglichkeiten diskutieren, die von Entwicklern zum Speichern ihrer Dateien übernommen werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten zum Speichern Ihrer Dateien**

 Aspose.Cells API stellt eine Klasse mit dem Namen bereit[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)die eine Excel-Datei darstellt und alle notwendigen Eigenschaften und Methoden bereitstellt, die Entwickler möglicherweise benötigen, um mit ihren Excel-Dateien zu arbeiten. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse bietet a[**speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))-Methode, die zum Speichern von Excel-Dateien verwendet wird. Das[**speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))-Methode verfügt über viele Überladungen, die zum Speichern von Excel-Dateien auf unterschiedliche Weise verwendet werden.

 Entwickler können auch das Dateiformat angeben, in dem ihre Dateien gespeichert werden sollen. Die Dateien können in verschiedenen Formaten gespeichert werden, z. B. XLS, SpreadsheetML, CSV, Tabulatorgetrennt, Tabulatorgetrennte Werte TSV, XPS und viele mehr. Diese Dateiformate werden mit angegeben[**Format speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) Aufzählung.

[**Format speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)Enumeration enthält viele vordefinierte Dateiformate (die von Ihnen ausgewählt werden können) wie folgt:

|**Dateiformattypen**|**Beschreibung**|
|:- |:- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API versucht, das passende Format anhand der Dateierweiterung zu erkennen, die im ersten Parameter der Speichermethode angegeben ist|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Stellt eine CSV-Datei dar|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Stellt eine Office Open XML SpreadsheetML-Datei dar|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Stellt die XML-basierte XLSM-Datei dar|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Stellt eine Excel-Vorlagendatei dar|
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Stellt eine Excel-Makro-aktivierte Vorlagendatei dar|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Stellt eine Excel XLAM-Datei dar|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Stellt eine tabulatorgetrennte Wertedatei dar|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Stellt eine tabulatorgetrennte Textdatei dar|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Stellt eine HTML-Datei(en) dar|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Stellt eine MHTML-Datei(en) dar|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Stellt eine OpenDocument Spreadsheet-Datei dar|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Stellt eine XLS-Datei dar, die das Standardformat für Excel 1997 bis 2003-Revisionen ist|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Stellt eine SpreadSheetML-Datei dar|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Stellt eine Excel 2007-Binärdatei XLSB dar|
|[**UNBEKANNT**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Repräsentiert ein unbekanntes Format, kann nicht gespeichert werden.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Stellt ein PDF-Dokument dar|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Stellt eine XML-Papierspezifikationsdatei (XPS) dar|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Stellt eine Datei im Tagged Image File Format (TIFF) dar|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Stellt eine XML-basierte Scalable Vector Graphics-Datei (SVG) dar|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Stellt das Datenaustauschformat dar.|
|[**ZAHLEN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Stellt eine Numbers-Datei dar.|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Stellt ein Markdown-Dokument dar.|
**Normalerweise gibt es zwei Möglichkeiten, Excel-Dateien wie folgt zu speichern:**

1. **Speichern der Datei an einem Ort**
1. **Speichern der Datei in einem Stream**

## **Datei an einem Ort speichern**

Wenn Entwickler ihre Dateien an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der[**Format speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) Aufzählung) beim Aufrufen der[**speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) Methode von[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)Objekt.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Arbeitsmappe im Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das Format TXT.

Sie können dasselbe Beispiel ändern, um Ihre Datei unter CSV zu speichern.[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) ist ein Komma, geben Sie also kein Trennzeichen an, wenn Sie im Format CSV speichern.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Speichern von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien enthalten Tabellenkalkulationsdaten ohne Formatierung. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen zwischen ihren Daten haben kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Datei in einem Stream speichern**

 Wenn Entwickler ihre Dateien in einem**Strom** dann sollten sie eine erstellen**FileOutputStream** Objekt und speichern Sie dann die Datei darin**Strom** Objekt durch Aufrufen der[**speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) Methode von[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Objekt. Entwickler können auch das gewünschte Dateiformat angeben (mithilfe der[**Format speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) Aufzählung) beim Aufrufen der[**speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) Methode.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Datei in anderem Format speichern**

### **XLS Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Legen Sie die ContentCopyForAccessibility-Option fest**

 Mit dem[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) Klasse, können Sie die PDF erhalten oder einstellen[**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent)Option zum Steuern des Inhaltszugriffs in der konvertierten PDF. Dies bedeutet, dass Bildschirmlesesoftware den Text in der PDF-Datei zum Lesen der PDF-Datei verwenden kann. Sie können es deaktivieren, indem Sie ein Kennwort zum Ändern der Berechtigungen anwenden und die beiden Elemente im Screenshot deaktivieren[Hier](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Exportieren Sie benutzerdefinierte Eigenschaften nach PDF**

Mit dem[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) Klasse können Sie die benutzerdefinierten Eigenschaften in der Quellarbeitsmappe in die PDF exportieren.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) Enumerator wird bereitgestellt, um anzugeben, wie Eigenschaften exportiert werden. Diese Eigenschaften können in Adobe Acrobat Reader angezeigt werden, indem Sie auf Datei und dann auf die Option Eigenschaften klicken, wie in der folgenden Abbildung gezeigt. Die Vorlagendatei „sourceWithCustProps.xlsx“ kann heruntergeladen werden[Hier](sourceWithCustProps.xlsx)zum Testen und Ausgeben steht die PDF-Datei "outSourceWithCustProps" zur Verfügung[Hier](outSourceWithCustProps.pdf)zur Analyse.

![todo: Bild_alt_Text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Konvertieren Sie eine Excel-Arbeitsmappe in Markdown**

Die Aspose.Cells API bietet Unterstützung für den Export von Tabellenkalkulationen in das Markdown-Format. Um das aktive Arbeitsblatt nach Markdown zu exportieren, pass[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)als zweiter Parameter von[**Arbeitsmappe.Speichern**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) Methode. Sie können auch verwenden[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)-Klasse, um zusätzliche Einstellungen für das Exportieren von Arbeitsblättern nach Markdown anzugeben.

Das folgende Codebeispiel veranschaulicht das Exportieren eines aktiven Arbeitsblatts nach Markdown mithilfe von[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)Aufzählungsmitglied. Bitte sehen Sie sich ... an[Markdown-Datei ausgeben](Book1.txt)generiert durch den Code als Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Themen vorantreiben**
- [Passen Sie die Komprimierungsstufe der Arbeitsmappe an](/cells/de/java/adjust-workbook-compression-level/)
- [Konvertieren von Arbeitsmappen in verschiedene Formate](/cells/de/java/converting-workbook-to-different-formats/)
- [Speichern Sie die Arbeitsmappe im strikt offenen XML-Tabellenformat](/cells/de/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Verfolgen Sie den Konvertierungsfortschritt von Excel bis TIFF](/cells/de/java/track-conversion-progress-of-excel-to-tiff/)
- [Verfolgen Sie den Fortschritt der Dokumentenkonvertierung](/cells/de/java/track-document-conversion-progress/)
