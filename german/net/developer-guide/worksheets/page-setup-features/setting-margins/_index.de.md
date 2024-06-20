---
title: Seitenränder einrichten
type: docs
weight: 20
url: /de/net/setting-margins/
description: In diesem Artikel erfahren Sie, wie Sie die Ränder eines Excel Arbeitsblatts mithilfe von Beispielcode einrichten. Außerdem lernen Sie, wie Sie mithilfe der C# API oder der .NET Bibliothek programmgesteuert die Ränder für die Seitenmitte sowie die Kopf und Fußzeilenränder für das Seitenlayout einstellen.
keywords: Excel Arbeitsblattrand auf Mitte einstellen C#, Arbeitsblatt Kopf und Fußzeilenrand einstellen C#
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt vollständig die Seiteneinrichtungsoptionen von Microsoft Excel. Entwickler müssen möglicherweise die Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. Dieses Thema erläutert, wie Sie Aspose.Cells verwenden, um die Seitennränder zu konfigurieren.

{{% /alert %}}

## **Ränder einstellen**

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), bereit, die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält die Sammlung [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) stellt die Eigenschaft [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) bereit, die zur Festlegung der Seiteneinrichtungsoptionen für ein Arbeitsblatt verwendet wird. Das Attribut [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) ist ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), das Entwicklern ermöglicht, verschiedene Seiteneinrichtungsoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) stellt verschiedene Eigenschaften und Methoden zur Verfügung, um Seiteneinrichtungsoptionen festzulegen.

### **Seitenränder**

Setzen Sie Seitenränder (links, rechts, oben, unten) mithilfe der Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). Im Folgenden sind einige der Methoden aufgeführt, die zur Festlegung von Seitenrändern verwendet werden:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **In der Lage zu zentrieren etwas auf einer Seite horizontal und vertikal. Die Klasse {0} hat Mitglieder zu diesem Zweck: {1} und {2}.**

Es ist möglich, etwas horizontal und vertikal auf einer Seite zu zentrieren. Dafür gibt es einige nützliche Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) und [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Kopf- und Fußzeilen Ränder**

Legen Sie Kopf- und Fußzeilenränder mit den Membern der Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) fest, wie beispielsweise [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) und [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
