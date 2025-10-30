---
title: Verschiedene Möglichkeiten, Dateien zu speichern
linktitle: Dateien speichern
type: docs
weight: 40
url: /de/python-net/different-ways-to-save-files/
description: Aspose.Cells für Python via .NET kann Dateien in verschiedene Formate speichern. Dateien als PDF speichern. Dateien als HTML speichern. Dateien als DOCX speichern. Dateien als PPTX speichern. Dateien als JSON speichern. Dateien als MHTML speichern.
keywords: Aspose.Cells für Python via .NET speichert Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML und anderen Formaten mit C#, speichert oder konvertiert Arbeitsmappen in PDF, HTML, JSON, TXT, SQL in C#.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET ermöglicht das Erstellen und Speichern von Dateien. Dieser Artikel erklärt die verschiedenen Möglichkeiten, Dateien zu speichern.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Dateien zu speichern**

Aspose.Cells für Python via .NET bietet die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert und die Eigenschaften und Methoden bereitstellt, um mit Excel-Dateien zu arbeiten. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) Klasse stellt die [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)-Methode bereit, die zum Speichern von Excel-Dateien verwendet wird. Die [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)-Methode hat viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weisen genutzt werden.

Das Dateiformat, in das die Datei gespeichert wird, wird durch die Enumeration [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) entschieden.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|CSV|Repräsentiert eine CSV-Datei|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Repräsentiert eine Excel 2007 XLSX Datei|
|Xlsm|Repräsentiert eine Excel 2007 XLSM Datei|
|Xltx|Repräsentiert eine Excel 2007 Vorlagen XLTX Datei|
|Xltm|Repräsentiert eine Excel 2007 makrofähige XLTM Datei|
|Xlsb|Repräsentiert eine Excel 2007 binäre XLSB Datei|
|SpreadsheetML|Repräsentiert eine Tabellenkalkulation XML-Datei|
|TSV|Repräsentiert eine durch Tabulatoren getrennte Werte-Datei|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Repräsentiert eine ODS-Datei|
|Html|Repräsentiert HTM L-Datei(en)|
|MHtml|Repräsentiert eine MHTML Datei(en)|
|Pdf|Repräsentiert eine PDF-Datei|
|XPS|Repräsentiert ein XPS-Dokument|
|TIFF|Repräsentiert das Dateiformat für markierte Bilddatei (TIFF)|

## **Wie man Datei in verschiedenen Formaten speichert**

Um Dateien an einen Speicherort zu speichern, geben Sie beim Aufrufen der Methode [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) des Objekts [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) den Dateinamen (vollständig mit Speicherpfad) und das gewünschte Dateiformat (aus der Enumeration [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat)) an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SavingFiletoSomeLocation-1.py" >}}

## **Wie man eine Arbeitsmappe als PDF speichert**
Portable Document Format (PDF) ist ein Dokumententyp, der von Adobe in den 1990er Jahren erstellt wurde. Der Zweck dieses Dateiformats war es, einen Standard für die Darstellung von Dokumenten und anderen Referenzmaterialien in einem Format einzuführen, das unabhängig von Anwendungssoftware, Hardware sowie Betriebssystem ist. Das PDF-Dateiformat kann vollständige Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich-Media-Inhalte, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die als Teil des Quelldokuments fungieren können.

Der folgende Code zeigt, wie man eine Arbeitsmappe als PDF-Datei mit Aspose.Cells für Python via .NET speichert:
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Save-As-Pdf.py" >}}

## **Wie man eine Arbeitsmappe im Text- oder CSV-Format speichert**

Manchmal möchten Sie ein Arbeitsblatt mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells für Python via .NET standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator) das Komma, also geben Sie keinen Trennzeichen an, wenn Sie im CSV-Format speichern. Bitte beachten Sie: Wenn Sie die Evaluierungsversion verwenden und selbst wenn die Eigenschaft [**TxtSaveOptions.export_all_sheets**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/export_all_sheets/) auf true gesetzt ist, exportiert das Programm weiterhin nur ein Arbeitsblatt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Wie man eine Datei in Textdateien mit benutzerdefiniertem Trennzeichen speichert**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-OpeningTextFilewithCustomSeparator-1.py" >}}


## **Wie man eine Excel-Datei in Html- und Mht-Dateien speichert**
Aspose.Cells für Python via .NET kann eine Excel-Datei, JSON, CSV oder andere Dateien einfach speichern, die von Aspose.Cells für Python via .NET als .html- und .mht-Dateien geladen werden können.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-MHTML.py" >}}


## **Wie man eine Excel-Datei in das OpenOffice-Format (ODS, SXC, FODS, OTS) speichert**
Wir können die Dateien als OpenOffice-Format speichern: ODS, SXC, FODS, OTS usw.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-ODS.py" >}}

## **Wie man eine Excel-Datei in JSON- oder XML-Dateien speichert**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat zum Austausch von Daten, das menschenlesbaren Text zur Speicherung und Übertragung von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative für XML. JSON leitet sich von JavaScript ab, ist jedoch ein sprachunabhängiges Datenformat. Die Generierung und Analyse von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells für Python via .NET unterstützt das Speichern von Dateien in JSON oder XML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-Convert-Excel-to-JSON.py" >}}


## **Erweiterte Themen**
- [Anpassen des Arbeitsmappe-Komprimierungsgrads](/cells/de/python-net/adjust-workbook-compression-level/)
- [Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern](/cells/de/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/)

{{< app/cells/assistant language="python-net" >}}
