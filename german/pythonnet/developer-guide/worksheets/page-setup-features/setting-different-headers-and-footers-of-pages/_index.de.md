---
title: Setzen von verschiedenen Kopf und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Dieses Beispiel zeigt, wie man mithilfe der Aspose.Cells für Python API verschiedene Kopf und Fußzeileneinstellungen des Seiten Setups des Excel Arbeitsblatts programmatisch festlegen kann. Sie können die Kopf und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten einstellen.
keywords: Python Excel Bibliothek, Python, Kopf und Fußzeile der ersten Seite festlegen, Kopf und Fußzeile ungerader Seiten in Python setzen, Kopf und Fußzeile gerader Seiten in Python festlegen.
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
Aspose.Cells für Python via .NET unterstützt dieselbe Funktion.

{{% /alert %}}

## **So legen Sie unterschiedliche Kopf- und Fußzeilen in MS Excel fest**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Markieren Sie **Unterschiedliche Kopf- und Fußzeilen auf geraden und ungeraden Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## **So legen Sie unterschiedliche Kopf- und Fußzeilen mit Aspose.Cells für Python Excel-Bibliothek fest**

Aspose.Cells für Python via .NET verhält sich wie Excel.
1. Aktiviert die Flags [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) und [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
