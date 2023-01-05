---
title: Lägger till VBA-modul och kod med Aspose.Cells
type: docs
weight: 20
url: /sv/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells låter dig lägga till en ny VBA-modul och makrokod med Aspose.Cells. Använd[**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) metod för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

## **Lägger till VBA-modul och kod med Aspose.Cells**

Följande exempelkod skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar utdata i formatet XLSM. En gång öppnar du utdatafilen XLSM i Microsoft Excel och klickar på**Utvecklare > Visual Basic** menykommandon kommer du att se en modul som heter "TestModule" och inuti den kommer du att se följande makrokod.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Exempelkod

Här är en exempelkod för att generera utdatafilen XLSM med VBA-modul och makrokod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
