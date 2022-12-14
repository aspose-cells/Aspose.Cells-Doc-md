---
title: Kontroller i diagram
linktitle: Former I Diagram
type: docs
weight: 60
url: /sv/java/controls-in-charts/
---
{{% alert color="primary" %}}

Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontrollerna i ett diagram vid körning.

{{% /alert %}}

## **Lägger till etikettkontroll till diagrammet**

Etiketter är ett sätt att ge användarna information om innehållet i ett kalkylblad. Aspose.Cells låter dig lägga till och manipulera etiketter även i diagram.

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) klass tillhandahåller en metod som heter[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), används för att lägga till en etikettkontroll till ett diagram. Nedan är en lista över de parametrar som används för metoden:

- **topp** – etikettens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av kartytan.
- **vänster** – etikettens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av kartytan.
- **höjd** – etikettens höjd, i enheter om 1/4000 av kartytan.
- **bredd** – etikettens bredd, i enheter om 1/4000 av kartytan.

 Metoden returnerar ett objekt av[**Märka**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) klass, där[**Märka**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)klass representerar en etikett i diagrammet. Den har några viktiga medlemmar som beskrivs nedan:

- [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)egenskapen anger en etiketts bildtextsträng.
- [**Fylla**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) egenskapen anger fyllningsfärgsattributen.

Följande exempel visar hur du lägger till en etikett i diagrammet. Exemplet använder en designerfil som har ett diagram i sig. Vi använder den här filen för att infoga en etikett i diagrammet.

Nedan finns en skärmdump av designerfilen.

**Designerdiagrammet**

![todo:image_alt_text](controls-in-charts_1.png)

Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden exekveras.

**En etikett läggs till i diagrammet**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Lägga till TextBox Control till diagrammet**

 Ett sätt att lyfta fram viktig information i en rapport är att använda en textruta. Ange till exempel text för att markera företagsnamnet eller för att ange den geografiska region med högst försäljning. De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) klass tillhandahåller en metod som heter[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), som används för att lägga till en textrutekontroll till ett diagram. Följande är parameterlistan som används för metoden:

- **topp** – den vertikala förskjutningen av textrutan från det övre vänstra hörnet i enheter på 1/4000 av sjökortsytan.
- **vänster** – den vertikala förskjutningen av textrutan från det övre vänstra hörnet i enheter på 1/4000 av sjökortsytan.
- **höjd**– textrutans höjd, i enheter om 1/4000 av kartytan.
- **bredd** – textrutans bredd, i enheter om 1/4000 av kartytan.

 Metoden returnerar ett objekt av[**Textruta**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) klass där[**Textruta**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)klass representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen som har ett diagram i sig. Vi använder den här filen för att infoga en textruta i diagrammet för att visa diagrammets titel.

Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet. Följande utdata genereras när koden exekveras.

**En textruta läggs till i diagrammet**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Lägger till bild till diagrammet**

Aspose.Cells låter dig infoga bilder i ett diagram. Till exempel, lägg till en bild för att framhäva eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildsfil.

 De[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) klass tillhandahåller en metod som heter[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), som används för att lägga till ett bildobjekt i diagrammet. Följande är parameterlistan som används för metoden:

- **topp**– bildens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av sjökortsytan.
- **vänster**– bildens vertikala förskjutning från det övre vänstra hörnet i enheter om 1/4000 av sjökortsytan.
- **ström** – ett strömobjekt som innehåller bilddata.
- **breddSkala** – skalan för bildens bredd, ett procentuellt värde.
- **höjdskala** – skalan för bildhöjd, ett procentuellt värde.

 Metoden returnerar ett objekt av[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) klass där[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)klass representerar ett bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen som har ett diagram i sig. Vi använder den här filen för att infoga en bild i diagrammet.

Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet. Följande utdata genereras när koden exekveras

**En bild infogas i diagrammet**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Lägger till kryssruta i diagrammet**

Aspose.Cells låter dig infoga kryssrutor i ett diagramblad med hjälp av[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) uppräkning. Följande exempel visar hur du lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_5.jpg)

De[utdatafil](InsertCheckboxInChartSheet_out.xlsx)som genereras av följande kodavsnitt bifogas för din referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
