---
title: Schrifteinstellungen
type: docs
weight: 30
url: /de/net/cells-font-settings/
---
{{% alert color="primary" %}}

Das Erscheinungsbild eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können Name, Stil, Größe, Farbe und andere Effekte der Schriftarten umfassen. Genau wie Microsoft Excel unterstützt auch Aspose.Cells die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}}

## **Schrifteinstellungen konfigurieren**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden, die zum Abrufen und Festlegen des Formatierungsstils einer Zelle verwendet werden. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)-Klasse stellt Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.

### **Festlegen des Schriftartnamens**

 Entwickler können jede Schriftart auf Text in einer Zelle anwenden, indem sie die verwenden[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Schriftstil auf Fett setzen**

 Entwickler können Text fett darstellen, indem sie das festlegen[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**IstBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) Eigentum zu**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Schriftgröße einstellen**

Stellen Sie die Schriftgröße mit ein[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**Größe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Schriftfarbe einstellen**

Verwenden Sie die[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)-Eigenschaft zum Festlegen der Schriftfarbe. Wählen Sie eine beliebige Farbe aus der Farbaufzählung (Teil des .NET-Frameworks) und weisen Sie sie der zu[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Festlegen des Unterstreichungstyps für Schriftarten**

Verwenden Sie die[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**Unterstreichen**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)Eigenschaft zum Unterstreichen von Text. Aspose.Cells bietet verschiedene vordefinierte Schriftarten für Unterstreichungen im[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) Aufzählung.

|**Unterstreichungstypen für Schriftarten**|**Beschreibung**|
|:- |:- |
|Buchhaltung|Eine einzige Buchhaltungsunterstreichung|
|Doppelt|Doppelter Unterstrich|
|DoubleAccounting|Doppelte Buchhaltung unterstreichen|
|Keiner|Keine Unterstreichung|
|Single|Eine einzelne Unterstreichung|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Einstellung des Strikeout-Effekts**

Wenden Sie das Durchstreichen an, indem Sie das festlegen[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)Eigentum zu**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Subscript-Effekt einstellen**

Wenden Sie den Index an, indem Sie die[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) Eigentum zu**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Einstellen des hochgestellten Effekts auf die Schriftart**

 Entwickler können den hochgestellten Effekt auf die Schriftart anwenden, indem sie die[**IstHochgestellt**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) Eigentum der[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) widersprechen**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Themen vorantreiben**
- [Wenden Sie hochgestellte und tiefgestellte Effekte auf Schriftarten an](/cells/de/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Rufen Sie eine Liste der Schriftarten ab, die in einer Tabelle oder Arbeitsmappe verwendet werden](/cells/de/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

