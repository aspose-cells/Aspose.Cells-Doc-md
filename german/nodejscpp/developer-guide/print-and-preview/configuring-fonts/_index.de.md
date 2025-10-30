---
title: Fonts für die Renderung von Tabellenkalkulationen mit Node.js über C++ konfigurieren
linktitle: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Erfahren Sie, wie Sie Schriftarten für die Renderung von Tabellenkalkulationen mit Aspose.Cells for Node.js via C++ konfigurieren. Stellen Sie sicher, dass die Schriftarten für eine optimale Konvertierungsgenauigkeit verfügbar sind.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells APIs bieten die Möglichkeit, Tabellenkalkulationen in Bildformate zu rendern sowie in PDF- und XPS-Formate zu konvertieren. Um die Konvertierungsqualität zu maximieren, müssen die in der Tabelle verwendeten Schriftarten im Standard-Schriftartenverzeichnis des Betriebssystems vorhanden sein. Falls die erforderlichen Schriftarten nicht vorhanden sind, versuchen die APIs, die benötigten Schriftarten durch verfügbare zu ersetzen.

## **Auswahl von Schriftarten**

Im Folgenden wird der Prozess erläutert, den die Aspose.Cells-APIs im Hintergrund durchlaufen.

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Schriftarten mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart unter dem [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--)-Eigenschaft des Arbeitsblatts zu verwenden.
1. Wenn die API die unter [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) oder [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) Eigenschaft zu verwenden.
1. Wenn die API die unter [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) oder [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) Eigenschaft zu verwenden.
1. Wenn die API die unter [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--) definierte Schriftart nicht finden kann, versucht sie, die geeignetsten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich rendert die API die Tabelle mit Arial, wenn sie keine Schriftarten im Dateisystem finden kann.

## **Benutzerdefinierte Schriftartordner einstellen**

Die APIs von Aspose.Cells durchsuchen das Standard-Schriftartenverzeichnis des Betriebssystems nach den erforderlichen Schriftarten. Falls die Schriftarten im System nicht vorhanden sind, durchsuchen die APIs benutzerdefinierte (vom Nutzer festgelegte) Verzeichnisse. Die Klasse [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) bietet verschiedene Methoden, um benutzerdefinierte Schriftartenverzeichnisse festzulegen, wie unten beschrieben.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Diese Methode ist nützlich, wenn die Schriftarten in mehreren Ordnern vorhanden sind und der Benutzer alle Ordner separat einrichten möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Diese Mechanismus ist nützlich, wenn der Benutzer Schriften aus mehreren Ordnern laden möchte oder eine einzelne Schriftdatei oder Schriftdaten aus einem Byte-Array.

{{% alert color="primary" %}}

Beide [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) und [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) Methoden akzeptieren einen booleschen Typ als zweiten Parameter. Das Übergeben von **true** als zweitem Parameter leitet die Aspose.Cells-APIs an, die Unterordner nach den Schriftarten-Dateien zu durchsuchen.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, also bevor andere Objekte der Aspose.Cells-APIs aufgerufen werden.

{{% /alert %}} {{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Festlegen der Schriftquellen verwendet werden, gelten nur die letzten Einstellungen.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Die APIs von Aspose.Cells bieten auch die Möglichkeit, Ersatzschriften für Renderungszwecke anzugeben. Dieses Mechanismus ist hilfreich, wenn eine benötigte Schriftart auf dem System nicht verfügbar ist. Nutzer können eine Liste von Schriftartenamen als Alternativen zu der ursprünglich geforderten Schriftart angeben. Dafür hat die API die Methode [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ **string**, der Name der zu ersetzenden Schriftart. Der zweite Parameter ist ein Array vom Typ **string**. Nutzer können eine Liste von Schriftartnamen als Ersatz für die ursprüngliche Schriftart (im ersten Parameter angegeben) bereitstellen.

Hier ist ein einfaches Anwendungsbeispiel.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Informationssammlung**

Zusätzlich zu den oben genannten Methoden bieten die APIs von Aspose.Cells auch Mittel, um Informationen über festgelegte Quellen und Alternativen zu sammeln.

1. Die [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) zurück, das die Liste der angegebenen Schriftartenquellen enthält. Falls keine Quellen festgelegt wurden, gibt die [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) Methode ein leeres Array zurück.
1. Die [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) Methode akzeptiert einen Parameter vom Typ **string**, um den Namen der Schriftart anzugeben, für die eine Ersetzung festgelegt wurde. Falls für den angegebenen Schriftartnamen keine Ersetzung festgelegt ist, gibt die [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) Methode null zurück.

## **Erweiterte Themen**
- [Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen](/cells/de/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions festlegen, um Priorität zu haben](/cells/de/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/nodejs-cpp/supported-font-formats/)
- [Arbeitsblatt zu Bild - Setzen des Pixelformats für das gerenderte Bild](/cells/de/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="nodejs-cpp" >}}
