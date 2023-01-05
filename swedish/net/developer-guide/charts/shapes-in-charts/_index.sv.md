---
title: Former i diagram
type: docs
weight: 70
url: /sv/net/controls-in-charts/
---
{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontrollerna i ett diagram vid körning.

{{% /alert %}}

## **Lägger till etikettkontroll till diagrammet**

Etiketter är ett sätt att ge användarna information om innehållet i ett kalkylblad.
Aspose.Cells låter dig lägga till och manipulera etiketter även i diagram.

De[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), används för att lägga till en etikettkontroll till ett diagram. Nedan är en lista över de parametrar som används för metoden:

- **topp** – etikettens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av kartytan.
- **vänster** – etikettens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av kartytan.
- **höjd** – etikettens höjd, i enheter om 1/4000 av kartytan.
- **bredd** – etikettens bredd, i enheter om 1/4000 av kartytan.

 Metoden återkommer[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)objekt. De[**Märka**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) klass representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(egenskap) – anger en etiketts bildtextsträng.
- [**Fylla**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (egenskap) – anger fyllningsfärgsattributen.

Följande exempel visar hur du lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i sig. Vi använder den här filen för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden exekveras.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Lägga till TextBox Control till diagrammet**

 Ett sätt att lyfta fram viktig information i en rapport är att använda en textruta. Ange till exempel text för att markera företagsnamnet eller för att ange den geografiska region med högst försäljning. De[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)som används för att lägga till en textrutekontroll till ett diagram. Följande är parameterlistan som används för metoden:

- **topp** – den vertikala förskjutningen av textrutan från det övre vänstra hörnet i enheter på 1/4000 av sjökortsytan.
- **vänster** – den vertikala förskjutningen av textrutan från det övre vänstra hörnet i enheter på 1/4000 av kartytan.
- **höjd**– textrutans höjd, i enheter om 1/4000 av kartytan.
- **bredd** – textrutans bredd, i enheter om 1/4000 av kartytan.

 Metoden återkommer[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) objekt. De[**Textruta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)klass representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i sig. Vi använder den här filen för att infoga en textruta i diagrammet för att visa diagrammets titel. Nedan finns den ursprungliga koden för att lägga till textruta i diagrammet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Lägger till bild till diagrammet**

Aspose.Cells låter dig infoga bilder i ett diagram. Till exempel, lägg till en bild för att framhäva eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildsfil.

 De[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) klass tillhandahåller en metod som heter[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), som används för att lägga till ett bildobjekt till diagrammet. Följande är parameterlistan som används för metoden:

- **topp**– bildens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av sjökortsytan.
- **vänster**– bildens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av sjökortsytan.
- **ström** – ett strömobjekt som innehåller bilddata.
- **breddSkala** – skalan för bildens bredd, ett procentuellt värde.
- **höjdskala** – skalan för bildhöjd, ett procentuellt värde.

 Metoden returnerar en[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objekt. De[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)klass representerar ett bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i sig. Vi använder den här filen för att infoga en bild i diagrammet. Nedan är den ursprungliga koden för att lägga till bild till diagrammet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Lägger till kryssruta i diagrammet**

 Aspose.Cells låter dig infoga kryssrutor i ett diagramblad med hjälp av[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) uppräkning. Följande exempel visar hur du lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

 De[utdatafil](101089316.xlsx)som genereras av följande kodavsnitt bifogas för din referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Förhandsämnen**
- [Lägg till WordArt vattenstämpel i diagrammet](/cells/sv/net/add-wordart-watermark-to-chart/)
