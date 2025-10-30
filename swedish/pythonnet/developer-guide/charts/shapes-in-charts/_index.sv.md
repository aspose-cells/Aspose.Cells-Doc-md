---
title: Former i diagram
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att lägga till kontroller och anpassa diagram i Microsoft Excel. Vår guide visar hur man manipulerar diagramseklement, justerar formatering och förbättrar det övergripande utseendet och användbarheten av diagrammen.
keywords: Aspose.Cells för Python via .NET, Diagramkontroller, Diagramanpassning, Microsoft Excel, Diagramelement, Formatering.
type: docs
weight: 70
url: /sv/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells för Python via .NET kan lägga till kontroller till ett diagram under körning.

{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användare om innehållet i ett kalkylarks innehåll.
Aspose.Cells för Python via .NET ger dig möjlighet att lägga till och manipulera etiketter även i diagram.

Klassen [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod med namnet [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart), som används för att lägga till en etikettkontroll i ett diagram. Nedan finns en lista över de parametrar som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter på 1/4000 av diagramområdet.

Metoden returnerar [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label)-objekt. Klassen [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (egenskap) – specificerar en etiketts bildtext.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (egenskap) – specificerar färgfyllningsegenskaper.

Följande exempel visar hur man lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden utförs.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att markera viktig information i en rapport är att använda en textruta. Till exempel, mata in text för att markera företagsnamnet eller för att ange den geografiska regionen med högst försäljning. Klassen [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart), som används för att lägga till en textruta styrenhet i ett diagram. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – den vertikala avvikelsen för textrutan från det övre vänstra hörnet i enheter på 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox)-objekt. Klassen [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln. Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Lägga till bild i diagrammet**

Aspose.Cells för Python via .NET tillåter att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga ett varumärke.

Klassen [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) tillhandahåller en metod som heter [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart), som används för att lägga till ett bildobjekt i diagrammet. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objekt. Klassen [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) representerar en bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en bild i diagrammet. Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Lägger till kryssruta i diagrammet**

Aspose.Cells för Python via .NET möjliggör att infoga kryssrutor i ett diagramblad med hjälp av [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype) uppräkningsfunktion. Följande exempel visar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

Den [utdatafilen](101089316.xlsx) som genererats av följande kodsnutt bifogas för din referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Fortsatta ämnen**
- [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/python-net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="python-net" >}}
