---
title: Kontroller i diagram
linktitle: Former i diagram
type: docs
weight: 60
url: /sv/java/controls-in-charts/
---

{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontroller i ett diagram vid körtid.

{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användarna om innehållet i ett kalkylblad. Aspose.Cells låter dig lägga till och manipulera etiketter även i diagram.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) tillhandahåller en metod som kallas [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-), används för att lägga till en etikettkontroll till ett diagram. Nedan är en lista över parametrarna som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter av 1/4000 av diagramområdet.

Metoden returnerar ett objekt av klassen [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label), där klassen [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) representerar en etikett i diagrammet. Den har några viktiga medlemmar som detaljeras nedan:

- Egenskapen [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) anger en etiketts bildtext.
- Egenskapen [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) anger färgfyllnadsattribut.

I följande exempel visas hur man lägger till en etikett i diagrammet. Exemplet använder en designfil som innehåller ett diagram. Vi använder denna fil för att infoga en etikett i diagrammet.

Nedan visas en skärmbild av designfilen.

**Designerdiagrammet**

![todo:image_alt_text](controls-in-charts_1.png)

Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden körs.

**En etikett läggs till i diagrammet**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att markera viktig information i en rapport är att använda en textruta. Till exempel, mata in text för att markera företagsnamnet eller för att ange den geografiska regionen med högst försäljning. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) tillhandahåller en metod som heter [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-), som används för att lägga till en textruta styrenhet i ett diagram. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar ett objekt av klassen [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) där klassen [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designfilen som innehåller ett diagram. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln.

Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet. Följande utdata genereras när koden körs.

**En textruta läggs till i diagrammet**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Lägga till bild i diagrammet**

Aspose.Cells gör det möjligt att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildfil.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) tillhandahåller en metod som heter [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-), som används för att lägga till ett bildobjekt i diagrammet. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett objekt av klassen [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) där klassen [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) representerar en bild i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designfilen som innehåller ett diagram. Vi använder denna fil för att infoga en bild i diagrammet.

Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet. Följande utdata genereras när koden körs.

**En bild infogas i diagrammet**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Lägger till kryssruta i diagrammet**

Aspose.Cells låter dig infoga kryssrutor i ett diagramblad genom att använda [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) uppräkning. Det följande exemplet visar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_5.jpg)

Den [utdatafil](InsertCheckboxInChartSheet_out.xlsx) som genereras av följande kodsnutt är bifogad som referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
