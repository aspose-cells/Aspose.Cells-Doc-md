---
title: Diagramm in Bild umwandeln für die japanische Region
description: Erfahren Sie, wie Sie Aspose.Cells for .NET die japanische Konfiguration für das Diagramm einstellen. Unser Leitfaden zeigt, wie Sie Diagramme so konfigurieren, dass sie japanische Zeichen und Formatierung unterstützen, einschließlich Schriftarten, Größe, Textausrichtung und mehr.
keywords: Aspose.Cells for .NET, Diagramme, japanische Konfiguration, Schriftart, Schriftgröße, Textausrichtung, Unterstützung.
linktitle: Japanische Region festlegen
type: docs
weight: 10
url: /de/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie die japanische Region für ein Diagramm festlegen können.

{{% /alert %}}

## **Definiert eine Vererbungsklasse**

Als ersten Schritt müssen Sie eine Klasse "ChartJapaneseSetttings" definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) erbt. 
Dann können Sie durch Neudefinition der entsprechenden Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.
Codebeispiel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Japanische Einstellung für Diagramm konfigurieren**

In diesem Schritt verwenden Sie die in Schritt zuvor definierte Klasse "ChartJapaneseSetttings".
Codebeispiel:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.

## **Fazit**

In diesem Beispiel, wenn Sie für ein Diagramm keine japanische Region festlegen, können die folgenden Diagrammelemente in der Standardsprache gerendert werden, wie zum Beispiel Englisch.
Nach obiger Operation können wir ein Ausgabediagrammbild mit japanischer Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Achsentitelname|軸タイトル|Achsentitel|
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|
|Diagramm-Titelname|グラフ タイトル|Diagrammtitel|
|Legende Anstiegsname|ぞうか|Erhöhen|
|Legende Abnahmename|削減|Abnehmen|
|Legende Gesamtname|すべての|Gesamt|
|Andere Bezeichnung|その他|Andere|
|Serienname|シリーズ|Serie|
