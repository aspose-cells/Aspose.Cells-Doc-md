---
title: Diagramm in Bild umwandeln für die chinesische Region mit Golang über C++
linktitle: Chinesische Region festlegen
description: Erfahren Sie, wie Sie Aspose.Cells for C++ verwenden, um die chinesische Konfiguration für Diagramme einzustellen. Unser Leitfaden zeigt, wie man Diagramme so konfiguriert, dass sie chinesische Zeichen und Formate unterstützen, einschließlich Schriftarten, Größen, Textausrichtungen und mehr.
keywords: Aspose.Cells for C++, Diagramme, Chinesische Konfiguration, Schriftarten, Schriftgrößen, Textausrichtung, Unterstützung.
type: docs
weight: 9
url: /de/go-cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie eine chinesische Region für ein Diagramm festlegen können.

{{% /alert %}}

## **Definiert eine Vererbungsklasse**

Der erste Schritt besteht darin, eine Klasse "ChartChineseSetttings" zu definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) erbt. 
Anschließend können Sie durch Überschreiben der zugehörigen Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache einstellen.

Codebeispiel:
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChineseSettting.go" >}}
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
