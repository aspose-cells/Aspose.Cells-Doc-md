---
title: Använda bildmarkörer samtidigt som data grupperas i smarta markörer
type: docs
weight: 630
url: /sv/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Den här artikeln presenterar ett exempel som illustrerar användningen av bildmarkörer medan data grupperas i smarta markörer.

{{% /alert %}} 
## **Använda bildmarkörer samtidigt som data grupperas i smarta markörer**
Följande exempelkod skapar en arbetsbok och lägger sedan till följande smarta markörtaggar i cellerna D2, E2 respektive F2.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Sedan fyller den datakällan med data och anropar[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) metod för att bearbeta smarta markörtaggar. Koden använder dessa bilder dvs[moon.png](5472549.png) och[moon2.png](5472548.png) men du kan använda vilken bild som helst. Följande skärmdump visar utdata från denna exempelkod. Som du kan se är data i kolumn E och F grupperade med avseende på data i kolumn D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
