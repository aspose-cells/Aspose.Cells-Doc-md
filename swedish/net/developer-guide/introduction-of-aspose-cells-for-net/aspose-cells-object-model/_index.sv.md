---
title: Aspose.Cells Objektmodell
type: docs
weight: 20
url: /sv/net/aspose-cells-object-model/
---
{{% alert color="primary" %}} 

 Aspose.Cells Objektmodell ger information om de strukturella relationerna mellan objekten i Aspose.Cells klassbibliotek.

{{% /alert %}} 

Den översta nivåstrukturen för objektmodellen Aspose.Cells visas nedan på ett hierarkiskt sätt.

|**Struktur på översta nivån för Aspose.Cells Objektmodell**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Som du kan se från ovanstående figur att roten av objektmodellen är Workbook-objektet. En kort beskrivning av några av objekten ges nedan i introduktionssyfte.
## **Arbetsbladssamling/Arbetsblad**
Arbetsboksobjektet innehåller WorksheetCollection, som representerar samlingen av alla kalkylbladsobjekt i ett kalkylblad enligt nedan:

|**Arbetsblad & Kalkylbladsobjekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|
## **Cells/Cell**
Varje kalkylbladsobjekt innehåller ett Cells-objekt som representerar samlingen av alla Cell-objekt i ett kalkylblad enligt nedan:

|**Cells & Cell objekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Du kan använda objektet Cell för att hämta och ställa in värdet, stilen, formeln och andra egenskaper för en enskild cell.
## **Diagramsamling/diagram**
Diagramobjekt representerar en samling av alla diagramobjekt i ett kalkylblad. Varje diagramobjekt består av flera andra objekt som samverkar för att skapa och hantera diagram. Diagramstrukturen i Aspose.Cells visas i diagrammet nedan:

|**Objektmodell av diagrammet**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|
## **Kommentarsamling/kommentar**
Varje kalkylbladsobjekt innehåller också ett kommentarsobjekt som representerar samlingen av alla kommentarsobjekt i ett kalkylblad enligt nedan:

|**Kommentarer & Kommentarobjekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Ett Comment-objekt används för att lägga till en kommentar till valfri specificerad cell i kalkylbladet.
## **HorizontalPageBreakCollection/HorizontalPageBreak**
Varje kalkylbladsobjekt innehåller en HorizontalPageBreakCollection som representerar en samling av alla HorizontalPageBreak-objekt i ett kalkylblad enligt nedan:

|**HPageBreaks & HPageBreak-objekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Ett HorizontalPageBreak-objekt används för att skapa en horisontell sidbrytning i kalkylbladet.
## **HyperlinkCollection/Hyperlink**
Ett kalkylbladsobjekt innehåller också en HyperlinkCollection som representerar en samling av alla hyperlänkobjekt i kalkylbladet enligt nedan:

|**Hyperlänkar och hyperlänkobjekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Ett hyperlänkobjekt representerar en hyperlänk i kalkylbladet. Utvecklare kan ställa in hyperlänkadresser och andra relaterade egenskaper med hjälp av Hyperlink-objekt.
## **Bildsamling/bild**
Varje kalkylbladsobjekt innehåller ett PictureCollection-objekt som representerar en samling av alla bildobjekt i ett kalkylblad enligt nedan:

|**Bilder & Bildobjekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Ett bildobjekt representerar en bild i kalkylbladet. Med hjälp av Picture Object kan utvecklare inte bara lägga till bilder i sina kalkylblad utan även placera dessa bilder var som helst. Det är också möjligt att ställa in ramar eller andra egenskaper för bilderna.
## **VerticalPageBreakCollection/VerticalPageBreak**
Varje kalkylbladsobjekt innehåller ett VerticalPageBreakCollection-objekt som representerar en samling av alla VerticalPageBreak-objekt i ett kalkylblad enligt nedan:

|**VPageBreaks & VPageBreak-objekt**|
|:- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Ett VerticalPageBreak-objekt används för att skapa en vertikal sidbrytning i kalkylbladet.
