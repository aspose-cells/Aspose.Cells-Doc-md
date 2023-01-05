---
title: Återanvända stilobjekt
type: docs
weight: 60
url: /sv/java/reusing-style-objects/
---
{{% alert color="primary" %}}

Att återanvända stilobjekt kan spara minne och få programmet att köras snabbare.

{{% /alert %}}

Så här tillämpar du viss formatering på ett stort antal celler i ett kalkylblad:

1. Skapa ett stilobjekt.
1. Ange attributen.
1. Använd stilen på cellerna i intervallet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReuseStyleObjects-ReuseStyleObjects.java" >}}

Samma process som diskuterats ovan skulle också kunna genomföras enligt följande.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReuseStyleObjects2.java" >}}

{{% alert color="primary" %}}

 Eftersom det[**Cell.getStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle() ) och[**Cell.setStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle(com.aspose.cells.Style) ) metoder använder mycket mindre minne och är effektiva, ju äldre*Cell.getStyle()* egendom som förbrukade mycket onödigt minne, togs bort när den släpptes*Aspose.Cells 7.1.0*.

{{% /alert %}}
