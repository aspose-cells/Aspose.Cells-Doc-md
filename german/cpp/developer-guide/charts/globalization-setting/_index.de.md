---
title: Diagramm in eine lokalisierte Bilddatei mit C++ konvertieren
description: Erfahren Sie, wie Sie Globalisierungskonfigurationen für Diagramme mit Aspose.Cells for C++ festlegen. Unser Leitfaden zeigt, wie Sie das Diagramm so konfigurieren, dass es mehrere Sprachen und regionale Formate unterstützt, um Text, Daten und Zahlen in verschiedenen Sprachen korrekt anzuzeigen.
keywords: Aspose.Cells for C++, Diagramme, Globalisierungseinstellungen, Mehrsprachigkeit, Regionale Formate, Anzeige, Text, Daten, Zahlen.
linktitle: Lokalisierten Bereich festlegen
type: docs
weight: 50
url: /de/cpp/convert-chart-to-localized-image/
alias: [/cpp/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie ein Diagramm in ein lokalisiertes Bild umwandeln können. Sie erfahren, wie Sie einen lokalisierten Bereich für ein Diagramm festlegen können.

{{% /alert %}}

## **Szenario**

In welcher Situation müssten wir eine lokalisierten Region für ein Diagramm festlegen?

Wenn Sie eine xlsx-Datei mit einem Diagramm in Excel öffnen, beispielsweise mit einer spanischen Regionaleinstellung, können Sie die Elemente im Diagrammbereich wie Diagrammtitel und Legende ins Spanische übersetzt sehen. Wenn Sie dieses Diagramm jedoch mit Aspose.Cells als Bild speichern, kann es zu folgendem Problem kommen: 

**![Globales Problem](GlobalIssue.png)**

In diesem Szenario ist die Diagrammlegende im Ausgabebild nicht dieselbe wie in Excel; sie wird standardmäßig in Englisch angezeigt. Sie können dieses Problem lösen, indem Sie die lokalisierten Regionseinstellungen für das Diagramm festlegen. Mit den richtigen Einstellungen werden die folgenden Elemente entsprechend Ihren Lokalisierungseinstellungen gerendert.

## **Unterstützte Elemente**

Die folgenden Elemente im Diagramm können entsprechend Ihren Lokalisierungseinstellungen gerendert werden.

|**Unterstützte Elemente**|**Standardwert in der englischen Umgebung**|
| :- | :- |
|Achsentiteln Name|Achsentitel|
|Achsenwert-Name|Hunderter, Tausender...|
|Diagrammtitel-Name|Diagrammtitel|
|Legende Zunahme-Name|Zunahme|
|Legende Abnahme-Name|Abnahme|
|Legende Gesamt-Name|Gesamt|
|Andere Name|Andere|
|Serienname|Serien|

## **Betriebsschritte**

Das folgende Beispiel zeigt im Detail, wie Sie eine lokalisierte Region einstellen, um den gewünschten Effekt zu erzielen.

- [Wie man die chinesische Region für das Diagramm einstellt](/cells/de/cpp/convert-chart-to-image-for-chinese-region/)
- [Wie man die japanische Region für das Diagramm einstellt](/cells/de/cpp/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="cpp" >}}
