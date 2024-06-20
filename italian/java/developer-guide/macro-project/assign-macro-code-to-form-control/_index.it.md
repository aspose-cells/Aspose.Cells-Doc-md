---
title: Assegnare Codice Macro al Controllo Modulo
type: docs
weight: 400
url: /it/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells ti consente di assegnare un Codice Macro a un Controllo Modulo come un Pulsante. Si prega di utilizzare il metodo [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) per assegnare un nuovo Codice Macro a un Controllo Modulo all'interno del workbook.

{{% /alert %}} 
## **Assegnare Codice Macro al Controllo Modulo usando Aspose.Cells**
Il codice di esempio seguente crea un nuovo workbook, assegna un Codice Macro a un Pulsante di Form e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel vedrai il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Ecco un codice di esempio per generare un file XLSM di output con Codice Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
