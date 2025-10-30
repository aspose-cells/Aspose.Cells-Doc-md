---
title: Tilldela makro till formulärkontroll med Golang via C++
linktitle: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/go-cpp/assign-macro-to-form-control/
description: Lär dig hur man tilldelar en makkod till en formulärkontroll som en knapp med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig tilldela ett makro kod till en formulärkontroll som en knapp. Använd [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) -egenskapen för att tilldela en ny makro kod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande kodexempel skapar en ny arbetsbok, tilldelar ett makrokod till en formulärknapp och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel, kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i C++**

Här är ett exempel på kod för att generera utdata-XLSM-fil med makro kod.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
