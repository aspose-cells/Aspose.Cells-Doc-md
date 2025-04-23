---
title: Implementera Anpassad Papperstorlek på Arbetsbladet för Rendering
type: docs
weight: 30
url: /sv/java/implement-custom-paper-size-of-worksheet-for-rendering/
---

## **Möjliga användningsscenario**

Det finns ingen direkt alternativ tillgängligt för att skapa anpassade papperstorlekar i MS Excel, men du kan ange anpassad papperstorlek för dina önskade arbetsblad vid rendering av Excel-filen till PDF-filformat. Denna dokumentation förklarar hur man ställer in anpassad papperstorlek på ett arbetsblad med hjälp av Aspose.Cells API:er.

## **Implementera anpassad pappersstorlek för arbetsblad för rendering**

Aspose.Cells tillåter dig att implementera önskad papperstorlek för arbetsbladet genom att använda metoden [**customPaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#customPaperSize-double-double-) i [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup). Följande provkod illustrerar hur man specificerar en anpassad papperstorlek för det första arbetsbladet i arbetsboken. Se också [utdata-PDF:en](45056030.pdf) genererad med följande kod för referens.

## **Skärmdump**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.java" >}}
{{< app/cells/assistant language="java" >}}
