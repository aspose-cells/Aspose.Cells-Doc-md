---
title: Ränder einstellen
type: docs
weight: 20
url: /de/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells unterstützt die Seiteneinrichtungsoptionen von Microsoft Excel vollständig. Entwickler müssen möglicherweise Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. In diesem Thema wird erläutert, wie Sie Aspose.Cells verwenden, um Seitenränder zu konfigurieren.

{{% /alert %}}

## **Ränder einstellen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält die[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse bietet die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) -Eigenschaft zum Festlegen der Seiteneinrichtungsoptionen für ein Arbeitsblatt. Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Attribut ist ein Objekt der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klasse, die es Entwicklern ermöglicht, verschiedene Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt festzulegen. Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)Die Klasse stellt verschiedene Eigenschaften und Methoden bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet werden.

### **Seitenränder**

 Stellen Sie die Seitenränder (links, rechts, oben, unten) mit ein[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)Klassenmitglieder. Nachfolgend sind einige der Methoden aufgeführt, die zum Festlegen von Seitenrändern verwendet werden:

- [**Linker Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Rechter Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Oberer Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Unterer Rand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Auf Seite zentrieren**

Es ist möglich, etwas auf einer Seite horizontal und vertikal zu zentrieren. Dafür gibt es einige nützliche Mitglieder der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klasse,[**Horizontal zentrieren**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) und[**Vertikal zentrieren**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Kopf- und Fußzeilenränder**

 Stellen Sie die Kopf- und Fußzeilenränder mit ein[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) Klassenmitglieder wie z[**Kopfzeilenrand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) und[**Fußzeilenrand**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
