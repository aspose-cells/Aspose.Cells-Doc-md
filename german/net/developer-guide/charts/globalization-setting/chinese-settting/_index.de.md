---
title: Konvertieren Sie das Diagramm in ein Bild für die chinesische Region
linktitle: Stellen Sie die chinesische Region ein
type: docs
weight: 9
url: /de/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie die chinesische Region für ein Diagramm festlegen.

{{% /alert %}}

##  **Definiert eine Vererbungsklasse**

Im ersten Schritt müssen Sie eine Klasse „ChartChineseSetttings“ definieren, von der geerbt wird[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Anschließend können Sie durch Umschreiben der zugehörigen Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.
Codebeispiel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Chinesische Einstellung für Diagramm konfigurieren**

In diesem Schritt verwenden Sie die Klasse „ChartChineseSetttings“, die Sie im vorherigen Schritt definiert haben.
Codebeispiel:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden entsprechend Ihren Einstellungen gerendert.

##  **Abschluss**

Wenn Sie in diesem Beispiel nicht die chinesische Region für ein Diagramm festlegen, werden die folgenden Diagrammelemente möglicherweise in der Standardsprache, z. B. Englisch, gerendert.
Nach dem obigen Vorgang können wir ein Ausgabediagrammbild mit der chinesischen Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Name des Achsentitels|坐标轴标题|Achsentitel|
|Name der Achseneinheit|百,千...|Hunderte, Tausende...|
|Name des Diagrammtitels|图表标题|Diagrammtitel|
|Legende: Name erhöhen|增加|Zunahme|
|Name der Legende verringern|减少|Verringern|
|Gesamtname der Legende|汇总|Gesamt|
|Anderer Name|其他|Andere|
|Serienname|系列|Serie|
