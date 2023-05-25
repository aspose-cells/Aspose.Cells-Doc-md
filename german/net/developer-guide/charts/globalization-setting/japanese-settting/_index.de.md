---
title: Konvertieren Sie das Diagramm in ein Bild für die japanische Region
linktitle: Legen Sie die japanische Region fest
type: docs
weight: 10
url: /de/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie die japanische Region für ein Diagramm festlegen.

{{% /alert %}}

##  **Definiert eine Vererbungsklasse**

 Im ersten Schritt müssen Sie eine Klasse „ChartJapaneseSetttings“ definieren, von der geerbt wird[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Anschließend können Sie durch Umschreiben der zugehörigen Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.
Codebeispiel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Konfigurieren Sie die japanische Einstellung für das Diagramm**

In diesem Schritt verwenden Sie die Klasse „ChartJapaneseSetttings“, die Sie im vorherigen Schritt definiert haben.
Codebeispiel:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden entsprechend Ihren Einstellungen gerendert.

##  **Abschluss**

Wenn Sie in diesem Beispiel nicht die japanische Region für ein Diagramm festlegen, werden die folgenden Diagrammelemente möglicherweise in der Standardsprache, z. B. Englisch, gerendert.
Nach dem obigen Vorgang können wir ein Ausgabediagrammbild mit der japanischen Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Name des Achsentitels|軸タイトル|Achsentitel|
|Name der Achseneinheit|百,千...|Hunderte, Tausende...|
|Name des Diagrammtitels|グラフ タイトル|Diagrammtitel|
|Legende: Name erhöhen|ぞうか|Zunahme|
|Name der Legende verringern|削減|Verringern|
|Gesamtname der Legende|すべての|Gesamt|
|Anderer Name|その他|Andere|
|Serienname|シリーズ|Serie|
