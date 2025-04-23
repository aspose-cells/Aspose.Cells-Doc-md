---
title: Hyperlink Typ erkennen
type: docs
weight: 180
url: /de/java/detect-hyperlink-type/
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks wie externe, Zellbezug, Dateipfad usw. haben. Aspose.Cells unterstützt die Funktion, den Typ des Hyperlinks zu erkennen. Die Arten von Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)-Enumeration repräsentiert. Die [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)-Enumeration hat die folgenden Elemente.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Externer Link
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE-PATH): Lokaler und voller Pfad zu Dateien/Ordnern.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-Mail
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL-REFERENCE) : Link zur Zelle oder benanntem Bereich.

Um den Typ des Hyperlinks zu überprüfen, bietet die [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)-Klasse eine [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)-Eigenschaft mit einem Rückgabetyp von [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Der folgende Codeausschnitt veranschaulicht die Verwendung der [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)-Eigenschaft unter Verwendung dieser [Excel-Quelldatei](LinkTypes.xlsx).

## Quellcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.

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
{{< app/cells/assistant language="java" >}}
