---
title: Lägga till VBA modul och kod med hjälp av Aspose.Cells
type: docs
weight: 20
url: /sv/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells tillåter att du lägger till en ny VBA-modul och makkod med Aspose.Cells. Använd metoden [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

## **Lägga till VBA-modul och kod med hjälp av Aspose.Cells**

Följande provkod skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar utdata i XLSM-format. När du öppnar utdata-XLSM-filen i Microsoft Excel och klickar på **Utvecklare > Visuell grund**-menykommandon kommer du att se en modul som heter "TestModule" och inuti den kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Exempelkod

Här är exempelkod för att generera utdatafilen XLSM med VBA-modul och makrokod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
