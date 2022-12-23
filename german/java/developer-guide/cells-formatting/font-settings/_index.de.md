---
title: Umgang mit Schrifteinstellungen
linktitle: Schrifteinstellungen
type: docs
weight: 20
url: /de/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

Das Erscheinungsbild des Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Diese Schriftarteinstellungen können Name, Stil, Größe, Farbe und andere Effekte der Schriftarten umfassen, wie unten in der Abbildung gezeigt:

**Schrifteinstellungen in Microsoft Excel** 

![todo: Bild_alt_Text](dealing-with-font-settings_1.png)

Genau wie Microsoft Excel unterstützt auch Aspose.Cells die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}} 
## **Schrifteinstellungen konfigurieren**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung stellt ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) )-Methode, mit der die Formatierung einer Zelle festgelegt wird. Auch das Objekt der[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Klasse stellt Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.

Dieser Artikel zeigt, wie Sie:

- [Wenden Sie eine bestimmte Schriftart auf Text an.](/cells/de/java/dealing-with-font-settings/)
- [Stellen Sie den Text auf fett](/cells/de/java/dealing-with-font-settings/).
- [Legen Sie die Schriftgröße fest](/cells/de/java/dealing-with-font-settings/).
- [Legen Sie die Schriftfarbe fest](/cells/de/java/dealing-with-font-settings/).
- [Text unterstreichen](/cells/de/java/dealing-with-font-settings/).
- [Durchgestrichener Text](/cells/de/java/dealing-with-font-settings/).
- [Text tiefstellen](/cells/de/java/dealing-with-font-settings/).
- [Text hochstellen](/cells/de/java/dealing-with-font-settings/).
### **Festlegen des Schriftartnamens**
 Wenden Sie mithilfe von eine bestimmte Schriftart auf Text in Zellen an[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[Name einsetzen](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Schriftstil auf Fett setzen**
 Setzen Sie den Text fett, indem Sie das einstellen[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) Eigentum zu**wahr**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Schriftgröße einstellen**
 Stellen Sie die Schriftgröße mit ein[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Festlegen des Unterstreichungstyps für Schriftarten**
 Text mit unterstreichen[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) Eigentum. Aspose.Cells bietet verschiedene vordefinierte Schriftarten für Unterstreichungen im[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)Aufzählung.

|**Unterstreichungstypen für Schriftarten**|**Beschreibung**|
|:- |:- |
|[KEINER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Keine Unterstreichung|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Eine einzelne Unterstreichung|
|[DOPPELT](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Doppelter Unterstrich|
|[BUCHHALTUNG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Eine einzige Buchhaltungsunterstreichung|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Doppelte Buchhaltung unterstreichen|
|[BINDESTRICH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Gestrichelte Unterstreichung|
|[BINDESTRICH_PUNKT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Dicker Strich-Punkt-Punkt-Unterstrich|
|[BINDESTRICH_PUNKT_SCHWER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Dicker Strich-Punkt-Unterstrich|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Dicker gestrichelter Unterstrich|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Lang gestrichelte Unterstreichung|
|[BINDESTRICH_LANG_SCHWER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Dicke lange gestrichelte Unterstreichung|
|[DOT SCHLAGEN](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Strich-Punkt-Unterstreichung|
|[PUNKT_PUNKT_BINDESTRICH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Strich-Punkt-Punkt-Unterstreichung|
|[GEPUNKTET](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Gepunktete Unterstreichung|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Dicke gepunktete Unterstreichung|
|[SCHWER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Dicke Unterstreichung|
|[WELLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Welle unterstreichen|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Unterstreichen mit doppelter Welle|
|[WELLIG_SCHWER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Schwere Wellenunterstreichung|
|` `[WÖRTER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Nur Nicht-Leerzeichen unterstreichen|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Schriftfarbe einstellen**
 Stellen Sie die Schriftfarbe mit ein[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setFarbe](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) Eigentum. Wählen Sie eine beliebige Farbe aus[Farbe](https://reference.aspose.com/cells/java/com.aspose.cells/Color) Aufzählung und ordnen Sie der die ausgewählte Farbe zu[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setFarbe](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Festlegen des Durchstreichungseffekts für Text**
 Durchgestrichener Text mit der[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setDurchgestrichen](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Index einstellen**
 Machen Sie Text hochgestellt, indem Sie die verwenden[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Einstellung hochgestellt**
 Wenden Sie Hochstellung auf Text mit an[Schriftart](https://reference.aspose.com/cells/java/com.aspose.cells/Font) Objekt[setHochgestellt](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Themen vorantreiben**
- [Wenden Sie hochgestellte und tiefgestellte Effekte auf Schriftarten an](/cells/de/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Rufen Sie eine Liste der Schriftarten ab, die in einer Tabelle oder Arbeitsmappe verwendet werden](/cells/de/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
