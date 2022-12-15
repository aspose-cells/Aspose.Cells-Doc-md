---
title: Beräkna skalningsfaktor för sidinställningar
type: docs
weight: 260
url: /sv/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

När du ställer in Skalning av sidinställningar med**Passar till n sida/sidor bred och m hög** option, Microsoft Excel beräknar skalningsfaktorn för sidinställningar. Du kan räkna ut samma sak med hjälp av[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) fast egendom. Den här egenskapen returnerar ett dubbelt värde som kan konverteras till ett procentuellt värde. Till exempel, om den returnerar 0,5079621076 betyder det att skalfaktorn är 51 %.

{{% /alert %}} 
## **Beräkna skalningsfaktor för sidinställningar**
 Följande exempelkod illustrerar hur man beräknar skalfaktor för sidinställningar med hjälp av[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)fast egendom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Konsolutgång**
Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
