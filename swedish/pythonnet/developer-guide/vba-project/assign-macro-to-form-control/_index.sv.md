---
title: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillåter att du tilldelar ett Makrokod till en formulärkontroll som en knapp. Använd [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name)-egenskapen för att tilldela en ny Makrokod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande exempelkod skapar en ny arbetsbok, tilldela en makro kod till en formulärknapp och sparar utdata i XLSM-format. När du sedan öppnar utdata-XLSM-filen i Microsoft Excel kommer du att se följande makro kod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i Python**

Här är ett exempel på kod för att generera utdata-XLSM-fil med makro kod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
