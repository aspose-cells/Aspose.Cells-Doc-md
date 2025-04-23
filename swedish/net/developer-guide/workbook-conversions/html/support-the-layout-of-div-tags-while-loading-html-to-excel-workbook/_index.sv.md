---
title: Stöd för layout av DIV taggar vid laddning av HTML till Excelsekvens
type: docs
weight: 50
url: /sv/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalt ignoreras layouten av div-taggar när HTML laddas in i en excel arbetsbok. Om du vill att layouten av div-taggar inte ska ignoreras, ställ då in egenskapen [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) till **true**. Standardvärdet för denna egenskap är **false**.

{{% /alert %}} 

Följande provkod illustrerar användningen av [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) egenskapen. Vänligen ladda ner [Aspose Logotyp](5115218.png) som används i inmatnings-HTML:n och [utmatnings-excelfilen](5115220.xlsx) som genereras av koden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
