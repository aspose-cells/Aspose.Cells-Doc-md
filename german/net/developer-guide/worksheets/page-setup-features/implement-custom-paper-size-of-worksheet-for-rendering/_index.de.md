---
title: Implementieren Sie eine benutzerdefinierte Papiergröße des Arbeitsblatts zum Rendern
type: docs
weight: 70
url: /de/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: In diesem Artikel wird erläutert, wie Sie den Beispielcode der Bibliothek C#, API oder .NET verwenden, um das benutzerdefinierte Papierformat Ihrer gewünschten Arbeitsblätter festzulegen, wenn Sie eine Excel-Datei programmgesteuert in das Dateiformat PDF rendern.
keywords: set custom paper size while rendering excel to pdf c#
---
##  **Mögliche Nutzungsszenarien**

Es gibt keine direkte Option zum Erstellen benutzerdefinierter Papierformate in MS Excel. Sie können jedoch beim Rendern der Excel-Datei das benutzerdefinierte Papierformat Ihrer gewünschten Arbeitsblätter auf das Dateiformat PDF festlegen. In diesem Dokument wird erläutert, wie Sie mithilfe der APIs Aspose.Cells ein benutzerdefiniertes Papierformat für ein Arbeitsblatt festlegen.

##  **Implementieren Sie eine benutzerdefinierte Papiergröße des Arbeitsblatts zum Rendern**

 Aspose.Cells ermöglicht Ihnen die Umsetzung Ihrer gewünschten Papiergröße des Arbeitsblattes. Sie können die verwenden[**BenutzerdefiniertePapiergröße**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) Methode der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse, um eine benutzerdefinierte Seitengröße anzugeben. Der folgende Beispielcode veranschaulicht, wie Sie ein benutzerdefiniertes Papierformat für das erste Arbeitsblatt in der Arbeitsmappe angeben. Bitte beachten Sie auch die[Ausgabe PDF](45056028.pdf)als Referenz mit dem folgenden Code generiert.

##  **Bildschirmfoto**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
