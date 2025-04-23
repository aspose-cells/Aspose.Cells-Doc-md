---
title: Återanvända stilobjekt
description: I Aspose.Cells for .NET kan du genom att skapa och använda återanvändbara stilobjekt förenkla stilhantering och förbättra kodens effektivitet. Vår guide kommer att hjälpa dig dra fördel av fördelarna med återanvändbara stilobjekt och implementera dem i din applikation.
keywords: Aspose.Cells for .NET, Återanvända stilobjekt, Stilhantering, Kodseffektivitet, Återanvändbara stilar, Applikationsutveckling, API referens, Exempelkod, Hämta, Support.
type: docs
weight: 3000
url: /sv/net/reusing-style-objects/
---

{{% alert color="primary" %}}

Att återanvända stilobjekt kan spara minne och göra ett program snabbare.

{{% /alert %}}

För att tillämpa viss formatering på en stor omfattning av celler i en arbetsbok:

1. Skapa en stilobjekt.
1. Ange attributen.
1. Tillämpa stilen på cellerna i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ReusingStyleObjects-ReusingStyleObjects.cs" >}}

{{% alert color="primary" %}}

Eftersom tillvägagångssättet [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle)/[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) använder mycket mindre minne och är effektivt, togs den äldre Cell.Style-egenskapen bort med versionen Aspose.Cells 7.1.0, vilken använde mycket onödigt minne.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
