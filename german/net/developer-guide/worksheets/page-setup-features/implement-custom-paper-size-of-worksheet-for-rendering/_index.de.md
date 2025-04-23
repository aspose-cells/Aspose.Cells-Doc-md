---
title: Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren
type: docs
weight: 70
url: /de/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: In diesem Artikel wird erklärt, wie Sie den C# API oder .NET Bibliothekscode verwenden können, um benutzerdefinierte Papiergröße für Ihre gewünschten Arbeitsblätter festzulegen, wenn Sie Excel Dateien programmgesteuert in das PDF Dateiformat rendern.
keywords: Benutzerdefinierte Papiergröße beim Rendern von Excel in PDF in C# festlegen
---

## **Mögliche Verwendungsszenarien**

Es gibt keine direkte Option zum Erstellen benutzerdefinierter Papiergrößen in MS Excel, jedoch können Sie die benutzerdefinierte Papiergröße Ihrer gewünschten Arbeitsblätter festlegen, wenn Sie Excel-Dateien in das PDF-Dateiformat rendern. In diesem Dokument wird erläutert, wie Sie die benutzerdefinierte Papiergröße eines Arbeitsblatts mithilfe der Aspose.Cells-APIs festlegen können.

## **Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren**

Aspose.Cells ermöglicht es Ihnen, die gewünschte Papiergröße des Arbeitsblatts zu implementieren. Sie können die [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize)-Methode der [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse verwenden, um eine benutzerdefinierte Seitengröße festzulegen. Der folgende Beispielscode veranschaulicht, wie Sie eine benutzerdefinierte Papiergröße für das erste Arbeitsblatt in der Arbeitsmappe festlegen. Bitte sehen Sie auch das [ausgegebene PDF](45056028.pdf) mit dem folgenden Code zur Referenz.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
