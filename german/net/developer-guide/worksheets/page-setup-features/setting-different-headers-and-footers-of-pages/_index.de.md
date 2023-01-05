---
title: Festlegen verschiedener Kopf- und Fußzeilen für verschiedene Seiten
type: docs
weight: 35
url: /de/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel unterstützt seit Excel 2007 das Festlegen unterschiedlicher Kopf- und Fußzeilen für die erste Seite, ungerade Seiten und gerade Seiten.
Aspose.Cells unterstützt dieselbe Funktion.

{{% /alert %}}

## **Unterschiedliche Kopf- und Fußzeilen in MS Excel einstellen**

**![Unterschiedliche Kopf- und Fußzeilen festlegen](difpage.png)**

1.  Klicken**Seitenlayout > Titel drucken > Kopf-/Fußzeile**.
1.  Prüfen**Verschiedene ungerade und gerade Seiten** oder**Andere Tannenseite**.
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.

## **Einstellen unterschiedlicher Kopf- und Fußzeilen mit Aspose.Cells**

Aspose.Cells verhält sich genauso wie Excel.
1.  Setzt die Flags[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) und[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Geben Sie verschiedene Kopf- und Fußzeilen ein.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
