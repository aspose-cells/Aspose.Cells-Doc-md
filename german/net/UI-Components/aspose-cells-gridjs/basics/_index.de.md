---
title: Aspose.Cells.GridJs Grundlagen
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/basics/
keywords: GridJs
description: Dieser Artikel stellt die grundlegenden Schritte zur Einrichtung einer Webanwendung für GridJs vor.
---

## Grundlagen von GridJs

Aspose.Cells.GridJs ist eine .NET-Standardbibliothek, mit der Benutzer eine Webanwendung entwickeln können, um Tabellenkalkulationen schnell und einfach anzuzeigen/bearbeiten. 

Aspose.Cells.GridJs unterstützt den Import der gängigen Tabellenkalkulationsdateiformate (XLS, XLSX, XLSM, XLSB, CSV, SpreadsheetML, ODS).

Es ermöglicht auch das Exportieren von Excel-Dateien in PDF, HTML usw. Unten finden Sie die grundlegenden Schritte zur Entwicklung einer Webanwendung für GridJs.

- Implementieren Sie GridCacheForStream, um Ihre eigene Geschäftslogik für den Zwischenspeicher zu schreiben.
- Richten Sie eine Controller-Aktion ein, um JSON aus der Tabellenkalkulationsdatei zu erhalten. Sie können die APIs GridJsWorkbook.ImportExcelFile und GridJsWorkbook.ExportToJson verwenden, GridJs speichert die Tabellendatei automatisch im Cache.
- Richten Sie eine Controller-Aktion ein, um JSON für die Update-Operation zu erhalten. Sie können die API GridJsWorkbook.UpdateCell verwenden, GridJs führt die Update-Operation im Cache durch und gibt das aktualisierte JSON zurück.
- Richten Sie eine Controller-Aktion ein, um die URLs der Bilder/Formdateien in der Tabellenkalkulation zu erhalten. GridJs wird automatisch alle Bilder/Formen im Cache zippen. Es wird die API GridCacheForStream.GetFileUrl verwendet.
- Richten Sie eine Controller-Aktion ein, um die Datei im Cache zu erhalten, damit können Sie die Bilder/Formen-Zip-Datei oder die Tabellenkalkulationsdatei im Cache erhalten. Es wird die API GridCacheForStream.LoadStream verwendet.
- Richten Sie eine Controller-Aktion ein, um die Tabellenkalkulation herunterzuladen. Sie können die API GridJsWorkbook.SaveToCacheWithFileName verwenden.

Unten ist eine einfache Demo zur Verwendung von Aspose.Cells.GridJs: https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs 

Wenn Sie Fragen, Anforderungen oder Hilfe benötigen, geben Sie bitte Feedback auf der folgenden Website https://forum.aspose.com/c/cells/9
