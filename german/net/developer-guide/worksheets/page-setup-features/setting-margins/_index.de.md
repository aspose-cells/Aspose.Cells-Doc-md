---
title: Ränder festlegen
type: docs
weight: 20
url: /de/net/setting-margins/
description: In diesem Artikel erfahren Sie, wie Sie mithilfe von Beispielcode die Ränder eines Excel-Arbeitsblatts festlegen. Sie erfahren außerdem, wie Sie mithilfe der Bibliothek C#, API oder .NET die Ränder für die Seitenmitte sowie die Kopf- und Fußzeilenränder der Seiteneinrichtung programmgesteuert festlegen.
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Seiteneinrichtungsoptionen von Microsoft Excel vollständig. Entwickler müssen möglicherweise Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckvorgang zu steuern. In diesem Thema wird erläutert, wie Sie Aspose.Cells zum Konfigurieren von Seitenrändern verwenden.

{{% /alert %}}

##  **Ränder festlegen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält die[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

 Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Eigenschaft, die zum Festlegen der Seiteneinrichtungsoptionen für ein Arbeitsblatt verwendet wird. Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Attribut ist ein Objekt von[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klasse, die es Entwicklern ermöglicht, verschiedene Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt festzulegen. Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)Die Klasse stellt verschiedene Eigenschaften und Methoden zum Festlegen von Seiteneinrichtungsoptionen bereit.

###  **Seitenränder**

 Legen Sie die Seitenränder fest (links, rechts, oben, unten) mit[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)Klassenmitglieder. Nachfolgend sind einige der Methoden aufgeführt, die zum Festlegen von Seitenrändern verwendet werden:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Oberer Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Unterer Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

###  **Auf Seite zentrieren**

 Es ist möglich, etwas horizontal und vertikal auf einer Seite zu zentrieren. Dafür gibt es einige nützliche Mitglieder der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klasse,[**MitteHorizontal**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) Und[**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

###  **Kopf- und Fußzeilenränder**

 Legen Sie die Ränder von Kopf- und Fußzeilen mit fest[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klassenmitglieder wie[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) Und[**Fußzeilenrand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
