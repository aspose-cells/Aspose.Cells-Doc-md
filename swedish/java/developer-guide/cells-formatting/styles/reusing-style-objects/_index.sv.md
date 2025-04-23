---
title: Återanvända stilobjekt
type: docs
weight: 60
url: /sv/java/reusing-style-objects/
---

{{% alert color="primary" %}}

Återanvändning av stilobjekt kan spara minne och få programmet att köra snabbare.

{{% /alert %}}

För att tillämpa viss formatering på en stor omfattning av celler i en arbetsbok:

1. Skapa en stilobjekt.
1. Ange attributen.
1. Tillämpa stilen på cellerna i området.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Samma process som diskuterats ovan kan också utföras på följande sätt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

Eftersom [**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle--) och [**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell/#setStyle-com.aspose.cells.Style-) metoderna använder mycket mindre minne och är effektiva, togs den äldre egenskapen *Cell.getStyle()* bort som använde mycket onödigt minne, med versionen *Aspose.Cells 7.1.0*.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
