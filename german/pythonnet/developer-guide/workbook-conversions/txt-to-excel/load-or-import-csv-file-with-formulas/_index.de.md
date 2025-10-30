---
title: Laden oder Importieren von CSV Dateien mit Formeln
type: docs
weight: 350
url: /de/python-net/load-or-import-csv-file-with-formulas/
description: Laden oder Importieren von CSV Dateien mit Formeln unter Verwendung der Aspose.Cells für Python via .NET API.
keywords: Python Laden oder Importieren von CSV Dateien mit Formeln, Konvertieren von CSV mit Formeln in Excel in Python via NET, Python Konvertieren von CSV mit Formeln in xlsx, Laden von CSV mit Formeln in Excel Datei.
---

{{% alert color="primary" %}} 

CSV-Datei enthält hauptsächlich textuelle Daten und keine Formeln. Manchmal kommt es jedoch vor, dass CSV-Dateien auch Formeln enthalten. Solche CSV-Dateien sollten geladen werden, indem die [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) auf **true** festgelegt wird. Sobald diese Eigenschaft auf **true** festgelegt ist, wird Aspose.Cells die Formel nicht als einfachen Text behandeln. Sie werden als Formel behandelt und der Formelberechnungsmotor von Aspose.Cells wird sie wie gewohnt verarbeiten.

{{% /alert %}} 

Der folgende Code zeigt, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zu Veranschaulichungszwecken verwenden wir die [einfache CSV-Datei](5115034.csv), die diese Daten enthält. Wie Sie sehen, enthält sie eine Formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



Der Code lädt zunächst die CSV-Datei, importiert sie dann erneut in die Zelle D4. Schließlich speichert er das Arbeitsmap-Objekt im XSLX-Format. Die [Ausgabe-XLSX-Datei](5115052.xlsx) sieht so aus. Wie Sie sehen, enthalten die Zelle C3 und F4 eine Formel und ihr Ergebnis 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
