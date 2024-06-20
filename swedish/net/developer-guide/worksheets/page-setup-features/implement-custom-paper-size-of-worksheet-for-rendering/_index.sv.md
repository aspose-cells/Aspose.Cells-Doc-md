---
title: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering
type: docs
weight: 70
url: /sv/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Den här artikeln förklarar hur man använder exempelkod för C# API eller .NET Library för att ställa in anpassad pappersstorlek för önskade arbetshäften när man renderar Excel fil till PDF filformat programmatiskt.
keywords: ställa in anpassad pappersstorlek vid rendering av excel till pdf c#
---

## **Möjliga användningsscenario**

Det finns ingen direkt möjlighet att skapa anpassade pappersstorlekar i MS Excel, men du kan ställa in anpassad pappersstorlek för önskade arbetshäften när du renderar Excel-fil till PDF-filformat. Detta dokument förklarar hur man ställer in anpassad pappersstorlek för ett ark med hjälp av Aspose.Cells API:er.

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**

Aspose.Cells låter dig implementera önskad pappersstorlek på arket. Du kan använda metoden [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) av klassen [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) för att ange en anpassad sidlängd. Följande exempelkod illustrerar hur man anger en anpassad pappersstorlek för det första arket i arbetsboken. Se även [utdata-PDF](45056028.pdf) genererad med följande kod för referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
