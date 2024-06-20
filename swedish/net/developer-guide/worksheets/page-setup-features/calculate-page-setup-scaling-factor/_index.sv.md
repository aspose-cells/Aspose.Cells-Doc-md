---
title: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 300
url: /sv/net/calculate-page-setup-scaling-factor/
description: Den här artikeln innehåller exempelkod som förklarar hur man använder C# API eller .NET biblioteket för att beräkna skalningsfaktorn för sidlayout med alternativet Passar till n sidor breda och m höga i Excel arket programmatiskt.
keywords: Passar till n sidor breda och m höga exel c#, beräkna sidlayout skalningsfaktor c#
---

{{% alert color="primary" %}}

När du ställer in sidlayoutskalning med alternativet **Passar till n sidor breda och m höga** beräknar Microsoft Excel sidlayoutskalningsfaktorn. Du kan beräkna samma sak med hjälp av [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)-egenskapen. Denna egenskap returnerar ett dubbelt värde som kan konverteras till procentvärde. Till exempel, om den returnerar 0,5 innebär det att skalningsfaktorn är 50%.

{{% /alert %}}

Följande exempelkod illustrerar hur man beräknar sidlayoutskalningsfaktorn med hjälp av [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)-egenskapen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
