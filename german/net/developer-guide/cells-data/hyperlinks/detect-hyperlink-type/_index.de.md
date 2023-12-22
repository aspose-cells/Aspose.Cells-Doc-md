---
title: Hyperlink-Typ erkennen
type: docs
weight: 160
url: /de/net/detect-hyperlink-type/
description: Erfahren Sie, wie Sie den Hyperlink-Typ mithilfe von Aspose.Cells for .NET API erkennen.
keywords: Detect hyperlink type, Detect the type of hyperlink, Get the type of hyperlink
---
##  **Hyperlink-Typ erkennen**

 Eine Excel-Datei kann verschiedene Arten von Hyperlinks enthalten, z. B. externe Links, Zellverweise, Dateipfade usw. Aspose.Cells unterstützt die Funktion zur Erkennung des Hyperlinktyps. Die Arten von Hyperlinks werden durch dargestellt[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Aufzählung. Der[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Die Aufzählung hat die folgenden Mitglieder.

- Extern: Externer Link
- FilePath: Lokaler und vollständiger Pfad zu Dateien/Ordnern.
- Email Email
- CellReference: Link zur Zelle oder zum benannten Bereich.

 Um die Art des Hyperlinks zu überprüfen, muss der[**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) Klasse bietet a[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) Eigenschaft mit einem Rückgabetyp von[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Der folgende Codeausschnitt demonstriert die Verwendung von[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)Eigentum, indem Sie dies nutzen[Quell-Excel-Datei](94896195.xlsx).

###  Quellcode

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Das Folgende ist die Ausgabe, die durch das oben angegebene Code-Snippet generiert wurde.

###  Konsolenausgabe
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
