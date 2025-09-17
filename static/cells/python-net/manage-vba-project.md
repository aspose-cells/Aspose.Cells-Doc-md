##Manage VBA codes of Excel Macro-Enabled workbook.
Add VBA Module and Modify VBA or Macro with Aspose.Cells for Python via .NET library.
## **Add a VBA Module in Python**
Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells for Python via .NET. Please use the [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) method to add the new VBA Module inside the workbook
The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.
Sub ShowMessage()
MsgBox "Welcome to Aspose!"
End Sub
Here is the sample code to generate the output XLSM file with VBA Module and Macro Code.
## **Modify VBA or Macro in Python**
You can modify VBA or Macro Code using Aspose.Cells for Python via .NET. Aspose.Cells for Python via .NET has added the following namespace and classes to read and modify the VBA project in the Excel file.
- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule
This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells for Python via .NET.
The following sample code loads the source Excel file which has a following VBA or Macro code inside it
Sub Button1_Click()
MsgBox "This is test message."
End Sub
After the execution of Aspose.Cells for Python via .NET sample code, the VBA or Macro code will be modified like this
Sub Button1_Click()
MsgBox "This is Aspose.Cells message."
End Sub
You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.
## **Advance topics**
- [Add a library reference to VBA project in workbook](https://docs.aspose.com/cells/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Check if Digital Signature of VBA Code is Valid](https://docs.aspose.com/cells/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](https://docs.aspose.com/cells/python-net/check-if-vba-code-is-signed/)
- [Check if VBA project in a Workbook is Signed](https://docs.aspose.com/cells/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](https://docs.aspose.com/cells/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Digitally Sign a VBA Code Project with Certificate](https://docs.aspose.com/cells/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](https://docs.aspose.com/cells/python-net/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while loading a workbook](https://docs.aspose.com/cells/python-net/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](https://docs.aspose.com/cells/python-net/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](https://docs.aspose.com/cells/python-net/password-protect-the-vba-project-of-excel-workbook/)
