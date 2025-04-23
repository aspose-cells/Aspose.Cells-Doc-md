---
title: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 220
url: /sv/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för Python via .NET för att ställa in AutoRecover-egenskapen för arbetsboken. Standardvärdet för denna egenskap är **true**. När du sätter den till **false** inaktiverar Microsoft Excel AutoRecover (Autospara) för den Excel-filen.

Aspose.Cells för Python via .NET tillhandahåller egenskapen [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

Följande kod förklarar hur man använder egenskapen [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) för arbetsboken. Koden läser först standardvärdet för denna egenskap som är **true**, sedan sätter den till **false** och sparar arbetsboken. Därefter läser den arbetsboken igen och hämtar värdet av denna egenskap, som då är **false**.

## C#-kod för att ställa in AutoRecover-egenskapen för arbetsboken

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Output**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

