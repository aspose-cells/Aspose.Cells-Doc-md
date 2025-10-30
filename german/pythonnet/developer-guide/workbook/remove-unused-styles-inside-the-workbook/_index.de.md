---
title: Entfernen Sie unbenutzte Stile innerhalb der Arbeitsmappe
type: docs
weight: 340
url: /de/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Ungenutzte Styles in der Excel-Datei nehmen nicht nur Platz ein, sondern verursachen auch Leistungsprobleme beim Konvertieren in verschiedene Formate wie PDF, HTML usw. Aspose.Cells for Python via .NET bietet die [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles)-Methode, um alle ungenutzten Styles im Arbeitsbuch zu entfernen.

{{% /alert %}}

Der folgende Code erläutert die Verwendung von [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). Der Code lädt die [Vorlagen-Excel-Datei](5115520.xlsx), die Sie über den bereitgestellten Link herunterladen können. Sie enthält einen unbenutzten Stil namens **AsposeStyle**. Dieser Stil und alle anderen unbenutzten Stile werden nach Ausführung des Codes entfernt.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
