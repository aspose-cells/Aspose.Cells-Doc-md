---
title: Diagramm in lokalisierte Bilddatei mit Python via .NET konvertieren
linktitle: Lokalisierten Bereich festlegen
type: docs
weight: 50
url: /de/python-net/convert-chart-to-localized-image/
alias: [/python-net/how-to-set-globalization-configuration-for-chart/]
description: Erfahren Sie, wie Sie Globalisierungskonfigurationen für Diagramme mit Aspose.Cells für Python via .NET festlegen. Konfigurieren Sie Diagramme, um mehrere Sprachen und regionale Formate für eine korrekte Anzeige von Texten, Daten und Zahlen zu unterstützen.
keywords: Aspose.Cells für Python via .NET, Diagramme, Globalisierungseinstellungen, Mehrere Sprachen, Regionale Formate, Anzeige, Text, Daten, Zahlen.
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie ein Diagramm in eine lokalisierte Bilddatei konvertieren und die lokalisierte Region für ein Diagramm festlegen.

{{% /alert %}}

## **Szenario**

Wann müssen Sie die lokalisierte Region für ein Diagramm einstellen?

Wenn Sie eine XLSX-Datei mit einem Diagramm in Excel mit spanischen Regionseinstellungen öffnen, erscheinen Elemente wie Diagrammtitel und Legende auf Spanisch. Das Speichern dieses Diagramms als Bild mit Aspose.Cells kann jedoch dazu führen, dass diese Elemente standardmäßig in Englisch verbleiben:

**![Globales Problem](GlobalIssue.png)**

Dies liegt daran, dass die Legende des Diagramms im Ausgabebild nicht mit der Excel-Lokalisierung übereinstimmt. Sie können dies beheben, indem Sie die Lokalisierungseinstellungen des Diagramms konfigurieren.

## **Unterstützte Elemente**

Die folgenden Diagrammelemente werden entsprechend Ihren Lokalisierungseinstellungen angezeigt:

| **Unterstützte Elemente**      | **Standardwert (Englisch)**       |
|-----------------------------|-----------------------------------|
| Achsentitelname             | Achsentitel                        |
| Achteenheitname             | Hundert, Tausend...                |
| Diagrammtitelname            | Diagrammtitel                     |
| Legend anstieg Name          | Steigung                          |
| Legend rückgang Name          | Rückgang                          |
| Legend Gesamtname            | Gesamt                            |
| Anderer Name                  | Andere                            |
| Serienname                    | Serie                             |

