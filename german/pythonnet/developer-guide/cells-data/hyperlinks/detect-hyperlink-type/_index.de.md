---
title: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/python-net/detect-hyperlink-type/
description: Erfahren Sie, wie Sie den Hyperlink Typ mithilfe der Aspose.Cells for Python via .NET API erkennen.
keywords: Python Excel Bibliothek, Hyperlink Typ in Python erkennen, Typ des Hyperlinks in Python erkennen, Typ des Hyperlinks abrufen.
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks wie externe, Zell- oder Dateipfadhyperlinks enthalten. Aspose.Cells for Python via .NET unterstützt die Funktion, den Typ des Hyperlinks zu erkennen. Die Arten von Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)-Enumeration dargestellt. Die [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)-Enumeration hat folgende Elemente.

- EXTERN: Externen Link
- DATEI_PFAD: Lokaler und vollständiger Pfad zu Dateien/Ordnern.
- E-MAIL: E-Mail
- ZELL_VERWEIS: Verweis auf Zelle oder benannten Bereich.

Um den Hyperlink-Typ zu überprüfen, enthält die {0}-Klasse eine Eigenschaft {1} mit einem Rückgabetyp von {2}. Der folgende Codeausschnitt veranschaulicht die Verwendung der Eigenschaft {3} anhand dieser {source excel file} (94896195.xlsx).

### Quellcode

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.

### Konsolenausgabe
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
