---
title: Hur man ställer in AutoRecover-egenskapen för Workbook
type: docs
weight: 220
url: /sv/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för arbetsboken. Standardvärdet för den här egenskapen är**Sann** . När du ställer in den**falsk** i en arbetsbok, Microsoft Excel inaktiverar automatisk återställning (autospara) på den Excel-filen.

 Aspose.Cells tillhandahåller[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) egenskap för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

 Följande kod förklarar hur du använder[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) arbetsbokens egendom. Koden läser först standardvärdet för denna egenskap som är**Sann** , då ställs det in som**falsk** och sparar arbetsboken. Sedan läser den arbetsboken igen och läser värdet av denna egenskap som är**falsk** just nu.

## C#-kod för att ställa in AutoRecover-egenskapen för Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Produktion**

Här är konsolutgången för ovanstående exempelkod.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
