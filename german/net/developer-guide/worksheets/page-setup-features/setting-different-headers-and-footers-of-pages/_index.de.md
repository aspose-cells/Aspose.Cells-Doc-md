---
title: Festlegen verschiedener Kopf- und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Dieser Artikel enthält Beispielcode, der zeigt, wie Sie mithilfe der Bibliothek C# und .NET API verschiedene Kopf- und Fußzeilen der Seiteneinrichtungseinstellungen für Excel-Arbeitsblätter programmgesteuert festlegen. Sie können die Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten festlegen.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel unterstützt seit Excel 2007 das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten.
Aspose.Cells unterstützt die gleiche Funktion.

{{% /alert %}}

##  **Festlegen unterschiedlicher Kopf- und Fußzeilen in MS Excel**

**![Unterschiedliche Kopf- und Fußzeilen festlegen](difpage.png)**

1. Klicken Sie auf *Seitenlayout > Titel drucken > Kopf-/Fußzeile**.
1.  Überprüfen**Verschiedene ungerade und gerade Seiten** oder *Andere Tannenseite**.
1. Geben Sie unterschiedliche Kopf- und Fußzeilen ein.

##  **Mit Aspose.Cells unterschiedliche Kopf- und Fußzeilen festlegen**

Aspose.Cells verhält sich genauso wie Excel.
1.  Setzt die Flags[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) Und[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Geben Sie unterschiedliche Kopf- und Fußzeilen ein.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
