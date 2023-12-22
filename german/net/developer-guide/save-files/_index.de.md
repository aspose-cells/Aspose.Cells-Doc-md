---
title: Verschiedene Möglichkeiten zum Speichern von Dateien
linktitle: Dateien speichern
type: docs
weight: 40
url: /de/net/different-ways-to-save-files/
description: Aspose.Cells for .NET kann Dateien in verschiedenen Formaten speichern. Speichern Sie Dateien unter PDF. Speichern Sie Dateien unter HTML. Speichern Sie Dateien unter DOCX. Speichern Sie Dateien unter PPTX. Speichern Sie Dateien unter JSON. Speichern Sie Dateien unter MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht das Erstellen und Speichern von Dateien. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien gespeichert werden können.

{{% /alert %}}

##  **Verschiedene Möglichkeiten zum Speichern von Dateien**

 Aspose.Cells bietet die**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Dies stellt eine Microsoft Excel-Datei dar und stellt die Eigenschaften und Methoden bereit, die für die Arbeit mit Excel-Dateien erforderlich sind. Der**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Klasse bietet die**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode zum Speichern von Excel-Dateien. Der**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Die Methode verfügt über viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weise verwendet werden.

 Das Dateiformat, in dem die Datei gespeichert wird, wird von bestimmt**[Speicherformat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Aufzählung

|**Dateiformattypen**|**Beschreibung**|
| :- | :- |
|CSV|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Stellt eine Excel 2007 XLSX-Datei dar|
|Xlsm|Stellt eine Excel 2007 XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007-Vorlagendatei XLTX dar|
|Xltm|Stellt eine Excel 2007-Makro-fähige XLTM-Datei dar|
|Xlsb|Stellt eine Excel 2007-Binärdatei XLSB dar|
|SpreadsheetML|Stellt eine Tabellenkalkulations-XML-Datei dar|
|TSV|Stellt eine tabulatorgetrennte Wertedatei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Stellt eine ODS-Datei dar|
|HTML|Stellt HTML Datei(en) dar|
|MHtml|Stellt eine MHTML-Datei(en) dar.|
|PDF|Stellt eine PDF-Datei dar|
|XPS|Stellt ein XPS-Dokument dar|
|TIFF|Stellt das getaggte Bilddateiformat dar (TIFF)|

##  **So speichern Sie Dateien in verschiedenen Formaten**

Um Dateien an einem Speicherort zu speichern, geben Sie den Dateinamen (komplett mit Speicherpfad) und das gewünschte Dateiformat (aus der Datei) an**[Speicherformat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** Aufzählung) beim Aufruf der**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Objekt**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **So speichern Sie eine Arbeitsmappe als PDF**
Portable Document Format (PDF) ist ein Dokumenttyp, der in den 1990er Jahren von Adobe entwickelt wurde. Der Zweck dieses Dateiformats bestand darin, einen Standard für die Darstellung von Dokumenten und anderem Referenzmaterial in einem Format einzuführen, das unabhängig von Anwendungssoftware, Hardware und Betriebssystem ist. Das Dateiformat PDF kann Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich Media, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die Teil des Quelldokuments werden können.

Die folgenden Codes zeigen, wie man eine Arbeitsmappe als PDF-Datei mit Aspose.Cells speichert:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **So speichern Sie eine Arbeitsmappe im Text- oder CSV-Format**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (zum Beispiel TXT, TabDelim, CSV usw.) speichern standardmäßig sowohl Microsoft Excel als auch Aspose.Cells nur den Inhalt des aktiven Arbeitsblatts.

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, bei der es sich um eine beliebige Excel- oder OpenOffice-Tabellendatei XLS (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern handeln kann.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das Format TXT.

 Sie können dasselbe Beispiel ändern, um Ihre Datei unter CSV zu speichern. Standardmäßig ist**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**ist ein Komma. Geben Sie daher beim Speichern im Format CSV kein Trennzeichen an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **So speichern Sie Dateien mit benutzerdefiniertem Trennzeichen in Textdateien**

Textdateien enthalten Tabellenkalkulationsdaten ohne Formatierung. Bei der Datei handelt es sich um eine Art reine Textdatei, deren Daten mit benutzerdefinierten Trennzeichen versehen werden können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **So speichern Sie eine Datei in einem Stream**

 Um Dateien in einem Stream zu speichern, erstellen Sie einen*MemoryStream* oder*Datenfluss*Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie das aufrufen**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Objekt**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode. Geben Sie das gewünschte Dateiformat mit an**[Speicherformat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** Aufzählung beim Aufruf der**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **So speichern Sie eine Excel-Datei in HTML- und MHT-Dateien**
Aspose.Cells kann einfach eine Excel-Datei, JSON, CSV oder andere Dateien speichern, die von Aspose.Cells als .html- und .mht-Dateien geladen werden könnten.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **So speichern Sie eine Excel-Datei in OpenOffice (ODS, SXC, FODS, OTS)**
Wir können die Dateien im Open-Office-Format speichern: ODS, SXC, FODS, OTS usw.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **So speichern Sie eine Excel-Datei im Format JSON oder XML**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat für die gemeinsame Nutzung von Daten, das menschenlesbaren Text zum Speichern und Übertragen von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative für XML. JSON ist von JavaScript abgeleitet, aber ein sprachunabhängiges Datenformat. Die Generierung und Analyse von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells unterstützt das Speichern von Dateien im Format JSON oder XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **Vorabthemen**
- [Passen Sie die Komprimierungsstufe der Arbeitsmappe an](/cells/de/net/adjust-workbook-compression-level/)
- [Speichern Sie die Arbeitsmappe im Strict Open XML-Tabellenformat](/cells/de/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Datei im Antwortobjekt speichern](/cells/de/net/saving-file-to-response-object/)
