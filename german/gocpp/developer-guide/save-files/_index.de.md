---
title: Verschiedene Möglichkeiten, Dateien mit Golang über C++ zu speichern
linktitle: Dateien speichern
type: docs
weight: 40
url: /de/go-cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ kann Dateien in verschiedene Formate speichern. Dateien im PDF Format speichern. Dateien im HTML Format speichern. Dateien im DOCX Format speichern. Dateien im PPTX Format speichern. Dateien im JSON Format speichern. Dateien im MHTML Format speichern.
keywords: Aspose.Cells speichert Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML und weitere Formate mit C++, speichert oder konvertiert Arbeitsmappen nach PDF, HTML, JSON, TXT, SQL in C++.
---

{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, Dateien zu erstellen und zu speichern. Dieser Artikel erklärt die verschiedenen Möglichkeiten, wie Dateien gespeichert werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten, Dateien zu speichern**

Aspose.Cells bietet die Klasse [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Microsoft Excel-Datei darstellt und die für die Arbeit mit Excel-Dateien notwendigen Eigenschaften und Methoden bereitstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) bietet die [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)-Methode, die zum Speichern von Excel-Dateien verwendet wird. Die Methode [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) hat viele Überladungen, die verwendet werden, um Dateien auf verschiedene Weisen zu speichern.

Das Dateiformat, in das die Datei gespeichert wird, wird durch die Enumeration [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) entschieden.

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

Um Dateien an einen Speicherort zu speichern, geben Sie beim Aufrufen der Methode [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) des Objekts [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) den Dateinamen (vollständig mit Speicherpfad) und das gewünschte Dateiformat (aus der Enumeration [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)) an.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles.go" >}}
## **Wie man eine Arbeitsmappe als PDF speichert**
Portable Document Format (PDF) ist ein Dokumententyp, der von Adobe in den 1990er Jahren erstellt wurde. Der Zweck dieses Dateiformats war es, einen Standard für die Darstellung von Dokumenten und anderen Referenzmaterialien in einem Format einzuführen, das unabhängig von Anwendungssoftware, Hardware sowie Betriebssystem ist. Das PDF-Dateiformat kann vollständige Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich-Media-Inhalte, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die als Teil des Quelldokuments fungieren können.

Der folgende Code zeigt, wie man eine Arbeitsmappe mit Aspose.Cells als PDF-Datei speichert:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-1.go" >}}
## **Wie man eine Arbeitsmappe im Text- oder CSV-Format speichert**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in Textformat konvertieren oder speichern. Für Textformate (zum Beispiel TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Beim Ausführen des Codes werden die Daten aller Blätter in der Arbeitsmappe in das TXT-Format konvertiert

Sie können das gleiche Beispiel anpassen, um Ihre Datei als CSV zu speichern. Standardmäßig ist [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) das Komma, also geben Sie keinen Trennzeichen an, wenn Sie im CSV-Format speichern. Bitte beachten Sie: Wenn Sie die Evaluierungsversion verwenden und selbst wenn die Eigenschaft [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) auf true gesetzt ist, exportiert das Programm weiterhin nur ein Arbeitsblatt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-2.go" >}}
## **Wie man eine Datei in Textdateien mit benutzerdefiniertem Trennzeichen speichert**

Textdateien enthalten Tabellendaten ohne Formatierung

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-3.go" >}}
## **Wie man eine Datei in einen Stream speichert**

Um Dateien in einen Stream zu speichern, erstellen Sie ein *MemoryStream* oder *FileStream*-Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie die [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)-Methode des Objekts [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) aufrufen. Geben Sie das gewünschte Dateiformat mithilfe der Enumeration [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) an, wenn Sie die [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)-Methode aufrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-4.go" >}}
## **Wie man eine Excel-Datei in Html- und Mht-Dateien speichert**
Aspose.Cells kann eine Excel-, JSON-, CSV- oder andere Dateien einfach als .html- und .mht-Dateien speichern.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-5.go" >}} 

## **Wie man eine Excel-Datei in das OpenOffice-Format (ODS, SXC, FODS, OTS) speichert**
Wir können die Dateien als OpenOffice-Format speichern: ODS, SXC, FODS, OTS usw.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-6.go" >}}
## **Wie man eine Excel-Datei in JSON- oder XML-Dateien speichert**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat zum Austausch von Daten, das menschenlesbaren Text zur Speicherung und Übertragung von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative für XML. JSON leitet sich von JavaScript ab, ist jedoch ein sprachunabhängiges Datenformat. Die Generierung und Analyse von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells unterstützt das Speichern von Dateien als JSON oder XML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveFiles-7.go" >}}

## **Erweiterte Themen**
- [Anpassen des Arbeitsmappe-Komprimierungsgrads](/cells/de/cpp/adjust-workbook-compression-level/)
- [Arbeitsmappe im Strict Open XML-Tabellenkalkulationsformat speichern](/cells/de/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Speichern der Datei im Antwortobjekt](/cells/de/cpp/saving-file-to-response-object/)
