---
title: Setzen von verschiedenen Kopf und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: In diesem Artikel finden Sie Beispielcode, der zeigt, wie Sie verschiedene Kopf und Fußzeilen der Excel Arbeitsblatt Page Setup Einstellungen programmatisch mit der C# Bibliothek und der .NET API einstellen können. Sie können die Kopf und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten festlegen.
keywords: Excel Kopf und Fußzeile der ersten Seite festlegen c#, Excel Kopf und Fußzeile der ungeraden Seiten festlegen c#, Excel Kopf und Fußzeile der geraden Seiten festlegen c#
---

{{% alert color="primary" %}}

MS Excel unterstützt das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten seit Excel 2007.
Aspose.Cells unterstützt dieselbe Funktion.

{{% /alert %}}

## **Setzen verschiedener Kopf- und Fußzeilen in MS Excel**

**![Setzen verschiedener Kopf- und Fußzeilen](difpage.png)**

1. Klicken Sie auf **Seitenlayout > Drucktitel > Kopf-/Fußzeile**.
1. Markieren Sie **Unterschiedliche Kopf- und Fußzeilen auf geraden und ungeraden Seiten** oder **Unterschiedliche erste Seite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## **Setzen von verschiedenen Kopf- und Fußzeilen mit Aspose.Cells**

Aspose.Cells verhält sich genauso wie Excel.
1. Setzt die Flags [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) und [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
