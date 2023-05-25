---
title: Kopieren Sie die Seiteneinrichtungseinstellungen vom Quellarbeitsblatt in das Zielarbeitsblatt
type: docs
weight: 80
url: /de/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: In diesem Artikel wird erläutert, wie Sie den Beispielcode der Bibliothek C#, API oder .NET verwenden, um Seiteneinrichtungseinstellungen programmgesteuert aus dem Quellarbeitsblatt in das Zielarbeitsblatt zu kopieren.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Mögliche Nutzungsszenarien**

Wenn Sie einer Arbeitsmappe ein neues Blatt hinzufügen, enthält es die standardmäßigen *Seiteneinrichtungseinstellungen*. Es kann vorkommen, dass Sie die Einstellungen übertragen müssen ([**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) von einem Arbeitsblatt zum anderen Arbeitsblatt. In diesem Dokument wird erläutert, wie Sie mithilfe von Aspose.Cells-APIs Seiteneinrichtungseinstellungen von einem Arbeitsblatt in ein anderes kopieren.

##  **Kopieren Sie die Seiteneinrichtungseinstellungen vom Quellarbeitsblatt in das Zielarbeitsblatt**

Der folgende Beispielcode veranschaulicht das Kopieren*Einstellungen für die Seiteneinrichtung*von einem Arbeitsblatt zum anderen mit[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)Methode. Als Referenz sehen Sie sich bitte den folgenden Beispielcode und seine Konsolenausgabe an.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
