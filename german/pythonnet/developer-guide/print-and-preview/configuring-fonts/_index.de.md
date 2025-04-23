---
title: Konfigurieren von Schriftarten zur Darstellung von Tabellenkalkulationen
type: docs
weight: 10
url: /de/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Mögliche Verwendungsszenarien**

Das API von Aspose.Cells for Python via .NET bietet die Möglichkeit, Tabellen in Bildformaten zu rendern und sie in PDF- & XPS-Formate umzuwandeln. Um die Konvertierungsqualität zu maximieren, müssen die in der Tabelle verwendeten Schriftarten im Standard-Schriftartenordner des Betriebssystems vorhanden sein. Falls die erforderlichen Schriftarten fehlen, versucht das API, die benötigten Schriftarten durch die verfügbaren zu ersetzen.

## **Auswahl von Schriftarten**

Unten ist der Prozess, den das API von Aspose.Cells for Python via .NET im Hintergrund ausführt.

1. Die API versucht, die Schriftarten im Dateisystem zu finden, die dem exakten Schriftartnamen entsprechen, der in der Tabelle verwendet wird.
1. Wenn die API die Schriftarten mit genau demselben Namen nicht finden kann, versucht sie, die Standardschriftart unter dem [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-Eigenschaft des Arbeitsblatts zu verwenden.
1. Wenn die API die unter [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) oder [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) Eigenschaft zu verwenden.
1. Wenn die API die unter [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) oder [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) definierte Schriftart nicht finden kann, versucht sie, die Schriftart unter [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) Eigenschaft zu verwenden.
1. Wenn die API die unter [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) definierte Schriftart nicht finden kann, versucht sie, die geeignetsten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Schließlich rendert die API die Tabelle mit Arial, wenn sie keine Schriftarten im Dateisystem finden kann.

## **Benutzerdefinierte Schriftartordner einstellen**

Aspose.Cells für Python via .NET APIs durchsuchen das Standard-Schriftartenverzeichnis des Betriebssystems nach den benötigten Schriftarten. Falls die erforderlichen Schriftarten nicht im Schriftartenverzeichnis des Systems verfügbar sind, durchsuchen die APIs die benutzerdefinierten (vom Benutzer definierten) Verzeichnisse. Die [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs)-Klasse bietet eine Reihe von Möglichkeiten, benutzerdefinierte Schriftartverzeichnisse festzulegen, wie unten beschrieben.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Diese Methode ist nützlich, wenn nur ein Ordner festgelegt werden soll.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Diese Methode ist nützlich, wenn die Schriftarten in mehreren Ordnern vorhanden sind und der Benutzer alle Ordner separat einrichten möchte, anstatt alle Schriftarten in einem einzigen Ordner zu kombinieren.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Diese Mechanismus ist nützlich, wenn der Benutzer Schriften aus mehreren Ordnern laden möchte oder eine einzelne Schriftdatei oder Schriftdaten aus einem Byte-Array.

{{% alert color="primary" %}}

Sowohl [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) als auch [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) Methoden akzeptieren einen zweiten Parameter vom Boolean-Typ. Das Übergeben von **true** als zweiten Parameter weist die Aspose.Cells für Python via .NET APIs an, die Unterordner nach Schriftartdateien zu durchsuchen.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Bitte verwenden Sie eine der oben genannten Methoden zu Beginn der Anwendung, also vor dem Aufrufen anderer Objekte der Aspose.Cells für Python via .NET APIs.

{{% /alert %}} {{% alert color="primary" %}}

Wenn alle oben genannten Methoden zum Festlegen der Schriftquellen verwendet werden, gelten nur die letzten Einstellungen.

{{% /alert %}}

## **Schriftarten-Ersatzmechanismus**

Aspose.Cells für Python via .NET APIs bieten auch die Möglichkeit, die Ersatzschriftart für Darstellungszwecke festzulegen. Dieser Mechanismus ist hilfreich, wenn eine erforderliche Schriftart auf dem Rechner fehlt, auf dem die Konvertierung durchgeführt werden soll. Benutzer können eine Liste von Schriftartnamen als Alternative zur ursprünglich benötigten Schriftart angeben. Dafür haben die Aspose.Cells für Python via .NET APIs die exposierte [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list)-Methode, die 2 Parameter akzeptiert. Der erste Parameter ist vom Typ **string**, der Name der zu ersetzenden Schriftart. Der zweite Parameter ist ein Array vom Typ **string**. Benutzer können eine Liste von Schriftartnamen als Ersatz für die ursprüngliche Schriftart angeben (im ersten Parameter angegeben).

Hier ist ein einfaches Anwendungsbeispiel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Informationssammlung**

Neben den oben genannten Methoden haben die Aspose.Cells für Python via .NET APIs auch Möglichkeiten bereitgestellt, Informationen darüber zu sammeln, welche Quellen und Ersatzschriften festgelegt wurden.

1. Die [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) Methode gibt ein Array vom Typ [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) zurück, das die Liste der angegebenen Schriftartenquellen enthält. Falls keine Quellen festgelegt wurden, gibt die [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) Methode ein leeres Array zurück.
1. Die [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) Methode akzeptiert einen Parameter vom Typ **string**, mit dem die Schriftart festgelegt werden kann, für die die Ersetzung vorgenommen wurde. Falls keine Ersetzung für den angegebenen Schriftartnamen vorgenommen wurde, gibt die [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) Methode null zurück.

## **Erweiterte Themen**
- [Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen](/cells/de/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions festlegen, um Priorität zu haben](/cells/de/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Unterstützte Schriftformate](/cells/de/python-net/supported-font-formats/)
- [Arbeitsblatt zu Bild - Setzen des Pixelformats für das gerenderte Bild](/cells/de/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

