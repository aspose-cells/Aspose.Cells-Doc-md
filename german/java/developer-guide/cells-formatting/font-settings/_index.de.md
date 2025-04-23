---
title: Umgang mit Schriftart Einstellungen
linktitle: Schriftart Einstellungen
type: docs
weight: 20
url: /de/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

Das Aussehen des Textes kann durch Ändern seiner Schriftart-Einstellungen gesteuert werden. Zu diesen Schriftart-Einstellungen können der Name, Stil, Größe, Farbe und andere Effekte der Schriften gehören, wie unten in der Abbildung gezeigt:

**Schriftart-Einstellungen in Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Genau wie Microsoft Excel unterstützt auch Aspose.Cells die Konfiguration der Schriftart-Einstellungen der Zellen.

{{% /alert %}} 
## **Konfigurieren von Schriftarteinstellungen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) die den Zugriff auf jede Arbeitsmappe in einer Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) dargestellt. Die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung stellt ein Objekt der Klasse [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) dar.

Aspose.Cells bietet die Methode [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)'s [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) , um die Formatierung einer Zelle festzulegen. Außerdem bietet das Objekt der Klasse [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) Eigenschaften zur Konfiguration der Schriftarteinstellungen.

Dieser Artikel zeigt, wie: 

- [Einer spezifischen Schriftart für Text anwenden.](/cells/de/java/dealing-with-font-settings/)
- [Fetten Text festlegen](/cells/de/java/dealing-with-font-settings/).
- [Schriftgröße festlegen](/cells/de/java/dealing-with-font-settings/).
- [Schriftfarbe festlegen](/cells/de/java/dealing-with-font-settings/).
- [Text unterstreichen](/cells/de/java/dealing-with-font-settings/).
- [Text durchstreichen](/cells/de/java/dealing-with-font-settings/).
- [Text als Index setzen](/cells/de/java/dealing-with-font-settings/).
- [Text als Hochindex setzen](/cells/de/java/dealing-with-font-settings/).
### **Schriftartname festlegen**
Wenden Sie einer spezifischen Schriftart für Text in Zellen die [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt's [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) Eigenschaft an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Schriftschnitt auf Fett setzen**
Setzen Sie den Text fett, indem Sie das [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt's [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) Eigenschaft auf **true** setzen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Schriftgröße festlegen**
Legen Sie die Schriftgröße mit der [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt's [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) Eigenschaft fest.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Schriftart-Unterstrich-Typ festlegen**
Unterstreichen Sie den Text mit der [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt's [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) Eigenschaft. Aspose.Cells bietet verschiedene vordefinierte Schriftart-Unterstricharten in der [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType) Aufzählung.

|**Schriftart-Unterstreichungstypen**|**Beschreibung**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Kein Unterstrich|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Ein einfacher Unterstrich|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Doppelter Unterstrich|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Einzelner Unterstrich für Rechnungswesen|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|Doppelte Buchhaltung-Unterstreichung|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Gestrichelter Unterstrich|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|Dicke Strichpunktlinie-Doppellinie Unterstreichung|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|Dicke Strichpunktlinie Unterstreichung|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|Dicke gestrichelte Unterstreichung|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|Lange gestrichelte Unterstreichung|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|Dicke lange gestrichelte Unterstreichung|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|Punkt-Strich Unterstreichung|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|Punkt-Punkt-Strich Unterstreichung|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Gepunkteter Unterstrich|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|Dicke gepunktete Unterstreichung|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Dicker Unterstrich|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Wellenunterstrich|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|Doppelt wellige Unterstreichung|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|Starke Wellen-Unterstreichung|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Unterstrichene Non-Space-Zeichen Nur|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Schriftfarbe festlegen**
Legen Sie die Schriftfarbe mit der [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Eigenschaft [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) des [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Objekts fest. Wählen Sie eine Farbe aus der [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-Aufzählung aus und weisen Sie die ausgewählte Farbe dem [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Objekt über [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) zu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Effekt Durchgestrichener Text festlegen**
Durchstreichen Sie den Text mit der [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Eigenschaft [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) des [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Objekts.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Tiefgestellte Zahl festlegen**
Machen Sie den Text tiefgestellt, indem Sie die [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Eigenschaft [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) des [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Objekts verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Hochgestellte Zahl festlegen**
Wenden Sie den Hochstellen-Effekt auf den Text mit der [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Eigenschaft [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) des [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font)-Objekts an.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Erweiterte Themen**
- [Hoch- und Tiefgestellt-Effekte auf Schriftarten anwenden](/cells/de/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen](/cells/de/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="java" >}}
