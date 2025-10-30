---
title: JavaScript ile ActiveX ComboBox Kontrolünü C++ kullanarak güncelleyin
linktitle: ActiveX ComboBox Kontrolünü Güncelle
type: docs
weight: 170
url: /tr/javascript-cpp/update-activex-combobox-control/
description: C++ ile Aspose.Cells for JavaScript kullanarak ActiveX ComboBox Kontrolü nün değerlerini nasıl okuyup yazacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**
C++ ile Aspose.Cells for JavaScript kullanarak ActiveX ComboBox Kontrolünün değerlerini okuyabilir veya yazabilirsiniz. ActiveX Kontrolüne [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) özelliğiyle erişin ve [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) özelliğiyle türünü kontrol edin, [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) değeri döndürmelidir ve ardından onu [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) nesnesine dönüştürerek çeşitli özelliklerini okuyabilir veya değiştirebilirsiniz.

Lütfen aşağıdaki örnek kodda kullanılan [örnek excel dosyasını](5115124.xlsx) indirin.
## **ActiveX ComboBox Kontrolünü Güncelleme**
Aşağıdaki ekran görüntüsü, [örnek excel dosyası](5115124.xlsx) üzerinde örnek kodun etkisini göstermektedir. Görebileceğiniz gibi, AktifX ComboBox değeri "Bu bir combo box kontrolüdür" olarak güncellenmiştir.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Örnek Kod**
[örnek excel dosyası](5115124.xlsx) içinde bulunan AktifX ComboBox Kontrolünün değerini güncelleyen aşağıdaki örnek kodu takip edin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update ActiveX ComboBox</title>
    </head>
    <body>
        <h1>Update ActiveX ComboBox in Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and first shape
            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value
            if (shape.activeXControl != null) {
                const c = shape.activeXControl;

                if (c instanceof AsposeCells.ComboBoxActiveXControl) {
                    // Type cast ActiveXControl into ComboBoxActiveXControl and change its value
                    const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
                    comboBoxActiveX.value = "This is combo box control with updated value.";
                }
            }

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
