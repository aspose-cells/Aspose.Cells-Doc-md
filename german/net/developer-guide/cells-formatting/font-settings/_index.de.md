---
title: Schriftart Einstellungen
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien. Es unterstützt das Festlegen von Schriftarteinstellungen von Zellen und ermöglicht es Benutzern, den Schriftschnitt und die Eigenschaften von Zellen anzupassen. Dieser Artikel führt ein, wie die Aspose.Cells Bibliothek verwendet wird, um Schriftarteinstellungen von Zellen festzulegen.
keywords: Aspose.Cells, Zellen, Schriftarteinstellungen, Stile, Eigenschaften
type: docs
weight: 30
url: /de/net/cells-font-settings/
---

{{% alert color="primary" %}}

Das Erscheinungsbild eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können den Namen, den Stil, die Größe, die Farbe und andere Effekte der Schriftarten umfassen. Ganz wie Microsoft Excel unterstützt auch Aspose.Cells das Konfigurieren der Schriftarteinstellungen von Zellen.

{{% /alert %}}

## **Konfigurieren von Schriftarteinstellungen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jede Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse stellt eine [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung bereit. Jedes Element in der [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)-Sammlung repräsentiert ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells bietet die [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Klasse' [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)-Methoden, die verwendet werden, um den Formatierungsstil einer Zelle abzurufen und festzulegen. Die Klasse [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) bietet Eigenschaften zur Konfiguration der Schriftarteinstellungen.

### **Schriftartname festlegen**

Entwickler können eine beliebige Schrift auf den Text innerhalb einer Zelle anwenden, indem sie die Eigenschaft [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) des Objekts [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) verwenden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Schriftschnitt auf Fett setzen**

Entwickler können den Text fett machen, indem sie die Eigenschaft [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Schriftgröße festlegen**

Setzen Sie die Schriftgröße mit der [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)-Eigenschaft des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Schriftfarbe festlegen**

Verwenden Sie die Eigenschaft [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font), um die Schriftfarbe festzulegen. Wählen Sie eine Farbe aus der Color-Enumeration (Teil des .NET-Frameworks) aus und weisen Sie sie der [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)-Eigenschaft zu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Schriftart-Unterstrich-Typ festlegen**

Verwenden Sie die Eigenschaft [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font), um Text zu unterstreichen. Aspose.Cells bietet verschiedene vordefinierte Schriftarten-Unterstreichungstypen in der [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) Enumeration.

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|
| :- | :- |
|Accounting|Einzelne Buchhaltungsunterstreichung|
|Double|Doppelte Unterstreichung|
|DoubleAccounting|Doppelte Buchhaltungsunterstreichung|
|None|Keine Unterstreichung|
|Single|Einfache Unterstreichung|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Einstellung des Durchgestrichen-Effekts**

Wenden Sie den Durchgestrichen-Effekt an, indem Sie die Eigenschaft [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Einstellen des Tiefgestellt-Effekts**

Wenden Sie den Tiefgestellt-Effekt an, indem Sie die Eigenschaft [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) des Objekts [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) auf **true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Einstellen des Hochgestellt-Effekts auf Schriftart**

Entwickler können den Hochgestellt-Effekt auf die Schriftart anwenden, indem sie die [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript)-Eigenschaft des [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)-Objekts auf **true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Erweiterte Themen**
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
