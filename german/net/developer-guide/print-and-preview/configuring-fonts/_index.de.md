---
title: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells APIs bieten die Möglichkeit, die Tabellenkalkulationen in Bildformate zu rendern und in PDF- und XPS-Formate zu konvertieren. Um die Konvertierungsgenauigkeit zu maximieren, ist es erforderlich, dass die in der Tabellenkalkulation verwendeten Schriftarten im Standard-Schriftartenverzeichnis des Betriebssystems verfügbar sind. Falls die erforderlichen Schriftarten nicht vorhanden sind, werden die Aspose.Cells APIs versuchen, die erforderlichen Schriftarten durch verfügbare zu ersetzen.

## **Auswahl von Schriftarten**

Im Folgenden wird der Prozess erläutert, den die Aspose.Cells-APIs im Hintergrund durchlaufen.

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Schriftarten mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart unter dem [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)-Eigenschaft des Arbeitsblatts zu verwenden.
1. Wenn die API die unter [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) Eigenschaft zu verwenden.
1. Wenn die API die unter [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) oder [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) Eigenschaft zu verwenden.
1. Wenn die API die unter [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) definierte Schriftart nicht finden kann, versucht sie, die geeignetsten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich rendert die API die Tabelle mit Arial, wenn sie keine Schriftarten im Dateisystem finden kann.

{{% alert color="primary" %}}

Grundsätzlich durchsuchen die Aspose.Cells APIs standardmäßig die Schriftartenverzeichnisse des Betriebssystems unter Windows, Linux, MacOS. Ab [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/) durchsuchen die APIs zusätzlich standardmäßig die Office-Cache-Cloud-Schriftartenverzeichnisse.

{{% /alert %}}

## **Benutzerdefinierte Schriftartordner einstellen**

Aspose.Cells-APIs suchen im Standard-Schriftartverzeichnis des Betriebssystems nach den benötigten Schriftarten. Falls die benötigten Schriftarten nicht im Schriftartverzeichnis des Systems vorhanden sind, durchsuchen die APIs die benutzerdefinierten (benutzerdefinierte) Verzeichnisse. Die Klasse [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) hat verschiedene Möglichkeiten zum Setzen von benutzerdefinierten Schriftartverzeichnissen, wie unten detailliert beschrieben.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Diese Methode ist nützlich, wenn die Schriftarten in mehreren Ordnern vorhanden sind und der Benutzer alle Ordner separat einrichten möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Diese Mechanismus ist nützlich, wenn der Benutzer Schriften aus mehreren Ordnern laden möchte oder eine einzelne Schriftdatei oder Schriftdaten aus einem Byte-Array.

{{% alert color="primary" %}}

Beide [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) und [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) Methoden akzeptieren einen booleschen Typ als zweiten Parameter. Das Übergeben von **true** als zweitem Parameter leitet die Aspose.Cells-APIs an, die Unterordner nach den Schriftarten-Dateien zu durchsuchen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, also bevor andere Objekte der Aspose.Cells-APIs aufgerufen werden.

{{% /alert %}} {{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Festlegen der Schriftquellen verwendet werden, gelten nur die letzten Einstellungen.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Die Aspose.Cells-APIs bieten auch die Möglichkeit, die Ersatzschriftart für das Rendern festzulegen. Dieser Mechanismus ist hilfreich, wenn eine benötigte Schriftart auf dem Rechner, auf dem die Konvertierung stattfinden soll, nicht verfügbar ist. Benutzer können eine Liste von Schriftartnamen als Alternative zur ursprünglich benötigten Schriftart festlegen. Um dies zu erreichen, haben die Aspose.Cells-APIs die [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) Methode freigegeben, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ **string** und sollte der Name der Schriftart sein, die ersetzt werden soll. Der zweite Parameter ist ein Array vom Typ **string**. Benutzer können eine Liste von Schriftartnamen als Ersatz für den originalen Schriftnamen (im ersten Parameter angegeben) angeben.

Hier ist ein einfaches Anwendungsbeispiel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Informationssammlung**

Neben den oben genannten Methoden bieten die Aspose.Cells APIs auch Möglichkeiten, Informationen darüber zu sammeln, welche Quellen und Substitutionen festgelegt wurden.

1. Die [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) zurück, das die Liste der angegebenen Schriftartenquellen enthält. Falls keine Quellen festgelegt wurden, gibt die [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) Methode ein leeres Array zurück.
1. Die [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) Methode akzeptiert einen Parameter vom Typ **string**, mit dem die Schriftart festgelegt werden kann, für die die Ersetzung vorgenommen wurde. Falls keine Ersetzung für den angegebenen Schriftartnamen vorgenommen wurde, gibt die [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) Methode null zurück.

## **Erweiterte Themen**
- [Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen](/cells/de/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions festlegen, um Priorität zu haben](/cells/de/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/net/supported-font-formats/)
- [Arbeitsblatt zu Bild - Setzen des Pixelformats für das gerenderte Bild](/cells/de/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
