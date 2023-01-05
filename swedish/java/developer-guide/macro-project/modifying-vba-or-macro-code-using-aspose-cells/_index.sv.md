---
title: Ändra VBA eller makrokod med Aspose.Cells
type: docs
weight: 90
url: /sv/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

Du kan ändra VBA eller makrokod med Aspose.Cells. Aspose.Cells har lagt till följande klasser för att läsa och ändra VBA-projektet i Excel-filen.

- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar dig hur du ändrar VBA- eller makrokoden i källfilen i Excel med Aspose.Cells.

{{% /alert %}} 
## **Exempel**
Följande exempelkod laddar källfilen i Excel som har en följande VBA- eller makrokod inuti

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Efter exekvering av Aspose.Cells exempelkod kommer VBA- eller makrokoden att ändras så här

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Du kan ladda ner[käll Excel-fil](5472596.xlsm) och den[utdata Excel-fil](5472597.xlsm) från de angivna länkarna.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






