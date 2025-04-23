---
title: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 260
url: /sv/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

När du ställer in siduppsättningsskalning med alternativet **Anpassa till n sidor bred och m hög**, så beräknar Microsoft Excel siduppsättningsfaktorn. Du kan beräkna samma sak med [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) egenskapen. Denna egenskap returnerar ett dubbelvärde som kan omvandlas till ett procentvärde. Till exempel, om den returnerar 0.5079621076 så innebär det att skalningsfaktorn är 51%.

{{% /alert %}} 
## **Beräkna siduppsättningsskalningsfaktorn**
Följande exempelkod illustrerar hur man beräknar siduppsättnings skalningsfaktorn med hjälp av [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) egenskapen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Konsoloutput**
Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
