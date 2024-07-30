---
title: Setzen von verschiedenen Kopf und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Dieser Artikel enthält Beispielscode, der zeigt, wie Sie mit der Aspose.Cells für Python API die verschiedenen Kopf und Fußzeilen der Excel Arbeitsblattseiteneinrichtungseinstellungen programmgesteuert setzen können. Sie können die Kopfzeilen und Fußzeilen für die erste Seite, die ungeraden Seiten und die geraden Seiten festlegen.
keywords: Python Excel Bibliothek, Setzen Sie den Excel Kopf und Fußzeilenheader für die erste Seite, legen Sie den Excel Kopf und Fußzeilenheader für ungerade Seiten in Python fest, legen Sie den Excel Kopf und Fußzeilenheader für gerade Seiten in Python fest.
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
Aspose.Cells für Python via .NET unterstützt dieselbe Funktion.

{{% /alert %}}

## **Wie man verschiedene Kopf- und Fußzeilen in MS Excel einstellt**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Markieren Sie **Unterschiedliche Kopf- und Fußzeilen auf geraden und ungeraden Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## **Wie man verschiedene Kopf- und Fußzeilen mit der Aspose.Cells für Python Excel-Bibliothek einstellt**

Aspose.Cells für Python via .NET verhält sich genauso wie Excel.
1. Setzt die Flags [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) und [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
