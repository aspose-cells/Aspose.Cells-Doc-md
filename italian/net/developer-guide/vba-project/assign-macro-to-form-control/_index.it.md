---
title: Assegna macro al controllo del modulo
type: docs
weight: 60
url: /it/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells permette di assegnare un Codice Macro ad un Controllo Modulo come un Pulsante. Si prega di utilizzare il[**Forma.MarcoNome**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) proprietà per assegnare un nuovo codice macro a un controllo modulo all'interno della cartella di lavoro.

{{% /alert %}}

Il codice di esempio seguente crea una nuova cartella di lavoro, assegna un codice macro a un pulsante modulo e salva l'output nel formato XLSM. Una volta, aprirai il file di output XLSM in Microsoft Excel vedrai il seguente codice macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna macro al controllo del modulo in C#**

Ecco il codice di esempio per generare il file di output XLSM con il codice macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
