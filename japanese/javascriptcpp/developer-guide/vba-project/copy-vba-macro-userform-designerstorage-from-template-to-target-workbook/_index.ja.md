---
title: テンプレートからターゲットブックへVBAマクロUserForm DesignerStorageをコピーするJavaScript版C++
linktitle: テンプレートから対象のブックへVBAマクロのUserForm DesignerStorageをコピー
type: docs
weight: 130
url: /ja/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Aspose.Cells for JavaScriptを使用して、一つのExcelファイルから別のExcelファイルへVBAプロジェクト（Designer Storage含む）をコピーする方法を学びます。
---

## **可能な使用シナリオ**  

Aspose.Cellsを使用すると、一つのExcelファイルから別のExcelファイルにVBAプロジェクトをコピーできます。VBAプロジェクトは、ドキュメント、手続き型、デザイナーなど、さまざまなタイプのモジュールで構成されています。すべてのモジュールはシンプルなコードでコピー可能ですが、デザイナーモジュールには追加のデータであるデザイナーストレージがあります。以下の二つの方法は、デザイナーストレージに関わっています。  

- [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **テンプレートからターゲットワークブックへのVBAマクロUserForm DesignerStorageのコピー**  

以下のサンプルコードをご覧ください。このコードは、[テンプレートExcelファイル](50528345.xlsm)から空のブックにVBAプロジェクトをコピーし、それを[出力Excelファイル](50528346.xlsm)として保存します。テンプレートExcelファイルのVBAプロジェクトを開くと、以下のようなユーザーフォームが見えます。ユーザーフォームはデザイナーストレージから構成されており、[**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)と[**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)の方法を使ってコピーされます。  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

以下のスクリーンショットは、テンプレートExcelファイルからコピーされた出力Excelファイルとその内容を示しています。ボタン1をクリックすると、VBAユーザーフォームが開き、その中のコマンドボタンをクリックするとメッセージボックスが表示されます。  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **サンプルコード**  

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
