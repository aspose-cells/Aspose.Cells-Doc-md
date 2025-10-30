---
title: Hur man ställer in AutoRecover egenskapen för arbetsboken med Golang via C++
linktitle: Hur man ställer in egenskapen AutoRecover för arbetsboken
type: docs
weight: 220
url: /sv/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Lär dig hur du aktiverar eller inaktiverar AutoRecover egenskapen för en arbetsbok med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att ställa in AutoRecover-egenskapen för en arbetsbok. Standardvärdet för denna egenskap är **true**. När du ställer in den till **false** inaktiverar Microsoft Excel AutoRecover (Autospara) för den Excel-filen.

Aspose.Cells tillhandahåller egenskapen [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) för att aktivera eller inaktivera detta alternativ.

{{% /alert %}}

Följande kod förklarar hur man använder [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/)-egenskapen för arbetsboken. Koden läser först standardvärdet för denna egenskap, vilket är **true**, ändrar den till **false** och sparar arbetsboken. Därefter läser den arbetsboken igen och hämtar värdet av denna egenskap, vilket är **false** nu.

## C++ kod för att ställa in AutoRecover-egenskapen för arbetsbok

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Output**

Här är konsoloutputen från ovanstående exempelkod.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
