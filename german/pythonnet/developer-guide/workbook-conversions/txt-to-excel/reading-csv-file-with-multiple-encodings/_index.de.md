---
title: CSV Datei mit mehreren Codierungen lesen
type: docs
weight: 200
url: /de/python-net/reading-csv-file-with-multiple-encodings/
description: Lesen von CSV Datei mit mehreren Encodings mithilfe der Aspose.Cells für Python via .NET API.
keywords: Python Lesen von CSV Datei mit mehreren Encodings, Konvertieren von CSV Datei mit mehreren Encodings in Excel in Python via NET, Python konvertieren CSV Datei mit mehreren Encodings in xlsx, Laden von CSV Datei mit mehreren Encodings in Excel Datei.
---

{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Codierungen (Unicode, ANSI, UTF8, UTF7 usw.). Aspose.Cells ermöglicht es Ihnen, solche CSV-Dateien zu laden und in andere Formate, z. B. PDF oder XLSX, zu konvertieren.

{{% /alert %}}

Aspose.Cells bietet die Eigenschaft [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/), die Sie auf **true** setzen müssen, um Ihre CSV-Datei mit mehreren Codierungen ordnungsgemäß zu laden.

Der folgende Screenshot zeigt eine Beispiel-CSV-Datei, die zwei Zeilen enthält. Die erste Zeile ist in **ANSI**-Codierung und die zweite Zeile ist in **Unicode**-Codierung

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Der folgende Screenshot zeigt die aus der obigen CSV-Datei konvertierte XLSX-Datei, ohne die [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)-Eigenschaft auf **true** zu setzen. Wie Sie sehen können, wurde der Unicode-Text nicht ordnungsgemäß konvertiert.

|**Ausgabedatei 1: keine Berücksichtigung mehrerer Codierungen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Der folgende Screenshot zeigt die aus der obigen CSV-Datei konvertierte XSLX-Datei, nachdem die [**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)-Eigenschaft auf **true** gesetzt wurde. Wie Sie sehen können, ist der Unicode-Text jetzt korrekt konvertiert.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Im Folgenden finden Sie den Beispielcode, der die obige CSV-Datei ordnungsgemäß in das XLSX-Format konvertiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
