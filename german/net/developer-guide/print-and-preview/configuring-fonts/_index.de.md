---
title: Konfigurieren von Schriftarten zum Rendern von Tabellenkalkulationen
type: docs
weight: 10
url: /de/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells-APIs bieten die Möglichkeit, die Tabellenkalkulationen in Bildformaten zu rendern und sie in die Formate PDF und XPS zu konvertieren. Um die Konvertierungstreue zu maximieren, müssen die in der Tabelle verwendeten Schriftarten im Standardverzeichnis für Schriftarten des Betriebssystems verfügbar sein. Falls die erforderlichen Schriftarten nicht vorhanden sind, versuchen die Aspose.Cells-APIs, die erforderlichen Schriftarten durch die verfügbaren zu ersetzen.

## **Auswahl an Schriftarten**

Unten ist der Prozess, dem Aspose.Cells-APIs hinter den Kulissen folgen.

1. Der API versucht, die Schriftarten im Dateisystem zu finden, die genau mit dem in der Tabelle verwendeten Schriftartnamen übereinstimmen.
1.  Wenn API die Schriftarten mit genau demselben Namen nicht finden kann, versucht es, die unter der Arbeitsmappe angegebene Standardschriftart zu verwenden**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** Eigentum.
1.  Wenn API die unter der Arbeitsmappe definierte Schriftart nicht finden kann**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** -Eigenschaft versucht es, die unter angegebene Schriftart zu verwenden**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** oder**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** Eigentum.
1.  Wenn API die unter definierte Schriftart nicht finden kann**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** oder**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** -Eigenschaft versucht es, die unter angegebene Schriftart zu verwenden**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** Eigentum.
1.  Wenn API die unter definierte Schriftart nicht finden kann**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** -Eigenschaft versucht es, die am besten geeigneten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Wenn schließlich API keine Schriftarten im Dateisystem finden kann, wird die Tabelle mit Arial gerendert.

## **Legen Sie benutzerdefinierte Schriftordner fest**

 Aspose.Cells APIs durchsuchen das Standardverzeichnis für Schriftarten des Betriebssystems nach den erforderlichen Schriftarten. Falls die erforderlichen Schriftarten nicht im Schriftartenverzeichnis des Systems verfügbar sind, durchsuchen die APIs die benutzerdefinierten (benutzerdefinierten) Verzeichnisse. Das**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**Die Klasse hat eine Reihe von Möglichkeiten zum Festlegen benutzerdefinierter Schriftartenverzeichnisse gezeigt, wie unten beschrieben.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: Diese Methode ist nützlich, wenn sich die Schriftarten in mehreren Ordnern befinden und der Benutzer alle Ordner separat festlegen möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**Hinweis: Dieser Mechanismus ist nützlich, wenn der Benutzer Schriftarten aus mehreren Ordnern oder eine einzelne Schriftartdatei oder Schriftartdaten aus einem Array von Bytes laden möchte.

{{% alert color="primary" %}}

 Beide**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** Methoden akzeptieren einen zweiten Parameter vom Typ Boolean. Vorbeigehen**wahr** da der zweite Parameter die Aspose.Cells-APIs anweist, die Unterordner nach den Schriftartdateien zu durchsuchen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Bitte verwenden Sie zu Beginn der Bewerbung eine der oben genannten Methoden, d.h. bevor andere Objekte von Aspose.Cells-APIs aufgerufen werden.

{{% /alert %}} {{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Einstellen der Schriftartquellen verwendet werden, werden nur die letzten Einstellungen wirksam.

{{% /alert %}}

## **Font-Ersetzungsmechanismus**

 Aspose.Cells-APIs bieten auch die Möglichkeit, die Ersatzschriftart für Wiedergabezwecke anzugeben. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Computer, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste mit Schriftartnamen als Alternative zur ursprünglich erforderlichen Schriftart bereitstellen. Um dies zu erreichen, haben die Aspose.Cells-APIs die ausgesetzt**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** Methode, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ**Schnur** , das sollte der Name der Schriftart sein, die ersetzt werden muss. Der zweite Parameter ist ein Array vom Typ**Schnur**Benutzer können eine Liste mit Schriftartnamen als Ersatz für den ursprünglichen Schriftartnamen (angegeben im ersten Parameter) bereitstellen.

Hier ist ein einfaches Nutzungsszenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Informationsbeschaffung**

Zusätzlich zu den oben erwähnten Methoden haben die Aspose.Cells-APIs auch Mittel bereitgestellt, um Informationen darüber zu sammeln, welche Quellen und Ersetzungen eingestellt wurden.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** Die Methode gibt ein Array des Typs zurück**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**enthält die Liste der angegebenen Schriftartquellen. Falls keine Quellen eingestellt wurden, wird die**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**Methode gibt ein leeres Array zurück.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** Die Methode akzeptiert einen Parameter vom Typ**Schnur** Ermöglicht die Angabe des Schriftartnamens, für den die Ersetzung festgelegt wurde. Falls für den angegebenen Schriftartnamen keine Ersetzung festgelegt wurde, dann die**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**Methode gibt null zurück.

## **Themen vorantreiben**
- [Legen Sie die Standardschriftart fest, während Sie die Tabelle in Bilder rendern](/cells/de/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Setzen Sie die DefaultFont-Eigenschaft von PdfSaveOptions und ImageOrPrintOptions auf Priorität](/cells/de/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/net/supported-font-formats/)
- [Arbeitsblatt zu Bild – Legen Sie das Pixelformat für das gerenderte Bild fest](/cells/de/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
