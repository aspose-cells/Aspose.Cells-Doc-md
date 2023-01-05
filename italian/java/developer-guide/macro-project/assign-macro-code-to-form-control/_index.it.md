---
title: Assegna il codice macro al controllo del modulo
type: docs
weight: 400
url: /it/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells permette di assegnare un Codice Macro ad un Controllo Modulo come un Pulsante. Si prega di utilizzare il[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) per assegnare un nuovo codice macro a un controllo modulo all'interno della cartella di lavoro.

{{% /alert %}} 
## **Assegnazione del codice macro al controllo del modulo utilizzando Aspose.Cells**
Il codice di esempio seguente crea una nuova cartella di lavoro, assegna un codice macro a un pulsante del modulo e salva l'output nel formato XLSM. Una volta, aprirai il file di output XLSM in Microsoft Excel vedrai il seguente codice macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Ecco un codice di esempio per generare il file di output XLSM con codice macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
