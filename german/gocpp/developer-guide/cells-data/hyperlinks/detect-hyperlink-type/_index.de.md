---
title: Hyperlink Typ mit Golang via C++ erkennen
linktitle: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/go-cpp/detect-hyperlink-type/
description: Lernen Sie, wie man den Hyperlink Typ durch die API Aspose.Cells for C++ erkennt.
keywords: Hyperlink Typ erkennen, Den Typ des Hyperlinks erkennen, Den Typ des Hyperlinks erhalten
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks wie externe Links, Zellverweise, Dateipfade usw. enthalten. Aspose.Cells unterstützt die Funktion, den Typ des Hyperlinks zu erkennen. Die Arten von Hyperlinks werden durch die [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)-Aufzählung repräsentiert. Die [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)-Aufzählung enthält die folgenden Elemente.

- Extern: Externer Link
- Dateipfad: Lokaler und vollständiger Pfad zu Dateien/Ordnern.
- E-Mail: E-Mail
- Zellverweis: Verknüpfung zu Zelle oder benanntem Bereich.

Um den Hyperlink-Typ zu überprüfen, enthält die {0}-Klasse eine Eigenschaft {1} mit einem Rückgabetyp von {2}. Der folgende Codeausschnitt veranschaulicht die Verwendung der Eigenschaft {3} anhand dieser {source excel file} (94896195.xlsx).

### Quellcode

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Das folgende ist die Ausgabe, die durch den obigen Codeausschnitt generiert wird.

### Konsolenausgabe
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
