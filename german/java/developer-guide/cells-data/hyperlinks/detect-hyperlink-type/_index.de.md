---
title: Hyperlinktyp erkennen
type: docs
weight: 180
url: /de/java/detect-hyperlink-type/
---
## **Hyperlinktyp erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks enthalten, z. B. externe Links, Zellreferenzen, Dateipfade usw. Aspose.Cells unterstützt die Funktion zur Erkennung des Hyperlinktyps. Die Arten von Hyperlinks werden durch dargestellt[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Aufzählung. Das[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Die Aufzählung hat die folgenden Mitglieder.

- [**EXTERN**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Externer Link
- [**DATEIPFAD**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Lokaler und vollständiger Pfad zu Dateien\Ordnern.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): Email
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Link zu Zelle oder benanntem Bereich.

Um die Art des Hyperlinks zu überprüfen, muss die[**Hyperlinks**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) Klasse bietet a[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) Eigenschaft mit einem Rückgabetyp von[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Das folgende Code-Snippet demonstriert die Verwendung von[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)Eigenschaft, indem Sie diese verwenden[Excel-Quelldatei](LinkTypes.xlsx).

## Quellcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Das Folgende ist die Ausgabe, die durch das oben angegebene Code-Snippet generiert wird.

## Konsolenausgabe
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
