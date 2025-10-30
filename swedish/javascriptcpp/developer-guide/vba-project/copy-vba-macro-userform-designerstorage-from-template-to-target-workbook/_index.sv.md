---
title: Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok med JavaScript via C++
linktitle: Kopiera VBA makro UserForm DesignerStorage från mallen till mål arbetsboken
type: docs
weight: 130
url: /sv/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Lär dig hur du kopierar ett VBA projekt, inklusive Designer Storage, från en Excel fil till en annan med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Aspose.Cells låter dig kopiera ett VBA-projekt från en Excel-fil till en annan Excel-fil. Ett VBA-projekt består av olika typer av moduler dvs. Dokument, Procedur, Designer etc. Alla moduler kan kopieras med enkel kod, men för Designer-modulen finns det extra data kallad Designer Storage som måste nås eller kopieras. Följande två metoder hanterar Designer Storage.  

- [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**  

Se följande kodexempel. Det kopierar VBA-projektet från [mallens Excel-fil](50528345.xlsm) till en tom arbetsbok och sparar den som [utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet i mallen för Excel-fil ser du en användarform som visas nedan. User Form består av Designer Storage, så den kommer att kopieras med hjälp av [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)- och [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)-metoder.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Följande skärmbild visar utdata Excel-filen och dess innehåll som kopierades från mall Excel-filen. När du klickar på Knapp 1 öppnas VBA-användarformuläret som i sig har en kommando-knapp som visar ett meddelandefönster vid klick.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Exempelkod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy VBA Designer UserForm Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils, SheetType, VbaModuleType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel macro-enabled (.xlsm) file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create empty target workbook
            const target = new Workbook();

            // Load the Excel file containing VBA-Macro Designer User Form
            const templateFile = new Workbook(new Uint8Array(arrayBuffer));

            // Copy all template worksheets to target workbook
            const sheets = templateFile.worksheets;
            const sheetCount = sheets.count;
            for (let i = 0; i < sheetCount; i++) {
                const ws = sheets.get(i);
                if (ws.type === SheetType.Worksheet) {
                    const s = target.worksheets.add(ws.name);
                    s.copy(ws);

                    // Put message in cell A2 of the target worksheet
                    s.cells.get("A2").putValue("VBA Macro and User Form copied from template to target.");
                }
            }

            // Copy the VBA-Macro Designer UserForm from Template to Target 
            const modules = templateFile.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const vbaItem = modules.get(i);
                if (vbaItem.name === "ThisWorkbook") {
                    // Copy ThisWorkbook module code
                    target.vbaProject.modules.get("ThisWorkbook").codes = vbaItem.codes;
                } else {
                    console.log(vbaItem.name);

                    let vbaMod = 0;
                    const sheet = target.worksheets.sheetByCodeName(vbaItem.name);
                    if (sheet.isNull()) {
                        vbaMod = target.vbaProject.modules.add(vbaItem.type, vbaItem.name);
                    } else {
                        vbaMod = target.vbaProject.modules.add(sheet);
                    }

                    target.vbaProject.modules.get(vbaMod).codes = vbaItem.codes;

                    if (vbaItem.type === AsposeCells.VbaModuleType.Designer) {
                        // Get the data of the user form i.e. designer storage
                        const designerStorage = modules.getDesignerStorage(vbaItem.name);

                        // Add the designer storage to target Vba Project
                        target.vbaProject.modules.addDesignerStorage(vbaItem.name, designerStorage);
                    }
                }
            }

            // Saving the modified Excel file
            const outputData = target.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDesignerForm.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA Designer UserForm copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
