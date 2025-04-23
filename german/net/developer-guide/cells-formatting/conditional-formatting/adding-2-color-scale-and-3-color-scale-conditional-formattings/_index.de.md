---
title: Hinzufügen von bedingten Formates mit 2 Farbskala und 3 Farbskala
description: Wie man die Aspose.Cells Bibliothek in C# verwendet, um bedingte Formatierungen für Zwei Farben Verhältnisse und Drei Farben Verhältnisse hinzuzufügen. Durch Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Bedingte Formatierung, C#, Farbverhältnis, Zwei Farbskala, Drei Farbskala
type: docs
weight: 20
url: /de/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

**2-Farbmuster** und **3-Farbmuster** Bedingte Formatierungen werden auf die gleiche Weise hinzugefügt, außer dass sie sich durch die [**FormatCondition.ColorScale.Is3ColorScale**](https://reference.aspose.com/cells/net/aspose.cells/colorscale/properties/is3colorscale)-Eigenschaft unterscheiden. Diese Eigenschaft ist **falsch** für 2-Farbmuster und **wahr** für 3-Farbmuster Bedingte Formatierungen.

{{% /alert %}}

Der folgende Beispielcode fügt 2-Farbmuster und 3-Farbmuster Bedingte Formatierungen hinzu. Es generiert die [Ausgabedatei Excel](5115058.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-AddColorScales-AddColorScales.cs" >}}
{{< app/cells/assistant language="csharp" >}}
