---
title: Modifica del codice VBA o Macro utilizzando Aspose.Cells
type: docs
weight: 90
url: /it/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

È possibile modificare il codice VBA o Macro utilizzando Aspose.Cells. Aspose.Cells ha aggiunto le seguenti classi per leggere e modificare il progetto VBA nel file Excel.

- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo ti mostrerà come modificare il codice VBA o Macro all'interno del file Excel di origine usando Aspose.Cells.

{{% /alert %}} 
## **Esempio**
Il seguente codice di esempio carica il file Excel di origine che contiene il seguente codice VBA o Macro al suo interno

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l'esecuzione del codice di esempio di Aspose.Cells, il codice VBA o Macro sarà modificato in questo modo

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

È possibile scaricare il [file Excel di origine](5472596.xlsm) e il [file Excel di output](5472597.xlsm) dai link forniti.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






{{< app/cells/assistant language="java" >}}
