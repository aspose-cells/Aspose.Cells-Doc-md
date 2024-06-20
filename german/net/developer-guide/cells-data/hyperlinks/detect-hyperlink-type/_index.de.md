---
title: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/net/detect-hyperlink-type/
description: Erfahren Sie, wie man den Hyperlink Typ über die Aspose.Cells for .NET API erkennt.
keywords: Hyperlink Typ erkennen, Den Typ des Hyperlinks erkennen, Den Typ des Hyperlinks erhalten
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks wie externe Links, Zellverweise, Dateipfade usw. enthalten. Aspose.Cells unterstützt die Funktion, den Typ des Hyperlinks zu erkennen. Die Arten von Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)-Aufzählung repräsentiert. Die [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)-Aufzählung enthält die folgenden Elemente.

- Extern: Externer Link
- Dateipfad: Lokaler und vollständiger Pfad zu Dateien/Ordnern.
- E-Mail: E-Mail
- Zellverweis: Verknüpfung zu Zelle oder benanntem Bereich.

Um den Hyperlink-Typ zu überprüfen, enthält die {0}-Klasse eine Eigenschaft {1} mit einem Rückgabetyp von {2}. Der folgende Codeausschnitt veranschaulicht die Verwendung der Eigenschaft {3} anhand dieser {source excel file} (94896195.xlsx).

### Quellcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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
