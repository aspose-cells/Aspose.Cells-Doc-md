---
title: Hantera Excel makrobokkoderna.
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/python-net/manage-vba-project/
description: Lägg till VBA modul och ändra VBA eller Macro med Aspose.Cells för Python via .NET biblioteket.
---

## **Lägg till en VBA-modul i Python**
{{% alert color="primary" %}}

Aspose.Cells tillåter dig att lägga till en ny VBA-modul och makokod med Aspose.Cells för Python via .NET. Använd [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/)-metoden för att lägga till den nya VBA-modulen i arbetsboken

{{% /alert %}}

Följande provkod skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar utdata i XLSM-format. När du öppnar utdata-XLSM-filen i Microsoft Excel och klickar på **Utvecklare > Visuell grund**-menykommandon kommer du att se en modul som heter "TestModule" och inuti den kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är provkoden för att generera utdata i XLSM-format med VBA-modul och makrokod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **Ändra VBA eller Macro i Python**

{{% alert color="primary" %}} 

Du kan ändra VBA- eller makokod med Aspose.Cells för Python via .NET. Aspose.Cells för Python via .NET har tillagt följande namespace och klasser för att läsa och ändra VBA-projektet i Excel-filen.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA- eller makokoden inuti käll-Excel-filen med Aspose.Cells för Python via .NET.

{{% /alert %}} 

Följande provkod laddar käll-Excel-filen som har följande VBA- eller makrokod inuti den

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Efter att ha kört Aspose.Cells för Python via .NET exempelprogram, kommer VBA- eller makokoden att ändras så här

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Du kan ladda ner den [källa Excel-filen](5112508.xlsm) och den [utdata Excel-filen](5112511.xlsm) från de angivna länkarna.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Fortsatta ämnen**
- [Lägg till en biblioteksreferens till VBA-projektet i arbetsboken](/cells/sv/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Kontrollera om den digitala signaturen av VBA-koden är giltig](/cells/sv/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/python-net/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projektet i en arbetsbok är signerat](/cells/sv/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/python-net/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt vid inläsning av en arbetsbok](/cells/sv/python-net/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/python-net/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA-projektet för Excel-arbetsbok](/cells/sv/python-net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="python-net" >}}
