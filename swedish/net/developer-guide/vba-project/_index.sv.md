---
title: Hantera Excel makrobokkoderna.
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/net/manage-vba-project/
description: Lägg till VBA modul och modifiera VBA eller makro med Aspose.Cells biblioteket.
---

## **Lägg till en VBA-modul i C#**
{{% alert color="primary" %}}

Aspose.Cells tillåter att du lägger till en ny VBA-modul och makrokod med hjälp av Aspose.Cells. Använd [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)-metoden för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

Följande provkod skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar utdata i XLSM-format. När du öppnar utdata-XLSM-filen i Microsoft Excel och klickar på **Utvecklare > Visuell grund**-menykommandon kommer du att se en modul som heter "TestModule" och inuti den kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är provkoden för att generera utdata i XLSM-format med VBA-modul och makrokod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modifiera VBA eller makro i C#**

{{% alert color="primary" %}} 

Du kan modifiera VBA eller makrokod med hjälp av Aspose.Cells. Aspose.Cells har lagt till följande namespace och klasser för att läsa och modifiera VBA-projektet i Excel-filen.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA eller makrokoden inne i käll-Excel-filen med hjälp av Aspose.Cells.

{{% /alert %}} 

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

Du kan ladda ner den [källa Excel-filen](5112508.xlsm) och den [utdata Excel-filen](5112511.xlsm) från de angivna länkarna.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Fortsatta ämnen**
- [Lägg till en biblioteksreferens till VBA-projektet i arbetsboken](/cells/sv/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Tilldela makro till formulärkontroll](/cells/sv/net/assign-macro-to-form-control/)
- [Kontrollera om den digitala signaturen av VBA-koden är giltig](/cells/sv/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/net/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projektet i en arbetsbok är signerat](/cells/sv/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken](/cells/sv/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/net/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt vid inläsning av en arbetsbok](/cells/sv/net/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/net/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA-projektet för Excel-arbetsbok](/cells/sv/net/password-protect-the-vba-project-of-excel-workbook/)

