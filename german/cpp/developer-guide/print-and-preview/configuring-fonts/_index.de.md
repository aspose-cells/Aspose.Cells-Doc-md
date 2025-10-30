---
title: Fonts für das Rendern von Tabellenkalkulationen mit C++ konfigurieren
linktitle: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Erfahren Sie, wie Sie Fonts für das Rendern von Tabellenkalkulationen in Bilder, PDF und XPS Formate mit Aspose.Cells for C++ konfigurieren.
---

## **Mögliche Verwendungsszenarien**

Die Aspose.Cells-APIs ermöglichen das Rendern von Tabellenkalkulationen in Bildformaten sowie die Umwandlung in PDF- und XPS-Formate. Damit die Konvertierungsqualität maximiert wird, müssen die in der Tabelle verwendeten Fonts im Standard-Font-Verzeichnis des Betriebssystems vorhanden sein. Wenn die benötigten Fonts nicht vorhanden sind, versucht die Aspose.Cells-API, die erforderlichen Fonts durch verfügbare zu ersetzen.

## **Auswahl von Schriftarten**

Unten ist der Prozess, den die Aspose.Cells-APIs im Hintergrund durchführen:

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Fonts mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart gemäß der [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)-Eigenschaft der Arbeitsmappe zu verwenden.
1. Wenn die API die in der Arbeitsmappe definierte Schriftart unter [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) nicht finden kann, versucht sie, die Schriftart gemäß der [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)-Eigenschaft zu verwenden.
1. Wenn die API die Schriftart unter [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) festzulegen.
1. Wenn die API die Schriftart unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) nicht finden kann, versucht sie, die am besten geeignete Schriftart aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich, wenn die API keine Schriftarten auf dem System findet, rendert sie die Tabelle mit Arial.

## **Benutzerdefinierte Schriftartordner einstellen**

Die Aspose.Cells-APIs durchsuchen das Standard-Schriftartenverzeichnis des Betriebssystems nach den benötigten Fonts. Wenn die benötigten Fonts im Systemfont-Verzeichnis nicht vorhanden sind, durchsuchen die APIs benutzerdefinierte (benutzerdefinierte) Verzeichnisse. Die Klasse [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) bietet mehrere Möglichkeiten, benutzerdefinierte Schriftartenverzeichnisse festzulegen, wie unten beschrieben:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Diese Methode ist nützlich, wenn die Fonts in mehreren Ordnern liegen und der Benutzer alle Ordner separat festlegen möchte, anstatt alle Fonts in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Dieser Mechanismus ist nützlich, wenn der Benutzer Schriftarten aus mehreren Ordnern, einer einzigen Schriftartdatei oder Schriftartdaten aus einem Byte-Array laden möchte.

{{% alert color="primary" %}}

Sowohl [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) als auch [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) Methoden akzeptieren einen zweiten Parameter vom Typ Boolean. Wenn **true** als zweiter Parameter übergeben wird, weist dies die Aspose.Cells APIs an, die Unterordner nach Schriftartdateien zu durchsuchen.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, das heißt, bevor Sie andere Objekte der Aspose.Cells APIs aufrufen.

{{% /alert %}}

{{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Festlegen der Schriftquellen verwendet werden, gelten nur die letzten Einstellungen.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Aspose.Cells APIs bieten auch die Möglichkeit, Ersatzschriftarten für Darstellungszwecke anzugeben. Dieser Mechanismus ist hilfreich, wenn die benötigte Schriftart auf dem Computer, auf dem die Konvertierung erfolgt, nicht verfügbar ist. Benutzer können eine Liste von Schriftartnamen als Alternative zur ursprünglich benötigten Schriftart bereitstellen. Um dies zu erreichen, haben die Aspose.Cells APIs die [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/) Methode freigegeben, die zwei Parameter akzeptiert. Der erste Parameter ist vom Typ **string** und sollte der Name der zu ersetzenden Schriftart sein. Der zweite Parameter ist ein Array vom Typ **string**. Benutzer können eine Liste von Schriftartnamen als Ersatz für den ursprünglichen Schriftartnamen (im ersten Parameter angegeben) angeben.

Hier ist ein einfaches Verwendungsszenario:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Informationssammlung**

Neben den oben genannten Methoden bieten die Aspose.Cells APIs auch Möglichkeiten, Informationen darüber zu sammeln, welche Quellen und Ersetzungen festgelegt wurden:

1. Die [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/)-Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) zurück, das die Liste der angegebenen Schriftquellen enthält. Wenn keine Quellen festgelegt wurden, gibt die [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/)-Methode ein leeres Array zurück.
1. Die [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/)-Methode akzeptiert einen Parameter vom Typ **string**, mit dem Sie den Schriftartnamen angeben können, für den eine Ersetzung festgelegt wurde. Wenn für den angegebenen Schriftartnamen keine Ersetzung festgelegt wurde, gibt die [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/)-Methode null zurück.

## **Fortgeschrittene Themen**
- [Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen](/cells/de/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions festlegen, um Priorität zu haben](/cells/de/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
