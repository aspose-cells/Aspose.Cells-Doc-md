---
title: Assegna Macro a Controllo Modulo
type: docs
weight: 60
url: /it/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di assegnare un codice Macro a un Controllo Modulo come un Pulsante. Si prega di utilizzare la proprietà [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) per assegnare un nuovo codice Macro a un Controllo Modulo all'interno del workbook.

{{% /alert %}}

Il codice di esempio seguente crea un nuovo workbook, assegna un codice Macro a un pulsante di modulo e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel, vedrai il codice Macro seguente.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna Macro a Controllo Modulo in C#**

Qui c'è il codice di esempio per generare il file XLSM di output con il codice Macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
