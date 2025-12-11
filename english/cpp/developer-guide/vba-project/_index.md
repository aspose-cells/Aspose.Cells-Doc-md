---
title: Manage VBA Codes of Excel Macro-Enabled Workbook with C++
linktitle: Macro Project
type: docs
weight: 200
url: /cpp/manage-vba-project/
description: Add VBA Module and Modify VBA or Macro with Aspose.Cells library in C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Add a VBA Module in C++**
{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells. Please use the [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) method to add the new VBA Module inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Here is the sample code to generate the output XLSM file with VBA Module and Macro Code.

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

## **Modify VBA or Macro in C++**

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells. Aspose.Cells has added the following namespace and classes to read and modify the VBA project in the Excel file.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 

The following sample code loads the source Excel file which has the following VBA or Macro code inside it:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

After the execution of Aspose.Cells sample code, the VBA or Macro code will be modified like this:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.

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

## **Advanced Topics**
- [Add a Library Reference to VBA Project in Workbook](/cells/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assign Macro to Form Control](/cells/cpp/assign-macro-to-form-control/)
- [Check if Digital Signature of VBA Code is Valid](/cells/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](/cells/cpp/check-if-vba-code-is-signed/)
- [Check if VBA Project in a Workbook is Signed](/cells/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](/cells/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](/cells/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitally Sign a VBA Code Project with Certificate](/cells/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](/cells/cpp/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while Loading a Workbook](/cells/cpp/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](/cells/cpp/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](/cells/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
