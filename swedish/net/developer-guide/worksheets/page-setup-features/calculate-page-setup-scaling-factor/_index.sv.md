---
title: Beräkna skalningsfaktor för sidinställningar
type: docs
weight: 300
url: /sv/net/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}}

När du ställer in Skalning av sidinställningar med**Passar till n sida/sidor bred och m hög** option, Microsoft Excel beräknar skalningsfaktorn för sidinställningar. Du kan räkna ut samma sak med hjälp av[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) fast egendom. Den här egenskapen returnerar ett dubbelt värde som kan konverteras till procentuellt värde. Till exempel, om den returnerar 0,5 betyder det att skalfaktorn är 50 %.

{{% /alert %}}

 Följande exempelkod illustrerar hur man beräknar skalfaktor för sidinställningar med hjälp av[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
