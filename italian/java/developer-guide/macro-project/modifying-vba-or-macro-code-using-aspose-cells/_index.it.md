---
title: Modifica VBA o codice macro utilizzando Aspose.Cells
type: docs
weight: 90
url: /it/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

È possibile modificare VBA o Macro Code utilizzando Aspose.Cells. Aspose.Cells ha aggiunto le seguenti classi per leggere e modificare il progetto VBA nel file Excel.

- VbaProject
- VbaModuleCollection
- Modulo Vba

Questo articolo ti mostrerà come modificare il VBA o il codice macro all'interno del file Excel di origine utilizzando Aspose.Cells.

{{% /alert %}} 
## **Esempio**
Il seguente codice di esempio carica il file Excel di origine che contiene un codice VBA o macro seguente

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l'esecuzione del codice di esempio Aspose.Cells, il codice VBA o Macro verrà modificato in questo modo

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Puoi scaricare il[file Excel di origine](5472596.xlsm) e il[file Excel di output](5472597.xlsm) dai link indicati.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






