---
title: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 220
url: /sv/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att ställa in egenskapen AutoRecover för arbetsboken. Standardvärdet för denna egenskap är **true**. När du ställer den som **false** på en arbetsbok avaktiverar Microsoft Excel AutoRecover (autosparläge) för den Excel-filen.

Aspose.Cells tillhandahåller egenskapen [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

Följande kod förklarar hur man använder egenskapen [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) för arbetsboken. Koden läser först in standardvärdet för egenskapen, som är **true**, sedan ställer den in värdet som **false** och sparar arbetsboken. Sedan läser den arbetsboken igen och läser värdet för egenskapen, som nu är **false**.

## C#-kod för att ställa in AutoRecover-egenskapen för arbetsboken

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Output**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
