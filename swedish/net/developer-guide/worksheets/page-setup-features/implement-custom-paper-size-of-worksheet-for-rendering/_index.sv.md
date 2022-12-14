---
title: Implementera anpassad pappersstorlek på arbetsbladet för rendering
type: docs
weight: 70
url: /sv/net/implement-custom-paper-size-of-worksheet-for-rendering/
---
## **Möjliga användningsscenarier**

Det finns inget direkt alternativ tillgängligt för att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in anpassad pappersstorlek för önskade kalkylblad när du renderar Excel-fil till PDF-filformat. Det här dokumentet förklarar hur du ställer in en anpassad pappersstorlek för ett kalkylblad med Aspose.Cells API:er.

## **Implementera anpassad pappersstorlek på arbetsbladet för rendering**

 Aspose.Cells låter dig implementera önskad pappersstorlek på arbetsbladet. Du kan använda[**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) metod för[**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) klass för att ange en anpassad sidstorlek. Följande exempelkod illustrerar hur du anger en anpassad pappersstorlek för det första kalkylbladet i arbetsboken. Se även[mata ut PDF](45056028.pdf) genereras med följande kod som referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
