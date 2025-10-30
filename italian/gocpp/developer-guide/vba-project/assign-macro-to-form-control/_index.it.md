---
title: Assegnare una Macro al Controllo modulo con Golang tramite C++
linktitle: Assegna Macro a Controllo Modulo
type: docs
weight: 60
url: /it/go-cpp/assign-macro-to-form-control/
description: Impara come assegnare un Codice Macro a un Controllo Modulo come un Pulsante usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di assegnare un codice Macro a un Controllo Modulo come un Pulsante. Si prega di utilizzare la proprietà [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) per assegnare un nuovo codice Macro a un Controllo Modulo all'interno del workbook.

{{% /alert %}}

Il seguente esempio di codice crea un nuovo workbook, assegna un Codice Macro a un Pulsante di Modulo e salva l’output in formato XLSM. Una volta aperto il file XLSM in Microsoft Excel, vedrai il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna Macro al Controllo Modulo in C++**

Qui c'è il codice di esempio per generare il file XLSM di output con il codice Macro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
