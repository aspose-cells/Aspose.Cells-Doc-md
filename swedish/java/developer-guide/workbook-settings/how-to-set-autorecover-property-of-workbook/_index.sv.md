---
title: Hur man ställer in AutoRecover-egenskapen för Workbook
type: docs
weight: 160
url: /sv/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för arbetsboken. Standardvärdet för den här egenskapen är**Sann** . När du ställer in den**falsk** en arbetsbok, Microsoft Excel inaktiverar automatisk återställning (autospara) på den Excel-filen.

 Aspose.Cells tillhandahåller[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) egenskap för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

## Java-kod för att ställa in AutoRecover-egenskapen för Workbook

 Följande kod förklarar hur du använder[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) arbetsbokens egendom. Koden läser först standardvärdet för denna egenskap som är**Sann** , då ställs det in som**falsk** och sparar arbetsboken. Sedan läser den arbetsboken igen och läser värdet på den här egenskapen som är falsk vid denna tidpunkt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Utdata genererad av exempelkod

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
