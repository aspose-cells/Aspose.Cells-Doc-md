---
title: Konvertera diagram till bild i SVG format
type: docs
weight: 140
url: /sv/java/converting-chart-to-image-in-svg-format/
---

{{% alert color="primary" %}} 

Scalable Vector Graphics (SVG) är ett XML-baserat vektorbildformat för tvådimensionell grafik som också stöder interaktivitet och animation. SVG-specifikationen är en öppen standard som utvecklats av World Wide Web Consortium (W3C) sedan 1999.

SVG-bilder och deras beteenden definieras i XML-textfiler. Detta innebär att de kan sökas, indexeras, skriptas och komprimeras. Som XML-filer kan SVG-bilder skapas och redigeras med vilken textredigerare som helst, men skapas oftare med ritprogram.

Aspose.Cells kan spara diagram som bilder i olika format som BMP, JPEG, PNG, GIF, SVG, osv. Den här artikeln förklarar hur man sparar diagram som SVG-bilder.

{{% /alert %}} 

Följande exempelkod förklarar hur man använder Aspose.Cells för att konvertera ett diagram till en SVG-formatbild. Koden laddar den käll-Excel-filen och sparar sedan det första diagrammet som hittas på den första arbetsbladet till SVG.

Bilden nedan visar den konverterade diagrammets bild i SVG-format skapad med exempelkoden.

**Utmatningsbild** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_1.png)

Eftersom SVG är ett XML-baserat format kan du också öppna utmatningsdiagrammet i en textredigerare som Notepad som visas på skärmbilden.

**Utmatnings-SCG i en textredigerare** 

![todo:image_alt_text](converting-chart-to-image-in-svg-format_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertCharttoImageinSVGFormat-ConvertCharttoImageinSVGFormat.java" >}}
{{< app/cells/assistant language="java" >}}
