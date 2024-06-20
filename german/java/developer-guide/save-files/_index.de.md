---
title: Speichern von Excel Dateien in CSV, PDF und anderen Formaten
linktitle: Dateien speichern
type: docs
weight: 20
url: /de/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** ermöglicht es Entwicklern, Excel-Dateien von Grund auf mit seiner flexiblen API zu erstellen. Sobald Sie Excel-Dateien erstellt haben, müssen Sie auch Ihre Arbeitsmappe (Datei) speichern. Aspose.Cells bietet eine Vielzahl von Möglichkeiten, um diese Dateien zu speichern. In diesem Thema werden alle möglichen Wege diskutiert, die von Entwicklern angenommen werden können, um ihre Dateien zu speichern.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Ihre Dateien zu speichern**

Aspose.Cells API bietet eine Klasse namens [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Excel-Datei darstellt und alle erforderlichen Eigenschaften und Methoden für Entwickler bereitstellt, um mit ihren Excel-Dateien zu arbeiten. Die Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) bietet eine [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))-Methode zur Speicherung von Excel-Dateien. Die Methode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) hat viele Überladungen, die verwendet werden, um Excel-Dateien auf verschiedene Arten zu speichern.

Entwickler können auch das Dateiformat angeben, in dem ihre Dateien gespeichert werden sollen. Die Dateien können in mehreren Formaten wie XLS, SpreadsheetML, CSV, Tabulatorgetrennt, TSV, XPS und vielen anderen gespeichert werden. Diese Dateiformate werden unter Verwendung der [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-Enumeration angegeben.

Die [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-Enumeration enthält viele vordefinierte Dateiformate (die von Ihnen ausgewählt werden können) wie folgt:

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API versucht, das geeignete Format anhand der im ersten Parameter der Save-Methode angegebenen Dateierweiterung zu erkennen.
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Stellt eine CSV-Datei dar.
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Stellt eine Office Open XML SpreadsheetML-Datei dar
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Stellt eine XLSM-Datei auf XML-Basis dar
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Stellt eine Excel-Template-Datei dar
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Stellt eine Excel-Macro-fähige Vorlagen-Datei dar
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Stellt eine Excel XLAM-Datei dar
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Stellt eine tabulatorgetrennte Werte-Datei dar
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Stellt eine tabellarische Textdatei dar
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Stellt eine HTML-Datei(en) dar
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Stellt eine MHTML-Datei(en) dar
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Stellt eine OpenDocument-Spreadsheetdatei dar
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Stellt eine XLS-Datei im Standardformat für Excel 1997 bis 2003 dar
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Stellt eine SpreadSheetML-Datei dar
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Stellt eine binäre XLSB-Datei von Excel 2007 dar
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Stellt ein nicht erkanntes Format dar, das nicht gespeichert werden kann
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Stellt ein PDF-Dokument dar
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Stellt eine XML Paper Specification (XPS)-Datei dar
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Stellt eine TIFF-Datei dar
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Stellt eine XML-basierte Scalable Vector Graphics (SVG)-Datei dar
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Stellt ein Datenaustauschformat dar
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Stellt eine Zahlen-Datei dar
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Stellt ein Markdown-Dokument dar.
**Normalerweise gibt es zwei Möglichkeiten, Excel-Dateien wie folgt zu speichern:**

1. **Datei an einem bestimmten Ort speichern**
1. **Datei in einem Stream speichern**

## **Datei an einem bestimmten Speicherort speichern**

Wenn Entwickler ihre Dateien an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-Enumeration) angeben, während sie die Methode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) des Objekts [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) aufrufen.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Arbeitsmappe in Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern im Textformat konvertieren oder speichern. Für Textformate (z.B. TXT, TabDelim, CSV etc.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das TXT-Format.

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) ein Komma, geben Sie also keinen Separator an, wenn Sie im CSV-Format speichern.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Textdateien mit benutzerdefiniertem Trennzeichen speichern**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Datei in einen Stream speichern**

Wenn Entwickler ihre Dateien in einen **Stream** speichern müssen, sollten sie ein **FileOutputStream**-Objekt erstellen und dann die Datei in dieses **Stream**-Objekt speichern, indem sie die Methode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) des Objekts [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) aufrufen. Entwickler können auch das gewünschte Dateiformat (unter Verwendung der [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)-Enumeration) beim Aufrufen der Methode [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) angeben.

**Beispiel:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Datei in einem anderen Format speichern**

### **XLS-Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **XLSX-Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **PDF-Dateien**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Option ContentCopyForAccessibility festlegen**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) können Sie die PDF-Option [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) festlegen, um den Zugriff auf den Inhalt in der konvertierten PDF zu steuern. Das bedeutet, dass Bildschirmleseprogramme den Text innerhalb der PDF-Datei zur Vorlesung der PDF-Datei nutzen können. Sie können dies deaktivieren, indem Sie ein Passwort für die Berechtigungsänderung anwenden und die beiden Elemente im Screenshot [hier](71630877.png) abwählen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Benutzerdefinierte Eigenschaften in PDF exportieren**

Mit der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) können Sie die benutzerdefinierten Eigenschaften im Quellarbeitsblatt in die PDF exportieren. Der [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)-Enumerator wird bereitgestellt, um die Art und Weise zu spezifizieren, wie die Eigenschaften exportiert werden. Diese Eigenschaften können in Adobe Acrobat Reader gesehen werden, indem auf Datei und dann Eigenschaften geklickt wird, wie im folgenden Bild gezeigt. Die Vorlagendatei "sourceWithCustProps.xlsx" kann zum Testen heruntergeladen werden [hier](sourceWithCustProps.xlsx) und die Ausgabe-PDF-Datei "outSourceWithCustProps" steht zur Analyse [hier](outSourceWithCustProps.pdf) zur Verfügung.

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Excel-Arbeitsmappe in Markdown konvertieren**

Die Aspose.Cells API unterstützt das Exportieren von Arbeitsmappen im Markdown-Format. Um das aktive Arbeitsblatt in Markdown zu exportieren, geben Sie [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) als zweiten Parameter der Methode [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) an. Sie können auch die Klasse [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in Markdown anzugeben.

Das folgende Codebeispiel demonstriert den Export des aktiven Arbeitsblatts in Markdown unter Verwendung des Enumerationsmitglieds [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). Bitte sehen Sie die durch den Code generierte [Ausgabedatei im Markdown-Format](Book1.txt) zur Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Erweiterte Themen**
- [Anpassen des Arbeitsmappe-Komprimierungsgrads](/cells/de/java/adjust-workbook-compression-level/)
- [Arbeitsmappe in verschiedene Formate konvertieren](/cells/de/java/converting-workbook-to-different-formats/)
- [Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern](/cells/de/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Konvertierungsvorgang von Excel nach TIFF verfolgen](/cells/de/java/track-conversion-progress-of-excel-to-tiff/)
- [Fortschritt der Dokumentkonvertierung nachverfolgen](/cells/de/java/track-document-conversion-progress/)
