---
title: Modifiera VBA eller Makrokod med Aspose.Cells
type: docs
weight: 90
url: /sv/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Du kan ändra VBA- eller Makrokod med Aspose.Cells. Aspose.Cells har lagt till följande klasser för att läsa och ändra VBA-projektet i Excel-filen.

- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA eller makrokoden inne i käll-Excel-filen med hjälp av Aspose.Cells.

{{% /alert %}} 
## **Exempel**
Följande provkod laddar käll-Excel-filen som har följande VBA- eller makrokod inuti den

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Efter att Aspose.Cells provkoden har körts kommer VBA- eller makrokoden att modifieras på detta sätt

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Du kan ladda ner [käll-excel-filen](5472596.xlsm) och [output-excel-filen](5472597.xlsm) från de angivna länkarna.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






