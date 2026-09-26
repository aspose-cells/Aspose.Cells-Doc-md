---
title: Manage VBA Codes of Excel Macro-Enabled Workbook with Golang via C++
linktitle: Macro Project
type: docs
weight: 200
url: /go-cpp/manage-vba-project/
description: Add VBA Module and Modify VBA or Macro with Aspose.Cells library in C++.
---

## **Add a VBA Module in C++**
{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells. Please use the [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/go-cpp/vbamodulecollection/add_worksheet/) method to add the new VBA Module inside the workbook.

{{% /alert %}}

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Here is the sample code to generate the output XLSM file with VBA Module and Macro Code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VbaProject.go" >}}

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VbaProject-1.go" >}}

## **Advanced Topics**
- [Add a Library Reference to VBA Project in Workbook](/cells/go-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assign Macro to Form Control](/cells/go-cpp/assign-macro-to-form-control/)
- [Check if Digital Signature of VBA Code is Valid](/cells/go-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](/cells/go-cpp/check-if-vba-code-is-signed/)
- [Check if VBA Project in a Workbook is Signed](/cells/go-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](/cells/go-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](/cells/go-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitally Sign a VBA Code Project with Certificate](/cells/go-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](/cells/go-cpp/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while Loading a Workbook](/cells/go-cpp/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](/cells/go-cpp/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](/cells/go-cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="go" >}}
