---
title: Hantera VBA koder i Excel makroaktiverad arbetsbok
linktitle: Makroprojekt
type: docs
weight: 200
url: /sv/nodejs-cpp/manage-vba-project/
description: Lägg till VBA modul och modifiera VBA eller makro med Aspose.Cells for Node.js via C++.
---

## **Lägg till en VBA-modul i Node.js**
{{% alert color="primary" %}}

Aspose.Cells gör det möjligt att lägga till en ny VBA-modul och makrokod med Aspose.Cells for Node.js via C++. Använd [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-)-metoden för att lägga till den nya VBA-modulen i arbetsboken.

{{% /alert %}}

Följande exempel skapar en ny arbetsbok och lägger till en ny VBA-modul och makrokod och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel och klickar på **Utvecklare > Visual Basic**-menyn, kommer du att se en modul med namnet "TestModule" och därinne följer makrokoden.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Här är exempel på kod för att generera XLSM-filen med VBA-modul och makrokod.

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

## **Modifiera VBA eller makro i Node.js**

{{% alert color="primary" %}} 

Du kan modifiera VBA- eller makrokod med Aspose.Cells for Node.js via C++. Aspose.Cells har lagt till följande modul och klasser för att läsa och modifiera VBA-projektet i Excel-filen.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Den här artikeln visar hur du ändrar VBA eller makrokoden inne i käll-Excel-filen med hjälp av Aspose.Cells.

{{% /alert %}} 

Följande exempel laddar den käll-Excel filen som har VBA- eller makrokod inuti den.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Efter att Aspose.Cells provkoden har körts kommer VBA- eller makrokoden att modifieras på detta sätt

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Du kan ladda ner den [källa Excel-filen](5112508.xlsm) och den [utdata Excel-filen](5112511.xlsm) från de angivna länkarna.

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

## **Fortsatta ämnen**
- [Lägg till en biblioteksreferens till VBA-projektet i arbetsboken](/cells/sv/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Tilldela makro till formulärkontroll](/cells/sv/nodejs-cpp/assign-macro-to-form-control/)
- [Kontrollera om den digitala signaturen av VBA-koden är giltig](/cells/sv/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Kontrollera om VBA-koden är signerad](/cells/sv/nodejs-cpp/check-if-vba-code-is-signed/)
- [Kontrollera om VBA-projektet i en arbetsbok är signerat](/cells/sv/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Kontrollera om VBA-projektet är skyddat och låst för visning](/cells/sv/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken](/cells/sv/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signera digitalt ett VBA-kodprojekt med certifikat](/cells/sv/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportera VBA-certifikat till fil eller ström](/cells/sv/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrera VBA-projekt vid inläsning av en arbetsbok](/cells/sv/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Ta reda på om VBA-projektet är skyddat](/cells/sv/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Lösenordsskydda VBA-projektet för Excel-arbetsbok](/cells/sv/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
