---
title: Aspose.Cells.GridJs Grundlagen
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/basics/
keywords: gridjs,python,edit,spreadsheet,view,viewer,editor,excel
---

## Grundlagen von GridJs

Aspose.Cells.GridJs ist eine Bibliothek, die es Benutzern ermöglicht, plattformübergreifende Webanwendungen zur schnellen und einfachen Anzeige oder Bearbeitung von Tabellenkalkulationsdateien zu entwickeln. 

## Warum Aspose.Cells.GridJs verwenden


- Es ermöglicht Benutzern, Tabellenkalkulationen zu erstellen, zu bearbeiten, zu formatieren, zusammenzuarbeiten und sicher zu teilen, mit Echtzeit-Updates, Formelunterstützung und umfangreichen Datenvisualisierungstools, ähnlich wie bei herkömmlichen Desktopanwendungen.
- Es unterstützt Dateneingabe und -bearbeitung, Format, Tabellenkalkulationsnavigation, Formelberechnung, Datenmanipulation, Diagramme und Visualisierungen, Import und Export, Sicherheit, Add-Ons und Anpassungen für Entwickler, um den Editor an spezifische Geschäftsanforderungen anzupassen.

## Funktionen


- Importieren, Anzeigen und Bearbeiten der gängigen Tabellenkalkulationsformate.
- Exportieren der Tabellenkalkulationen in verschiedene unterstützte Dateiformate.
- Anzeigen und Verwalten von Bilddateien, Formen oder Diagrammen.
- Durchführung von Gitterdesign- und Layoutanpassungen.
- Verwaltung mehrerer Arbeitsblätter.
- Erstellung und Berechnung von Excel®-Formeln.

## Unterstützte Dateiformate

https://docs.aspose.com/cells/python-net/supported-file-formats/

## Allgemeine Verwendung

Nachfolgend sind die grundlegenden Prozessschritte zur Entwicklung einer Webanwendung für GridJs aufgeführt.

- Legen Sie das Cache-Speicherverzeichnis über Config.set_file_cache_directory(`Speicherpfad`) fest.
- Lizenz über Config.set_license(`Lizenzpfad`) festlegen.
- Legen Sie die Bildrouten-URL GridJsWorkbook.set_image_url_base(`Route für die Bildanzeige`);
- Richten Sie eine Aktionroute ein, um `json` aus der Tabellenkalkulationsdatei zu erhalten. Sie können die APIs `GridJsWorkbook.ImportExcelFile` und `GridJsWorkbook.ExportToJson` verwenden, `GridJs` speichert die Datei automatisch im Cache.
- Richten Sie eine Aktionroute für die Aktualisierungsoperation ein, um `json` zu erhalten. Sie können die API `GridJsWorkbook.UpdateCell` verwenden, `GridJs` führt die Aktualisierungsoperation im Cache durch und gibt das aktualisierte `json` zurück.
- Richten Sie eine Aktionroute ein, um die Datei im Cache zu erhalten, um die Bilder/Forms Zip-Datei oder die Tabellenkalkulationsdatei im Cache abzurufen.
- Richten Sie eine Routenaktion ein, um die Tabellenkalkulation herunterzuladen. Sie können die API `GridJsWorkbook.SaveToCacheWithFileName` verwenden.

Nachfolgend finden Sie eine grundlegende Demo zur Veranschaulichung der Verwendung von Aspose.Cells.GridJs:

https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net 

In der Demo verwenden wir [gridjs-spreadsheet](https://www.npmjs.com/package/gridjs-spreadsheet) zur Darstellung der Client-seitigen Seite.

Wenn Sie Fragen, Anforderungen oder Hilfe benötigen, geben Sie bitte Feedback auf der folgenden Website https://forum.aspose.com/c/cells/9
