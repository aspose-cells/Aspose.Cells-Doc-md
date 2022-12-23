---
title: Hantera VBA-koder för Excel Macro-Enabled arbetsbok.
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/net/manage-vba-project/
description: Lägg till VBA-modul och ändra VBA eller makro med Aspose.Cells-biblioteket.
---
## **Lägg till en VBA-modul i C#**
{{% alert color="primary" %}}

 Aspose.Cells låter dig lägga till en ny VBA-modul och makrokod med Aspose.Cells. Använd[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) metod för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

Följande exempelkod skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar utdata i formatet XLSM. En gång öppnar du utdatafilen XLSM i Microsoft Excel och klickar på**Utvecklare > Visual Basic** menykommandon kommer du att se en modul som heter "TestModule" och inuti den kommer du att se följande makrokod.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är exempelkoden för att generera utdatafilen XLSM med VBA-modul och makrokod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Ändra VBA eller makro i C#**

{{% alert color="primary" %}} 

Du kan ändra VBA eller makrokod med Aspose.Cells. Aspose.Cells har lagt till följande namnområde och klasser för att läsa och ändra VBA-projektet i Excel-filen.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar dig hur du ändrar VBA- eller makrokoden i källfilen i Excel med Aspose.Cells.

{{% /alert %}} 

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

 Du kan ladda ner[käll Excel-fil](5112508.xlsm) och den[utdata Excel-fil](5112511.xlsm) från de angivna länkarna.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Förhandsämnen**
- [Lägg till en biblioteksreferens till VBA-projektet i arbetsboken](/cells/sv/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Tilldela makro till formulärkontroll](/cells/sv/net/assign-macro-to-form-control/)
- [Kontrollera om den digitala signaturen för VBA-koden är giltig](/cells/sv/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/net/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projekt i en arbetsbok är signerat](/cells/sv/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok](/cells/sv/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/net/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt när en arbetsbok laddas](/cells/sv/net/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/net/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA Project of Excel Workbook](/cells/sv/net/password-protect-the-vba-project-of-excel-workbook/)

