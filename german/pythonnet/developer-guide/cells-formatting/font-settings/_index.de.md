---
title: Schriftart Einstellungen
description: Aspose.Cells ist eine Python Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen der Schriftarteinstellungen von Zellen, sodass Benutzer den Schriftstil und die Eigenschaften der Zellen anpassen können. Dieser Artikel stellt vor, wie man mit der Aspose.Cells für Python via .NET Bibliothek die Schriftarteinstellungen der Zellen festlegt.
keywords: Aspose.Cells für Python via .NET, Zellen, Schriftarteinstellungen, Stile, Eigenschaften
type: docs
weight: 30
url: /de/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

Das Aussehen eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können Name, Stil, Größe, Farbe und andere Effekte der Schrift umfassen. Genau wie Microsoft Excel unterstützt Aspose.Cells für Python via .NET auch die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}}

## **Konfigurieren von Schriftarteinstellungen**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse dargestellt. Die [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Klasse bietet eine [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)-Sammlung. Jedes Element in der [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/)-Sammlung repräsentiert ein Objekt der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse.

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Klasse' [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) und [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style)-Methoden, die verwendet werden, um den Formatierungsstil einer Zelle abzurufen und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) bietet Eigenschaften zur Konfiguration der Schriftarteinstellungen.

### **Schriftartname festlegen**

Entwickler können jede Schriftart auf Text innerhalb einer Zelle anwenden, indem sie die [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-Eigenschaft des [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/)-Objekts verwenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Schriftschnitt auf Fett setzen**

Entwickler können den Text fett machen, indem sie die Eigenschaft [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) des Objekts [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Schriftgröße festlegen**

Setzen Sie die Schriftgröße mit der [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size)-Eigenschaft des Objekts [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Schriftfarbe festlegen**

Verwenden Sie die Eigenschaft [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) des Objekts [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font), um die Schriftfarbe festzulegen. Wählen Sie eine Farbe aus der Color-Enumeration (Teil des .NET-Frameworks) aus und weisen Sie sie der [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color)-Eigenschaft zu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Schriftart-Unterstrich-Typ festlegen**

Verwenden Sie die [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline)-Eigenschaft des [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-Objekts, um Text zu unterstreichen. Aspose.Cells für Python via .NET bietet verschiedene vordefinierte Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype)-Enumeration.

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|
| :- | :- |
|BUCHHALTUNG|Einzelne Buchhaltung-Unterstreichung|
|DOPPELT|Doppelte Unterstreichung|
|DOPPELT_BUCHHALTUNG|Doppelte buchhalterische Unterstreichung|
|KEINE|Keine Unterstreichung|
|EINZEL|Eine einzelne Unterstreichung|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Einstellung des Durchgestrichen-Effekts**

Wenden Sie den Durchgestrichen-Effekt an, indem Sie die Eigenschaft [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) des Objekts [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Einstellen des Tiefgestellt-Effekts**

Wenden Sie den Tiefgestellt-Effekt an, indem Sie die Eigenschaft [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) des Objekts [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Einstellen des Hochgestellt-Effekts auf Schriftart**

Entwickler können den Hochgestellt-Effekt auf die Schriftart anwenden, indem sie die [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript)-Eigenschaft des [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font)-Objekts auf **true** setzen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Erweiterte Themen**
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


{{< app/cells/assistant language="python-net" >}}
