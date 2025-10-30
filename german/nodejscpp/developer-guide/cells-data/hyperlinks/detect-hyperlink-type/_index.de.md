---
title: Hyperlink Typ erkennen
type: docs
weight: 160
url: /de/nodejs-cpp/detect-hyperlink-type/
description: Erfahren Sie, wie man den Hyperlink Typ durch die Aspose.Cells for Node.js via C++ API erkennt.
keywords: Hyperlink Typ erkennen Node.js via C++, Hyperlink Typ Node.js via C++ erkennen, den Typ des Hyperlinks Node.js via C++ abrufen
---

## **Hyperlink-Typ erkennen**

Eine Excel-Datei kann verschiedene Arten von Hyperlinks enthalten, wie externe, Zellverweis, Dateipfad usw. Aspose.Cells for Node.js via C++ unterstützt die Funktion, den Hyperlink-Typ zu erkennen. Die Arten von Hyperlinks sind durch die [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeration dargestellt. Die [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeration hat die folgenden Mitglieder.

- External: Externer Link
- FilePath: Lokale und vollständige Pfade zu Dateien/Ordnern.
- Email: E-Mail
- CellReference: Verweis auf Zelle oder benannten Bereich.

Um den Typ des Hyperlinks zu überprüfen, bietet die [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) Klasse eine [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) Methode mit einem Rückgabewert vom Typ [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Das folgende Codesnippet demonstriert die Verwendung der [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) Methode anhand dieser [Excel-Quelldatei](94896195.xlsx).

### Quellcode

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
{{< app/cells/assistant language="nodejs-cpp" >}}
