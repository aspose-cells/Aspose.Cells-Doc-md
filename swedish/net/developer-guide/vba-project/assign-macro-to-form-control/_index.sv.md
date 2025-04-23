---
title: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells låter dig tilldela ett makro kod till en formulärkontroll som en knapp. Använd [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) -egenskapen för att tilldela en ny makro kod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande exempelkod skapar en ny arbetsbok, tilldela en makro kod till en formulärknapp och sparar utdata i XLSM-format. När du sedan öppnar utdata-XLSM-filen i Microsoft Excel kommer du att se följande makro kod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i C#**

Här är ett exempel på kod för att generera utdata-XLSM-fil med makro kod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
