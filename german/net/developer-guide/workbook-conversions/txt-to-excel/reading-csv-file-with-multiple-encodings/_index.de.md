---
title: Lesen von CSV-Datei mit mehreren Codierungen
type: docs
weight: 200
url: /de/net/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Mit Aspose.Cells können Sie solche CSV-Dateien laden und in andere Formate konvertieren, z. B. PDF oder XLSX.

{{% /alert %}}

 Aspose.Cells bietet die[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) Eigenschaft, die Sie festlegen müssen**wahr** um Ihre CSV-Datei mit mehreren Kodierungen richtig zu laden.

 Der folgende Screenshot zeigt eine Beispieldatei CSV, die zwei Zeilen enthält. Die erste Zeile ist drin**ANSI** Codierung und die zweite Zeile ist in**Unicode** Codierung

|**Eingabedatei**|
|:- |
|![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_1.png)|

 Der folgende Screenshot zeigt die XLSX-Datei, die aus der obigen CSV-Datei konvertiert wurde, ohne die[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) Eigentum zu**wahr**. Wie Sie sehen können, wurde der Unicode-Text nicht richtig konvertiert.

|**Ausgabedatei 1: keine Anpassung an Mehrfachcodierung vorgenommen**|
|:- |
|![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_2.png)|

 Der folgende Screenshot zeigt die XSLX-Datei, die aus der obigen CSV-Datei konvertiert wurde, nachdem die[**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded) Eigentum zu**wahr**. Wie Sie sehen können, wird der Unicode-Text jetzt korrekt konvertiert.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
|:- |
|![todo: Bild_alt_Text](reading-csv-file-with-multiple-encodings_3.png)|

Unten ist der Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Zum Thema passende Artikel

- [Öffnen von CSV-Dateien](/cells/de/net/opening-files-with-different-formats/#opening-csv-files)
