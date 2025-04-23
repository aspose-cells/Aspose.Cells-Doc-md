---
title: Assegna Macro a Controllo Modulo
type: docs
weight: 60
url: /it/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET permette di assegnare un Macro Code a un controllo modulo come un pulsante. Usa la proprietà [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) per assegnare un nuovo Macro Code a un controllo modulo all’interno della cartella di lavoro.

{{% /alert %}}

Il codice di esempio seguente crea un nuovo workbook, assegna un codice Macro a un pulsante di modulo e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel, vedrai il codice Macro seguente.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna Macro a controllo modulo in Python**

Qui c'è il codice di esempio per generare il file XLSM di output con il codice Macro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
