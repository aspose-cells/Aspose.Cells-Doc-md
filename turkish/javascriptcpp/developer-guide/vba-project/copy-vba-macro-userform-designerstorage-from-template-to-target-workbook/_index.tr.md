---
title: JavaScript kullanarak Şablondan Hedef Çalışma Kitabına VBA Makro Kullanıcı Formu Tasarımcısı Depolama Kopyala C++ ile
linktitle: Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama
type: docs
weight: 130
url: /tr/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Aspose.Cells for JavaScript kullanarak bir Excel dosyasından diğerine Designer Storage dahil olmak üzere VBA projesini kopyalamayı öğrenin.
---

## **Olası Kullanım Senaryoları**  

Aspose.Cells, bir Excel dosyasından diğerine VBA projesi kopyalamanıza olanak tanır. Bir VBA projesi, çeşitli modül tiplerinden oluşur: Belge, Yordam, Designer vb. Tüm modüller basit kodla kopyalanabilir, ancak Designer modülü için erişilmesi veya kopyalanması gereken Designer Storage adı verilen ek veriler vardır. Aşağıdaki iki yöntem Designer Storage ile ilgilidir.  

- [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-)  
- [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-)  

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**  

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [şablon Excel dosyasından](50528345.xlsm) VBA projesini boş bir çalışma kitabına kopyalar ve [çıktı Excel dosyası](50528346.xlsm) olarak kaydeder. Şablon Excel dosyasının içindeki VBA projesini açarsanız, aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Depolama içerir, bu nedenle [**VbaModuleCollection.designerStorage(string)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#designerStorage-string-) ve [**VbaModuleCollection.addDesignerStorage(string, number[])**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#addDesignerStorage-string-numberarray-) metodları kullanılarak kopyalanacaktır.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

Aşağıdaki ekran görüntüsü, kopyalanan şablon Excel dosyasından çıktı Excel dosyasını ve içeriğini gösterir. Buton 1'e tıkladığınızda VBA Kullanıcı Formu açılır ve kendisi de tıklamada mesaj kutusu gösteren bir komut düğmesine sahiptir.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Örnek Kod**  

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
