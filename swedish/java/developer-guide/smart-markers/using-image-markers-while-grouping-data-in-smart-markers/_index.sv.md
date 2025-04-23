---
title: Använda bildenkoder vid gruppering av data i Smart Markers
type: docs
weight: 630
url: /sv/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Denna artikel presenterar ett exempel som illustrerar användningen av bildkoder vid gruppering av data i smart markörer.

{{% /alert %}} 
## **Använda bildenkoder vid gruppering av data i Smart Markers**
Följande kodexempel skapar en arbetsbok och lägger sedan till de följande smarternamnstaggarna i cellerna D2, E2 och F2 respektive.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Sedan fyller den datakällan med data och anropar [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) metoden för att bearbeta smartmerkretiketter. Koden använder dessa bilder t.ex [moon.png](5472549.png) och [moon2.png](5472548.png) men du kan använda vilken bild som helst. Nedanstående skärmbild visar utdata av denna kod. Som du kan se är data i kolumn E och F grupperad med avseende på data i kolumn D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
