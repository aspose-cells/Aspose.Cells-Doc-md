---
title: Aggiunta di modulo e codice VBA utilizzando Aspose.Cells
type: docs
weight: 20
url: /it/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice macro utilizzando Aspose.Cells. Utilizzare il[**Cartella di lavoro.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) metodo per aggiungere il nuovo modulo VBA all'interno della cartella di lavoro

{{% /alert %}}

## **Aggiunta di modulo e codice VBA utilizzando Aspose.Cells**

Il seguente codice di esempio crea una nuova cartella di lavoro e aggiunge un nuovo modulo VBA e codice macro e salva l'output nel formato XLSM. Una volta, aprirai il file XLSM di output in Microsoft Excel e fai clic su**Sviluppatore > Visual Basic** comandi di menu, vedrai un modulo chiamato "TestModule" e al suo interno vedrai il seguente codice macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Codice di esempio

Ecco un codice di esempio per generare il file XLSM di output con il modulo VBA e il codice macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
