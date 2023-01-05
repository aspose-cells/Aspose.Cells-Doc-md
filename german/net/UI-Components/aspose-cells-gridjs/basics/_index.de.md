---
title: Aspose.Cells.GridJs-Grundlagen
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/basics/
---
## Grundlagen von GridJs

 Aspose.Cells.GridJs ist eine .NET-Standardbibliothek, mit der Benutzer Webanwendungen entwickeln können, um Tabellenkalkulationen schnell und einfach anzuzeigen/zu bearbeiten.

Aspose.Cells.GridJs unterstützt den Import der gängigen Tabellenformate (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Es ermöglicht auch den Export von Excel-Dateien nach PDF, HTML usw. Nachfolgend finden Sie die grundlegenden Prozessschritte zum Entwickeln einer Webanwendung von GridJs.

- Implementieren Sie GridCacheForStream, um Ihre eigene Geschäftslogik für die Cache-Speicherung zu schreiben.
- Richten Sie eine Controller-Aktion ein, um JSON aus der Tabellenkalkulationsdatei abzurufen. Sie können die GridJsWorkbook.ImportExcelFile- und GridJsWorkbook.ExportToJson-APIs verwenden, GridJs speichert die Spread-Datei automatisch im Cache.
- Richten Sie eine Controller-Aktion ein, um JSON für den Aktualisierungsvorgang abzurufen. Sie können GridJsWorkbook.UpdateCell API verwenden. GridJs führt den Aktualisierungsvorgang im Cache durch und gibt den aktualisierten JSON zurück.
- Richten Sie eine Controller-Aktion ein, um die Bild-/Formdatei-URL in der Tabelle abzurufen. GridJs komprimiert automatisch alle Bilder/Formen im Cache. Es verwendet GridCacheForStream.GetFileUrl API.
- Richten Sie eine Controller-Aktion ein, um die Datei im Cache abzurufen, damit wir die ZIP-Datei mit Bildern/Formen oder die Tabellenkalkulationsdatei im Cache abrufen können. Sie verwendet GridCacheForStream.LoadStream API.
- Richten Sie eine Controller-Aktion ein, um die Tabelle herunterzuladen. Sie können GridJsWorkbook.SaveToCacheWithFileName API verwenden.

 Nachfolgend finden Sie eine einfache Demo, um die Verwendung von Aspose.Cells.GridJs zu zeigen: https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs

Wenn Sie Fragen, Anforderungen oder Hilfe benötigen, geben Sie bitte Feedback auf der folgenden Website https://forum.aspose.com/c/cells/9