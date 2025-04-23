---
title: Seitenränder einrichten
type: docs
weight: 20
url: /de/python-net/setting-margins/
description: In diesem Artikel lernen Sie, wie Sie die Ränder eines Excel Arbeitsblatts mit Beispiellcode einstellen. Außerdem erfahren Sie, wie Sie die Ränder für die Seitenmitte, den Kopf und Fußzeilenabstand des Page Setups programmgesteuert mit der Aspose.Cells for Python via .NET API festlegen.
keywords: Python Excel Bibliothek, Python Ränder des Excel Arbeitsblatts zentrieren, Ränder für Kopf und Fußzeilen mit Python einstellen.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET unterstützt vollständig die Seiten-Setup-Optionen von Microsoft Excel. Entwickler müssen möglicherweise die Seiteneinrichtungs-Einstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. Dieses Thema erläutert, wie man Aspose.Cells for Python via .NET nutzt, um Seitenränder zu konfigurieren.

{{% /alert %}}

## **Seitliche Ränder festlegen**

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält die Sammlung [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) dargestellt.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) stellt die Eigenschaft [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) bereit, die zur Festlegung der Seiteneinrichtungsoptionen für ein Arbeitsblatt verwendet wird. Das Attribut [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) ist ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), das Entwicklern ermöglicht, verschiedene Seiteneinrichtungsoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) stellt verschiedene Eigenschaften und Methoden zur Verfügung, um Seiteneinrichtungsoptionen festzulegen.

## **Seitenränder einstellen**

Setzen Sie Seitenränder (links, rechts, oben, unten) mithilfe der Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Im Folgenden sind einige der Methoden aufgeführt, die zur Festlegung von Seitenrändern verwendet werden:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Auf Seite zentrieren**

Es ist möglich, etwas horizontal und vertikal auf einer Seite zu zentrieren. Dafür gibt es einige nützliche Member der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) und [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Kopf- und Fußzeilenränder festlegen**

Legen Sie Kopf- und Fußzeilenränder mit den Membern der Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fest, wie beispielsweise [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) und [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
