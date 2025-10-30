---
title: Formulär i Diagram med Golang via C++
linktitle: Former i diagram
description: Lär dig hur du använder Aspose.Cells for C++ för att lägga till kontroller och anpassa diagram i Microsoft Excel. Vår guide kommer att demonstrera hur man manipulerar diagramelement, justerar formatering och förbättrar det övergripande utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, Diagramkontroller, Diagramanpassning, Microsoft Excel, Diagramelement, Formatering.
type: docs
weight: 70
url: /sv/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontroller i ett diagram vid körtid.

{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användare om innehållet i ett kalkylarks innehåll.
Aspose.Cells tillåter dig att lägga till och manipulera etiketter även i diagram.

Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) tillhandahåller en metod som heter [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/), som används för att lägga till en etikettkontroll till ett diagram. Nedan är en lista över parametrarna som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter på 1/4000 av diagramområdet.

Metoden returnerar [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/) objekt. [**Label**](https://reference.aspose.com/cells/go-cpp/label/)-klassen representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (egenskap) – anger etikettens rubriksträng.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (egenskap) – specificerar färgfyllningsegenskaper.

Följande exempel visar hur man lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden utförs.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att belysa viktig information i en rapport är att använda en textruta. Till exempel, ange text för att belysa företagsnamnet eller för att visa den geografiska regionen med högst försäljning. Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) tillhandahåller en metod som heter [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/), som används för att lägga till en textrutekontroll till ett diagram. Följande är parameternlistan för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – den vertikala avvikelsen för textrutan från det övre vänstra hörnet i enheter på 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) objekt. [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/)-klassen representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln. Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Lägga till bild i diagrammet**

Aspose.Cells gör det möjligt att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildfil.

Klass [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) tillhandahåller en metod som heter [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/), som används för att lägga till en bildobjekt till diagrammet. Följande är parameternlistan för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/) objekt. [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/)-klassen representerar ett bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en bild i diagrammet. Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Lägger till kryssruta i diagrammet**

Aspose.Cells tillåter dig att infoga kryssrutor i ett diagramblad genom att använda [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/)-uppräkningen. Följande exempel demonstrerar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

Den [utdatafilen](101089316.xlsx) som genererats av följande kodsnutt bifogas för din referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Fortsatta ämnen**
- [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/cpp/add-wordart-watermark-to-chart/)
