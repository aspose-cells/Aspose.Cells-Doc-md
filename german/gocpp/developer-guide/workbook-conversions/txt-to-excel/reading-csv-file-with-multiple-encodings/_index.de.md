---
title: CSV Datei mit mehreren Kodierungen lesen mit Golang via C++
linktitle: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 200
url: /de/go-cpp/reading-csv-file-with-multiple-encodings/
description: Lerne, wie du CSV Dateien mit mehreren Kodierungen mit Aspose.Cells for C++ liest.
---

{{% alert color="primary" %}}

Manchmal enthält deine CSV-Datei mehrere Kodierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht das Laden solcher CSV-Dateien und die Konvertierung in andere Formate, zum Beispiel PDF oder XLSX.

{{% /alert %}}

Aspose.Cells bietet die [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)-Eigenschaft, die du auf **true** setzen musst, um deine CSV-Datei mit mehreren Kodierungen korrekt zu laden.

Das folgende Beispiel zeigt eine CSV-Datei mit zwei Zeilen. Die erste Zeile ist in **ANSI**-Kodierung und die zweite in **Unicode**-Kodierung.

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Das folgende Beispiel zeigt die XLSX-Datei, die aus der oben genannten CSV-Datei konvertiert wurde, ohne die [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)-Eigenschaft auf **true** zu setzen. Wie du sehen kannst, wurde der Unicode-Text nicht korrekt konvertiert.

|**Ausgabedatei 1: keine Berücksichtigung mehrerer Codierungen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Das folgende Beispiel zeigt die XLSX-Datei, die nach Setzen der [**TxtLoadOptions.IsMultiEncoded**](https://reference.aspose.com/cells/go-cpp/txtloadoptions/ismultiencoded/)-Eigenschaft auf **true** aus der oben genannten CSV-Datei konvertiert wurde. Wie du sehen kannst, wurde der Unicode-Text jetzt richtig konvertiert.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadingCsvFileWithMultipleEncodings.go" >}}
## Verwandte Artikel

- [Öffnen von CSV-Dateien](/cells/de/cpp/opening-files-with-different-formats/#opening-csv-files)
