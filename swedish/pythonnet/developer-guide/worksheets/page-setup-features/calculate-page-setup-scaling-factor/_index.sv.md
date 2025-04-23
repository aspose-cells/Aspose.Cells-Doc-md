---
title: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 300
url: /sv/python-net/calculate-page-setup-scaling-factor/
description: Denna artikel ger exempel på kod som förklarar hur man använder Aspose.Cells för Python via .NET API er för att beräkna sidinställningens skalingsfaktor med hjälp av Fit to n sidor bredd och m högt alternativ för Excel arbetsblad programmässigt.
keywords: Python Excel bibliotek, Python passa till n sidor brett och m högt Excel, beräkna sidinställningens skalningsfaktor i Python.
---

{{% alert color="primary" %}}

När du ställer in sidlayoutskalning med alternativet **Passar till n sidor breda och m höga** beräknar Microsoft Excel sidlayoutskalningsfaktorn. Du kan beräkna samma sak med hjälp av [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)-egenskapen. Denna egenskap returnerar ett dubbelt värde som kan konverteras till procentvärde. Till exempel, om den returnerar 0,5 innebär det att skalningsfaktorn är 50%.

{{% /alert %}}

Följande exempelkod illustrerar hur man beräknar sidlayoutskalningsfaktorn med hjälp av [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale)-egenskapen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
