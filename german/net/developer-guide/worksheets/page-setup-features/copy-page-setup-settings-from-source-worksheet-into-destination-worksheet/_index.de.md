---
title: Kopieren von Seiteneinrichtungseinstellungen vom Quellarbeitsblatt in das Zielarbeitsblatt
type: docs
weight: 80
url: /de/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: In diesem Artikel wird erläutert, wie der C# API oder .NET Bibliotheksbeispielcode verwendet wird, um die Seiteneinrichtungseinstellungen vom Quellarbeitsblatt in das Zielarbeitsblatt programmgesteuert zu kopieren.
keywords: Seitenlayouteinstellungen in c# kopieren, Seitenlayouteinstellungen auf Zielseitenblatt in c# kopieren
---

## **Mögliche Verwendungsszenarien**

Wenn Sie ein neues Blatt zu einer Arbeitsmappe hinzufügen, enthält es die Standard-*Seiteneinrichtungseinstellungen*. Es kann vorkommen, dass Sie die Einstellungen ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) von einem Arbeitsblatt auf ein anderes Arbeitsblatt übertragen müssen. In diesem Dokument wird erläutert, wie die Seiteneinrichtungseinstellungen von einem Arbeitsblatt auf ein anderes mithilfe der Aspose.Cells-APIs kopiert werden.

## **Seiteneinrichtungseinstellungen von der Quellarbeitsmappe in die Zieltabelle kopieren**

Der folgende Beispielcode veranschaulicht, wie die *Seiteneinrichtungseinstellungen* von einem Arbeitsblatt auf ein anderes mithilfe der Methode [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy) kopiert werden. Bitte beachten Sie den folgenden Beispielcode und dessen Konsolenausgabe als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
