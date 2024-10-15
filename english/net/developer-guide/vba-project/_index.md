---
title: Manage VBA codes of Excel Macro-Enabled workbook.
linktitle: Macro Project
type: docs
weight: 200
url: /net/manage-vba-project/
description: Add VBA Module and Modify VBA or Macro with Aspose.Cells library.
---

## **Add a VBA Module in C#**
{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells. Please use the [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) method to add the new VBA Module inside the workbook

{{% /alert %}}

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once, you will open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Here is the sample code to generate the output XLSM file with VBA Module and Macro Code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modify VBA or Macro in C#**

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells. Aspose.Cells has added the following namespace and classes to read and modify the VBA project in the Excel file.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 

The following sample code loads the source Excel file which has a following VBA or Macro code inside it

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

After the execution of Aspose.Cells sample code, the VBA or Macro code will be modified like this

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Advance topics**
- [Add a library reference to VBA project in workbook](/cells/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Assign Macro to Form Control](/cells/net/assign-macro-to-form-control/)
- [Check if Digital Signature of VBA Code is Valid](/cells/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](/cells/net/check-if-vba-code-is-signed/)
- [Check if VBA project in a Workbook is Signed](/cells/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](/cells/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](/cells/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitally Sign a VBA Code Project with Certificate](/cells/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](/cells/net/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while loading a workbook](/cells/net/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](/cells/net/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](/cells/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}