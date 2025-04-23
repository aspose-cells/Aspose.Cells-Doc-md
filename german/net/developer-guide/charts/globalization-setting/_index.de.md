---
title: Diagramm in lokalisiertes Bild konvertieren
description: Erfahren Sie, wie Sie Globalisierungskonfigurationen für Diagramme mithilfe von Aspose.Cells for .NET setzen können. Unser Leitfaden zeigt, wie Sie das Diagramm so konfigurieren, dass es multiple Sprachen und regionale Formate unterstützt, um Text, Datum und Zahlen in verschiedenen Sprachen korrekt anzuzeigen.
keywords: Aspose.Cells for .NET, Diagramme, Globalisierungseinstellungen, Mehrere Sprachen, Regionale Formate, Anzeige, Text, Daten, Zahlen.
linktitle: Lokalisierten Bereich festlegen
type: docs
weight: 50
url: /de/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie ein Diagramm in ein lokalisiertes Bild umwandeln können. Sie erfahren, wie Sie einen lokalisierten Bereich für ein Diagramm festlegen können.

{{% /alert %}}

## **Szenario**

In welchem Szenario müssen wir einen lokalisierten Bereich für ein Diagramm festlegen? 

Wenn Sie eine xlsx-Datei mit einem Diagramm in Excel öffnen, und in diesem Fall angenommen wird sie mit spanischer regionaler Einstellung in Excel geöffnet, sehen Sie die Elemente im Diagrammbereich, wie den Diagrammtitel, die Legende, sie sind ins Spanische übersetzt. Aber wenn Sie dieses Diagramm als Bild mit Aspose.Cells speichern, können Sie auf folgendes Problem stoßen: 

**![Globales Problem](GlobalIssue.png)**

In diesem Szenario werden die Elemente der Diagrammlegende im Ausgabebild nicht gleich wie in Excel dargestellt, sie bleiben standardmäßig in Englisch angezeigt. Jetzt können Sie dieses Problem lösen, indem Sie einen lokalisierten Bereich für das Diagramm festlegen. Mit den richtigen Einstellungen werden die folgenden Elemente gemäß Ihren Lokalisierungseinstellungen gerendert.

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

Das folgende Beispiel wird Ihnen im Detail zeigen, wie Sie eine lokalisierte Region festlegen, um den gewünschten Effekt zu erzielen.

- [Wie man die chinesische Region für das Diagramm einstellt](/cells/de/net/convert-chart-to-image-for-chinese-region/)
- [Wie man die japanische Region für das Diagramm einstellt](/cells/de/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
