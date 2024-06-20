---
title: Aggiunta Modulo VBA e Codice usando Aspose.Cells
type: docs
weight: 20
url: /it/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di aggiungere un nuovo Modulo VBA e Codice Macro utilizzando Aspose.Cells. Si prega di utilizzare il metodo [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) per aggiungere il nuovo Modulo VBA all'interno del workbook

{{% /alert %}}

## **Aggiunta Modulo VBA e Codice usando Aspose.Cells**

Il seguente codice di esempio crea un nuovo workbook e aggiunge un nuovo modulo VBA e codice macro e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel e fare clic sui comandi del menu **Sviluppo > Visual Basic**, verrà visualizzato un modulo chiamato "TestModule" e al suo interno verrà visualizzato il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Codice di esempio

Ecco un codice di esempio per generare il file XLSM di output con Modulo VBA e Codice Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
