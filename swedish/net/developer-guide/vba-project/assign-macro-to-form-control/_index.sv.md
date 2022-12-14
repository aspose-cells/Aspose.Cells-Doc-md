---
title: Tilldela makro till formulärkontroll
type: docs
weight: 60
url: /sv/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells låter dig tilldela en makrokod till en formulärkontroll som en knapp. Vänligen använd[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) egenskap för att tilldela en ny makrokod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande exempelkod skapar en ny arbetsbok, tilldelar en makrokod till en formulärknapp och sparar utdata i XLSM-format. När du kommer att öppna utdata XLSM-filen i Microsoft Excel kommer du att se följande makrokod.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i C#**

Här är exempelkoden för att generera utdata-XLSM-filen med makrokod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
