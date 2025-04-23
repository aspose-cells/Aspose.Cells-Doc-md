---
title: Aspose.Cells objektmodell
type: docs
weight: 20
url: /sv/net/aspose-cells-object-model/
---

{{% alert color="primary" %}} 

Aspose.Cells objektmodell ger information om de strukturella relationerna mellan objekten i Aspose.Cells klassbiblioteket 

{{% /alert %}} 

Den övre nivån av strukturen för Aspose.Cells objektmodell visas nedan på ett hierarkiskt sätt

|**Översta nivån av Aspose.Cells objektmodell**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_1.png)|
Som du kan se från ovanstående figur är roten av objektmodellen arbetsboken. En kort beskrivning av några av objekten ges nedan för inledande ändamål
## **WorksheetCollection/Worksheet**
Arbetsboksobjekt innehåller WorksheetCollection, som representerar samlingen av alla arbetsbladsobjekt i en kalkylblad som visas nedan

|**Arbetsblad & Arbetsbladsobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_2.png)|
## **Cells/Cell**
Varje arbetsbladsobjekt innehåller ett Cells-objekt som representerar samlingen av alla Cell-objekt i ett arbetsblad som visas nedan

|**Celler & Cell-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_3.png)|
Du kan använda Cell-objektet för att hämta och ange värdet, stilen, formeln och andra egenskaper för en enskild cell
## **ChartCollection/Chart**
Diagramobjekt representerar en samling med alla Diagramobjekt i ett Arbetsblad. Varje Diagramobjekt består av flera andra objekt som arbetar tillsammans för att skapa och hantera diagram. Diagramstrukturen i Aspose.Cells visas i diagrammet nedan

|**Objektmodell för diagrammet**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_4.png)|
## **CommentCollection/Comment**
Varje arbetsbladsobjekt innehåller också ett kommentarsobjekt som representerar samlingen av alla kommentarsobjekt i ett arbetsblad som visas nedan

|**Kommentarer & Kommentarsobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_5.png)|
Ett kommentarsobjekt används för att lägga till en kommentar till en angiven cell i arbetsbladet
## **HorizontalPageBreakCollection/HorizontalPageBreak**
Varje arbetsbladsobjekt innehåller en HorizontalPageBreakCollection som representerar en samling av alla HorizontalPageBreak-objekt i ett arbetsblad som visas nedan

|**HPageBreaks & HPageBreak-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_6.png)|
Ett HorizontalPageBreak-objekt används för att skapa en horisontell sidbrytning i arbetsbladet
## **HyperlinkCollection/Hyperlink**
Ett Arbetsbladsobjekt innehåller också en HyperlinkCollection som representerar en samling av alla Hyperlänkobjekt i arbetsbladet som visas nedan

|**Hyperlänkar & Hyperlänkobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_7.png)|
Ett Hyperlänkobjekt representerar en hyperlänk i arbetsbladet. Utvecklare kan ställa in hyperlänkadress och andra relaterade egenskaper med hjälp av Hyperlänkobjekt
## **PictureCollection/Picture**
Varje arbetsbladsobjekt innehåller en PictureCollection-objekt som representerar en samling av alla Bildobjekt i ett arbetsblad som visas nedan

|**Bilder & Bildobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_8.png)|
Ett Bildobjekt representerar en bild i arbetsbladet. Med Bildobjektet kan utvecklare inte bara lägga till bilder i sina arbetsblad utan också positionera dessa bilder på valfri plats. Det är också möjligt att ställa in ramar eller andra egenskaper för bilderna

## **VerticalPageBreakCollection/VerticalPageBreak**
Varje arbetsbladsobjekt innehåller en VerticalPageBreakCollection-objekt som representerar en samling av alla VerticalPageBreak-objekt i ett arbetsblad som visas nedan

|**VPageBreaks & VPageBreak-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_9.png)|
Ett VerticalPageBreak-objekt används för att skapa ett vertikalt sidbrott i kalkylarket.


## **PivotTableCollection/PivotTable**
Varje Worksheet-objekt innehåller en PivotTableCollection-objekt som representerar en samling av alla PivotTable-objekt i ett kalkylblad som visas nedan:

|**PivotTabeller & PivotTable-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_10.png)|
Ett PivotTable-objekt representerar en pivottabell i kalkylarket. Utvecklare kan ställa in stilen för pivottabellen och andra relaterade egenskaper med hjälp av PivotTable-objekt.

## **TimelineCollection/Timeline**
Varje Worksheet-objekt innehåller en TimelineCollection-objekt som representerar en samling av alla tidsaxelobjekt i ett kalkylblad som visas nedan:

|**Tidsaxlar & tidsaxelobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_11.png)|
Ett tidsaxel-objekt representerar en tidsaxel i kalkylarket. Utvecklare kan ställa in stilen för tidsaxeln och andra relaterade egenskaper med hjälp av tidsaxel-objekt.

## **SlicerCollection/Slicer**
Varje Worksheet-objekt innehåller en SlicerCollection-objekt som representerar en samling av alla Slicer-objekt i ett kalkylblad som visas nedan:

|**Slicers & Slicer-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_12.png)|
Ett Slicer-objekt representerar en slicer i kalkylarket. Utvecklare kan ställa in stilen för slicern och andra relaterade egenskaper med hjälp av Slicer-objekt.

## **ListObjectCollection/ListObject**
Varje Worksheet-objekt innehåller en ListObjectCollection-objekt som representerar en samling av alla ListObject-objekt i ett kalkylblad som visas nedan:

|**Listor & ListObject-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_13.png)|
Ett ListObject-objekt representerar en tabell i kalkylarket. Utvecklare kan ställa in stilen för tabellen och andra relaterade egenskaper med hjälp av ListObject-objekt.

## **ShapeCollection/Shape**
Varje Worksheet-objekt innehåller en ShapeCollection-objekt som representerar en samling av alla Shape-objekt i ett kalkylblad som visas nedan:

|**Former & formobjekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_14.png)|
Ett Shape-objekt representerar en form i kalkylarket. Utvecklare kan ställa in stilen för formen och andra relaterade egenskaper med hjälp av Shape-objekt.

## **SparklineGroupCollection/SparklineGroup**
Varje Worksheet-objekt innehåller en SparklineGroupCollection-objekt som representerar en samling av alla SparklineGroup-objekt i ett kalkylblad som visas nedan:

|**Sparkline-grupper & SparklineGroup-objekt**|
| :- |
|![todo:image_alt_text](aspose-cells-object-model_15.png)|
Ett SparklineGroup-objekt representerar en sparkline-grupp i kalkylarket. Utvecklare kan ställa in stilen för sparkline-gruppen och andra relaterade egenskaper med hjälp av SparklineGroup-objekt.
{{< app/cells/assistant language="csharp" >}}
