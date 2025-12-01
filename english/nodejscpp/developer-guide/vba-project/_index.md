---
title: Manage VBA codes of Excel Macro-Enabled workbook
linktitle: Macro Project
type: docs
weight: 200
url: /nodejs-cpp/manage-vba-project/
description: Add VBA Module and Modify VBA or Macro with Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Add a VBA Module in Node.js**
{{% alert color="primary" %}}

Aspose.Cells allows you to add a new VBA Module and Macro Code using Aspose.Cells for Node.js via C++. Please use the [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) method to add the new VBA Module inside the workbook

{{% /alert %}}

The following sample code creates a new workbook and adds a new VBA Module and Macro Code and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel and click the **Developer > Visual Basic** menu commands, you will see a module named "TestModule" and inside it, you will see the following macro code.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Here is the sample code to generate the output XLSM file with VBA Module and Macro Code.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Modify VBA or Macro in Node.js**

{{% alert color="primary" %}} 

You can modify VBA or Macro Code using Aspose.Cells for Node.js via C++. Aspose.Cells has added the following module and classes to read and modify the VBA project in the Excel file.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

This article will show you how to change the VBA or Macro Code inside the source Excel file using Aspose.Cells.

{{% /alert %}} 

The following sample code loads the source Excel file which has the following VBA or Macro code inside it

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

After the execution of Aspose.Cells sample code, the VBA or Macro code will be modified like this

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

You can download the [source Excel file](5112508.xlsm) and the [output Excel file](5112511.xlsm) from the given links.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Advance topics**
- [Add a library reference to VBA project in workbook](/cells/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assign Macro to Form Control](/cells/nodejs-cpp/assign-macro-to-form-control/)
- [Check if Digital Signature of VBA Code is Valid](/cells/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Check if VBA Code is Signed](/cells/nodejs-cpp/check-if-vba-code-is-signed/)
- [Check if VBA project in a Workbook is Signed](/cells/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Check if VBA Project is Protected and Locked for Viewing](/cells/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook](/cells/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitally Sign a VBA Code Project with Certificate](/cells/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Export VBA Certificate to File or Stream](/cells/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filter VBA Project while loading a workbook](/cells/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Find out if VBA Project is Protected](/cells/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Password Protect the VBA Project of Excel Workbook](/cells/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
