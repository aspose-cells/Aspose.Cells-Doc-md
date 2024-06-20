---
title: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 160
url: /sv/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att ställa in egenskapen AutoRecover för arbetsboken. Standardvärdet för denna egenskap är **true**. När du anger det som **false** på en arbetsbok inaktiverar Microsoft Excel autorecover (autosave) på den Excel-filen.

Aspose.Cells tillhandahåller egenskapen [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

## Java-kod för att ställa in egenskapen AutoRecover för arbetsboken

Följande kod förklarar hur man använder egenskapen [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) för arbetsboken. Koden läser först det standardvärde som är **true**, sedan ställer den in det som **false** och sparar arbetsboken. Sedan läser den in arbetsboken igen och läser värdet av denna egenskap som för närvarande är falskt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Utdata genererad av exempelkod

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
