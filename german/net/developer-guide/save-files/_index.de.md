---
title: Verschiedene Möglichkeiten zum Speichern von Dateien
linktitle: Daten abspeichern
type: docs
weight: 40
url: /de/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht das Erstellen und Speichern von Dateien. In diesem Artikel werden die verschiedenen Möglichkeiten erläutert, wie Dateien gespeichert werden können.

{{% /alert %}}

## **Verschiedene Möglichkeiten zum Speichern von Dateien**

 Aspose.Cells bietet die**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** die eine Microsoft Excel-Datei darstellt und die Eigenschaften und Methoden bereitstellt, die zum Arbeiten mit Excel-Dateien erforderlich sind. Das**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse bietet die**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode zum Speichern von Excel-Dateien. Das**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**-Methode verfügt über viele Überladungen, die zum Speichern von Dateien auf unterschiedliche Weise verwendet werden.

 Das Dateiformat, in dem die Datei gespeichert wird, wird von festgelegt**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**Aufzählung

|**Dateiformattypen**|**Beschreibung**|
|:- |:- |
|CSV|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97-2003-Datei dar|
|XLSX|Stellt eine Excel 2007 XLSX-Datei dar|
|XLSM|Stellt eine Excel 2007 XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007-Vorlagen-XLTX-Datei dar|
|Xltm|Stellt eine XLTM-Datei mit Excel 2007-Makros dar|
|XLSB|Stellt eine binäre Excel 2007-XLSB-Datei dar|
|SpreadsheetML|Stellt eine Tabellenkalkulations-XML-Datei dar|
|TSV|Stellt eine tabulatorgetrennte Wertedatei dar|
|Tabulatorgetrennt|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Stellt eine ODS-Datei dar|
|HTML|Repräsentiert HTML-Datei(en)|
|HTML|Stellt eine MHTML-Datei(en) dar|
|Pdf|Stellt eine PDF-Datei dar|
|XPS|Stellt ein XPS-Dokument dar|
|TIFF|Repräsentiert das Tagged Image File Format (TIFF)|

## **Speichern von Dateien in verschiedenen Formaten**

 Um Dateien an einem Speicherort zu speichern, geben Sie den Dateinamen (komplett mit Speicherpfad) und das gewünschte Dateiformat (aus der**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** Aufzählung) beim Aufrufen der**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Objekt**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Arbeitsmappe als pdf speichern**
Portable Document Format (PDF) ist ein Dokumenttyp, der von Adobe in den 1990er Jahren erstellt wurde. Der Zweck dieses Dateiformats bestand darin, einen Standard für die Darstellung von Dokumenten und anderem Referenzmaterial in einem Format einzuführen, das unabhängig von Anwendungssoftware, Hardware und Betriebssystem ist. Das PDF-Dateiformat kann Informationen wie Text, Bilder, Hyperlinks, Formularfelder, Rich Media, digitale Signaturen, Anhänge, Metadaten, Geodaten und 3D-Objekte enthalten, die Teil des Quelldokuments werden können.

Der folgende Code zeigt, wie man die Arbeitsmappe als PDF-Datei mit Aspose.Cells speichert:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Arbeitsmappe im Text- oder CSV-Format speichern**

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, bei der es sich um eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern handeln kann.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das TXT-Format.

 Sie können dasselbe Beispiel ändern, um Ihre Datei im CSV-Format zu speichern. Standardmäßig,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**ist ein Komma, also geben Sie beim Speichern im CSV-Format kein Trennzeichen an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Speichern von Textdateien mit benutzerdefiniertem Trennzeichen**

Textdateien enthalten Tabellenkalkulationsdaten ohne Formatierung. Die Datei ist eine Art einfache Textdatei, die einige benutzerdefinierte Trennzeichen zwischen ihren Daten haben kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Datei in einem Stream speichern**

 Um Dateien in einem Stream zu speichern, erstellen Sie eine*MemoryStream* oder*Datenfluss* Objekt und speichern Sie die Datei in diesem Stream-Objekt, indem Sie die aufrufen**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Objekt**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** Methode. Geben Sie das gewünschte Dateiformat mit an**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** Aufzählung beim Aufruf der**[Speichern](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Speichern von Dateien als Html- und Mht-Dateien**
Aspose.Cells kann einfach eine Excel-Datei, JSON, CSV oder andere Dateien speichern, die von Aspose.Cells als .html- und .mht-Dateien geladen werden können.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Speichern als OpenOffice (ODS, SXC, FODS, OTS)**
Wir können die Dateien im offenen Office-Format speichern: ODS, SXC, FODS, OTS usw.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Excel-Datei als JSON oder XML speichern**

JSON (JavaScript Object Notation) ist ein offenes Standarddateiformat zum Teilen von Daten, das menschenlesbaren Text zum Speichern und Übertragen von Daten verwendet. JSON-Dateien werden mit der Erweiterung .json gespeichert. JSON erfordert weniger Formatierung und ist eine gute Alternative zu XML. JSON ist von JavaScript abgeleitet, aber ein sprachunabhängiges Datenformat. Das Generieren und Parsen von JSON wird von vielen modernen Programmiersprachen unterstützt. application/json ist der Medientyp, der für JSON verwendet wird.

Aspose.Cells unterstützt das Speichern von Dateien in JSON oder XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Themen vorantreiben**
- [Passen Sie die Komprimierungsstufe der Arbeitsmappe an](/cells/de/net/adjust-workbook-compression-level/)
- [Speichern Sie die Arbeitsmappe im strikt offenen XML-Tabellenformat](/cells/de/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Datei im Antwortobjekt speichern](/cells/de/net/saving-file-to-response-object/)
