---
title: Hantera VBA koder för Excel makroaktiverat arbetsbok med C++
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/cpp/manage-vba-project/
description: Lägg till VBA modul och ändra VBA eller makro med Aspose.Cells biblioteket i C++.
---

## **Lägg till en VBA-modul i C++**
{{% alert color="primary" %}}

Aspose.Cells låter dig lägga till en ny VBA-modul och makrokod med Aspose.Cells. Använd [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) metoden för att lägga till den nya VBA-modulen i arbetsboken.

{{% /alert %}}

Följande exempel skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar resultatet i XLSM-format. När du öppnar den exporterade XLSM-filen i Microsoft Excel och klickar på kommando menyn **Utvecklarverktyg > Visual Basic**, kommer du att se en modul som heter "TestModule" och inuti den ser du följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Här är provkoden för att generera utdata i XLSM-format med VBA-modul och makrokod.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ändra VBA eller makro i C++**

{{% alert color="primary" %}} 

Du kan modifiera VBA eller makrokod med hjälp av Aspose.Cells. Aspose.Cells har lagt till följande namespace och klasser för att läsa och modifiera VBA-projektet i Excel-filen.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA eller makrokoden inne i käll-Excel-filen med hjälp av Aspose.Cells.

{{% /alert %}} 

Följande exempel laddar in källexcelfilen som innehåller följande VBA- eller makrokod:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Efter körning av Aspose.Cells exempel kod, kommer VBA- eller makrokoden att ändras så här:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Du kan ladda ner den [källa Excel-filen](5112508.xlsm) och den [utdata Excel-filen](5112511.xlsm) från de angivna länkarna.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Avancerade ämnen**
- [Lägg till ett bibliotek i VBA-projekt i arbetsboken](/cells/sv/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Tilldela makro till formulärkontroll](/cells/sv/cpp/assign-macro-to-form-control/)
- [Kontrollera om den digitala signaturen av VBA-koden är giltig](/cells/sv/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/cpp/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projektet i en arbetsbok är signerat](/cells/sv/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken](/cells/sv/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt vid inläsning av en arbetsbok](/cells/sv/cpp/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/cpp/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA-projektet för Excel-arbetsbok](/cells/sv/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
