---
title: VBA kodlarını Yönetme — Excel Makro Etkin çalışma kitabı
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/javascript-cpp/manage-vba-project/
description: VBA Modülü Ekle ve Aspose.Cells for JavaScript ile C++ kullanarak VBA veya Makroyu Değiştir.
---

## **JavaScript üzerinden C++ ile VBA Modülü Ekle**
{{% alert color="primary" %}}

Aspose.Cells, C++ kullanarak Aspose.Cells for JavaScript ile yeni bir VBA Modülü ve Makro Kodu eklemenize olanak tanır. Lütfen çalışma kitabına yeni VBA Modülü eklemek için [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) yöntemini kullanın

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM formatında kaydeder. Çıktı XLSM dosyasını Microsoft Excel’de açıp **Geliştirici > Görsel Basic** menü komutlarına tıklarsanız, "TestModule" adlı bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **JavaScript üzerinden C++ ile VBA veya Makroyu Değiştir**

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript ile C++ kullanarak VBA veya Makro Kodu değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projesini okumak ve değiştirmek için aşağıdaki modülleri ve sınıfları eklemiştir.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyasındaki VBA veya Makro Kodunu değiştirmeyi gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, içeriğinde VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilmiş olacaktır

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Verilen bağlantılardan [kaynak Excel dosyasını](5112508.xlsm) ve [çıktı Excel dosyasını](5112511.xlsm) indirebilirsiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Çalışma Kitabındaki VBA projeye bir kütüphane referansı ekle](/cells/tr/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makroyu Form Kontrole Ata](/cells/tr/javascript-cpp/assign-macro-to-form-control/)
- [VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et](/cells/tr/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalı Olup Olmadığını Kontrol Et](/cells/tr/javascript-cpp/check-if-vba-code-is-signed/)
- [Çalışma Kitabındaki VBA projesinin imzalı olup olmadığını kontrol edin](/cells/tr/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korunup Görüntülemeye Kilitli Olup Olmadığını Kontrol Edin](/cells/tr/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama](/cells/tr/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Sertifika ile Bir VBA Kod Projesini Dijital Olarak İmzalama](/cells/tr/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarma](/cells/tr/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Bir çalışma kitabı yüklenirken VBA Projesini Filtreleme](/cells/tr/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korunup Korunmadığını Bulma](/cells/tr/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruma](/cells/tr/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
