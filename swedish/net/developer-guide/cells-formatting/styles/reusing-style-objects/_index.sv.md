---
title: Återanvända stilobjekt
description: Aspose.Cells for .NET, genom att skapa och använda återanvändbara stilobjekt, kan du förenkla stilhantering och förbättra kodeffektiviteten. Vår guide hjälper dig att utnyttja fördelarna med återanvändbara stilobjekt och implementera dem i din applikation.
keywords: Aspose.Cells for .NET, Reusing Style Objects, Style Management, Code Efficiency, Reusable Styles, Application Development, API Reference, Example Code, Download, Support.
type: docs
weight: 3000
url: /sv/net/reusing-style-objects/
---
{{% alert color="primary" %}}

Att återanvända stilobjekt kan spara minne och göra ett program snabbare.

{{% /alert %}}

Så här tillämpar du viss formatering på ett stort antal celler i ett kalkylblad:

1. Skapa ett stilobjekt.
1. Ange attributen.
1. Använd stilen på cellerna i intervallet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

 Eftersom den[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) metoden använder mycket mindre minne och är effektiv, den äldre Cell.Style-egenskapen som förbrukade mycket onödigt minne togs bort när Aspose.Cells 7.1.0 släpptes.

{{% /alert %}}
