---
title: Seitenränder einrichten
type: docs
weight: 20
url: /de/python-net/setting-margins/
description: In diesem Artikel erfahren Sie, wie Sie die Ränder eines Excel Arbeitsblatts mithilfe von Beispielcode einstellen können. Sie lernen auch, wie Sie die Ränder für die Seitenmitte, die Kopf und Fußzeilenränder des Seiten Setups mithilfe der Aspose.Cells für Python via .NET API programmgesteuert einstellen können.
keywords: Python Excel Bibliothek, Excel Arbeitsblattrand in der Mitte einstellen, Arbeitsblattkopf und fußzeilenrand mit Python einstellen.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET unterstützt Microsoft Excels Seiteneinrichtungsoptionen vollständig. Entwickler müssen möglicherweise Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. In diesem Thema wird erläutert, wie man Aspose.Cells für Python via .NET verwendet, um Seitenränder zu konfigurieren.

{{% /alert %}}

## **Wie man Ränder einstellt**

Aspose.Cells für Python via .NET stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält die [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt die Eigenschaft [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) bereit, die zur Festlegung der Seiteneinrichtungsoptionen für ein Arbeitsblatt verwendet wird. Das Attribut [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) ist ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), das Entwicklern ermöglicht, verschiedene Seiteneinrichtungsoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) stellt verschiedene Eigenschaften und Methoden zur Verfügung, um Seiteneinrichtungsoptionen festzulegen.

## **Wie man Seitenränder einstellt**

Setzen Sie Seitenränder (links, rechts, oben, unten) mithilfe der Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Im Folgenden sind einige der Methoden aufgeführt, die zur Festlegung von Seitenrändern verwendet werden:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Wie man in der Mitte der Seite zentriert**

Es ist möglich, etwas horizontal und vertikal auf einer Seite zu zentrieren. Dafür gibt es einige nützliche Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) und [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Wie man Kopf- und Fußzeilenränder einstellt**

Legen Sie Kopf- und Fußzeilenränder mit den Membern der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fest, wie beispielsweise [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) und [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
