---
title: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 200
url: /de/net/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es Ihnen, solche CSV-Dateien zu laden und in andere Formate, z. B. PDF oder XLSX, zu konvertieren.

{{% /alert %}}

Aspose.Cells bietet die Eigenschaft [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded), die Sie auf **true** setzen müssen, um Ihre CSV-Datei mit mehreren Codierungen ordnungsgemäß zu laden.

Der folgende Screenshot zeigt eine Beispiel-CSV-Datei, die zwei Zeilen enthält. Die erste Zeile ist in **ANSI**-Codierung und die zweite Zeile ist in **Unicode**-Codierung

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Der folgende Screenshot zeigt die aus der obigen CSV-Datei konvertierte XLSX-Datei, ohne die [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)-Eigenschaft auf **true** zu setzen. Wie Sie sehen können, wurde der Unicode-Text nicht ordnungsgemäß konvertiert.

|**Ausgabedatei 1: keine Berücksichtigung mehrerer Codierungen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Der folgende Screenshot zeigt die aus der obigen CSV-Datei konvertierte XSLX-Datei, nachdem die [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/ismultiencoded)-Eigenschaft auf **true** gesetzt wurde. Wie Sie sehen können, ist der Unicode-Text jetzt korrekt konvertiert.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCSVMultipleEncodings-1.cs" >}}

## Verwandte Artikel

- [Öffnen von CSV-Dateien](/cells/de/net/opening-files-with-different-formats/#opening-csv-files)
{{< app/cells/assistant language="csharp" >}}
