---
title: Schriftarteinstellungen
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen der Schriftarteinstellungen von Zellen, sodass Benutzer den Schriftartstil und die Eigenschaften von Zellen anpassen können. In diesem Artikel wird erläutert, wie Sie mithilfe der Bibliothek Aspose.Cells die Einstellungen für die Schriftart von Zellen festlegen.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /de/net/cells-font-settings/
---
{{% alert color="primary" %}}

Das Erscheinungsbild eines Textes kann durch Ändern der Schriftarteinstellungen gesteuert werden. Die Schriftarteinstellungen können den Namen, den Stil, die Größe, die Farbe und andere Effekte der Schriftarten umfassen. Ebenso wie Microsoft Excel unterstützt auch Aspose.Cells die Konfiguration der Schriftarteinstellungen der Zellen.

{{% /alert %}}

##  **Konfigurieren der Schriftarteinstellungen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse'[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden, die zum Abrufen und Festlegen des Formatierungsstils einer Zelle verwendet werden. Der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Die Klasse stellt Eigenschaften zum Konfigurieren von Schriftarteinstellungen bereit.

###  **Festlegen des Schriftartnamens**

 Entwickler können mithilfe von jede beliebige Schriftart auf Text in einer Zelle anwenden[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Setzen Sie den Schriftstil auf „Fett“.**

 Entwickler können Text fett formatieren, indem sie festlegen[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)Eigenschaft auf *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Schriftgröße einstellen**

Stellen Sie die Schriftgröße mit ein[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**Größe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Schriftfarbe einstellen**

Benutzen Sie die[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)Eigenschaft zum Festlegen der Schriftfarbe. Wählen Sie eine beliebige Farbe aus der Farbaufzählung (Teil des .NET-Frameworks) aus und weisen Sie sie dem zu[**Farbe**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Festlegen des Schriftart-Unterstreichungstyps**

Benutzen Sie die[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**Unterstreichen**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)Eigenschaft zum Unterstreichen von Text. Aspose.Cells bietet verschiedene vordefinierte Schriftarten für Unterstreichungen im[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) Aufzählung.

|**Schriftarten für Unterstreichungen**|**Beschreibung**|
| :- | :- |
|Buchhaltung|Eine einzelne Buchhaltungsunterstreichung|
|Doppelt|Doppelte Unterstreichung|
|DoubleAccounting|Doppelte Buchhaltung unterstreichen|
|Keiner|Keine Unterstreichung|
|Einzel|Eine einzelne Unterstreichung|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Festlegen des Strikeout-Effekts**

Wenden Sie die Durchstreichung an, indem Sie die festlegen[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) Objekt[**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)Eigenschaft auf *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Tiefgestellten Effekt einstellen**

Wenden Sie den Index an, indem Sie festlegen[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt[**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)Eigenschaft auf *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Festlegen des Hochstellungseffekts für die Schriftart**

 Entwickler können den hochgestellten Effekt auf die Schriftart anwenden, indem sie festlegen[**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) Eigentum der[**Stil.Schriftart**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)Objekt auf *true** setzen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **Vorabthemen**
- [Wenden Sie hochgestellte und tiefgestellte Effekte auf Schriftarten an](/cells/de/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Rufen Sie eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten ab](/cells/de/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

