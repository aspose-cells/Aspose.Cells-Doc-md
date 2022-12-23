---
title: Implementera anpassad pappersstorlek på arbetsbladet för rendering
type: docs
weight: 30
url: /sv/java/implement-custom-paper-size-of-worksheet-for-rendering/
---
## **Möjliga användningsscenarier**

Det finns inget direkt alternativ tillgängligt för att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in anpassad pappersstorlek för önskade kalkylblad när du renderar Excel-fil till filformatet PDF. Det här dokumentet förklarar hur du ställer in en anpassad pappersstorlek för ett kalkylblad med Aspose.Cells API:er.

## **Implementera anpassad pappersstorlek på arbetsbladet för rendering**

Aspose.Cells låter dig implementera önskad pappersstorlek på arbetsbladet med hjälp av[**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize(double,%20double) ) metod för[**Utskriftsformat**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) . Följande exempelkod illustrerar hur du anger en anpassad pappersstorlek för det första kalkylbladet i arbetsboken. Se även[utgång PDF](45056030.pdf) genereras med följande kod som referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
