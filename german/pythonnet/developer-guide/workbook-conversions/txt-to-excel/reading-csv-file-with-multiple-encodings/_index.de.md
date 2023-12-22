---
title: Lesen der Datei CSV mit mehreren Kodierungen
type: docs
weight: 200
url: /de/python-net/reading-csv-file-with-multiple-encodings/
description: Lesen der CSV-Datei mit mehreren Codierungen unter Verwendung von Aspose.Cells for Python via .NET API.
keywords: Python Reading CSV File with Multiple Encodings, Convert CSV File with Multiple Encodings to Excel in Python via NET, Python convert CSV File with Multiple Encodings to xlsx, Load CSV File with Multiple Encodings to Excel file.
---
{{% alert color="primary" %}}

Manchmal enthält Ihre CSV-Datei mehrere Kodierungen (Unicode, ANSI, UTF8, UTF7 usw.). Mit Aspose.Cells können Sie solche CSV-Dateien laden und in andere Formate konvertieren, zum Beispiel PDF oder XLSX.

{{% /alert %}}

 Aspose.Cells bietet die[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/) Eigenschaft, die Sie festlegen müssen**WAHR** um Ihre CSV-Datei mit mehreren Kodierungen ordnungsgemäß zu laden.

 Der folgende Screenshot zeigt eine Beispieldatei CSV, die zwei Zeilen enthält. Die erste Zeile ist drin**ANSI** Kodierung und die zweite Zeile ist in**Unicode** Codierung

|**Eingabedatei**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Der folgende Screenshot zeigt die Datei XLSX, die aus der obigen Datei CSV konvertiert wurde, ohne dass die festgelegt wurde[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)Eigenschaft auf *true**. Wie Sie sehen, wurde der Unicode-Text nicht richtig konvertiert.

|**Ausgabedatei 1: Es wurden keine Vorkehrungen für Mehrfachkodierung getroffen**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

 Der folgende Screenshot zeigt die aus der oben genannten CSV-Datei konvertierte XSLX-Datei nach dem Festlegen von[**TxtLoadOptions.is_multi_encoded**](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/is_multi_encoded/)Eigenschaft auf *true**. Wie Sie sehen, wird der Unicode-Text jetzt ordnungsgemäß konvertiert.

|**Ausgabedatei 2: IsMultiEncoded ist auf true gesetzt**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Unten finden Sie den Beispielcode, der die obige Datei CSV ordnungsgemäß in das Format XLSX konvertiert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ReadingCSVMultipleEncodings-1.py" >}}
