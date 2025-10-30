---
title: Visa cellområde som datamärken med Golang via C++
linktitle: Visar cellområdet som datamärken
description: Lär dig att visa ett cellområde som datapunkter i diagram med Aspose.Cells for C++. Vår guide visar hur du länkar etiketterna till din datakälla och formaterar dem för att ge korrekt och meningsfull information.
keywords: Aspose.Cells for C++, diagram, datapunktetiketter, cellområde, datakälla, formatering, noggrannhet, meningsfull information.
type: docs
weight: 130
url: /sv/go-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

I Microsoft Excel 2013 kan du visa ett cellområde för datamärken. Aspose.Cells stödjer denna funktion.

{{% /alert %}}

## **Kryssrutan för att visa cellområde som datamärken**

Att visa cellområdet som datamärken i Microsoft Excel:

1. Välj seriens datamärken och högerklicka för att öppna snabbmenyn.
1. Välj **Formatera datamärken**. Etikettalternativ visas.
1. Välj eller avmarkera alternativet **Etiketten innehåller - Värde från celler**.

Exempelkoden nedan använder ett diagramseriedatamärken och ställer in [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/go-cpp/datalabels/getshowcellrange/)-egenskapen till **true** för att välja alternativet **Etikett innehåller - Värde från celler**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowingCellRangeAsTheDataLabels.go" >}}
