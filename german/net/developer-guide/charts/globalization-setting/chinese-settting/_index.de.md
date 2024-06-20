---
title: Diagramm in Bild für die chinesische Region umwandeln
description: Lernen Sie, wie Sie Aspose.Cells for .NET chinesische Konfigurationen für Diagramme verwenden. Unsere Anleitung zeigt, wie Diagramme konfiguriert werden können, um chinesische Zeichen und Formate zu unterstützen, einschließlich Schriftarten, Größen, Textrichtungen und mehr.
keywords: Aspose.Cells for .NET, Diagramme, Chinesische Konfiguration, Schriftarten, Schriftgröße, Textrichtung, Unterstützung.
linktitle: Chinesische Region festlegen
type: docs
weight: 9
url: /de/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie eine chinesische Region für ein Diagramm festlegen können.

{{% /alert %}}

## **Definiert eine Vererbungsklasse**

Als erstes müssen Sie eine Klasse "ChartChineseSetttings" definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) geerbt. 
Dann können Sie durch Neudefinition der entsprechenden Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache festlegen.
Codebeispiel:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Konfigurieren Sie die chinesischen Einstellungen für das Diagramm**

In diesem Schritt verwenden Sie die Klasse "ChartChineseSetttings", die Sie im vorherigen Schritt definiert haben.
Codebeispiel:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.

## **Fazit**

In diesem Beispiel, wenn Sie keine chinesische Region für ein Diagramm festlegen, werden die folgenden Diagrammelemente möglicherweise in der Standardsprache, wie Englisch, gerendert.
Nach der oben genannten Operation können wir ein Ausgabediagrammbild mit chinesischer Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Axis Title Name|坐标轴标题|Achsentitel|
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|
|Chart Title Name|图表标题|Diagrammtitel|
|Legend Increase Name|增加|Zunahme|
|Legend Decrease Name|减少|Rückgang|
|Legend Total Name|汇总|Gesamt|
|Other Name|其他|Sonstige|
|Series Name|系列|Serie|
