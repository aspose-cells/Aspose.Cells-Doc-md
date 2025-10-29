---
title: Назначение и проверка цифровых подписей с помощью JavaScript через C++
linktitle: Подпись
type: docs
weight: 140
url: /ru/javascript-cpp/assign-and-validate-digital-signatures/
description: Цифровая подпись и проверка файла Excel с помощью Aspose.Cells for JavaScript через C++. Защитите подлинность содержимого рабочей книги с помощью цифровых подписей.
keywords: Цифровая подпись файла Excel, добавление цифровой подписи для Excel с помощью JavaScript через C++, как проверить цифровую подпись JavaScript через C++
---

{{% alert color="primary" %}}  
Цифровая подпись обеспечивает уверенность в том, что файл рабочей книги является действительным и никто его не изменял. Вы можете создать личную цифровую подпись, используя **Microsoft Selfcert.exe** или любой другой инструмент, или приобрести цифровую подпись. После создания цифровой подписи ее необходимо прикрепить к вашей рабочей книге. Прикрепление цифровой подписи аналогично запечатыванию конверта. Если приходит запечатанный конверт, у вас есть уверенность, что никто не затрагивал его содержимое.  
{{% /alert %}}  

## **Введение**  

Используйте диалоговое окно цифровой подписи для прикрепления цифровой подписи. Диалоговое окно цифровой подписи перечисляет действительные сертификаты. Вы можете использовать диалоговое окно цифровой подписи для просмотра сертификатов и выбора нужного. Если у рабочей книги есть цифровая подпись, имя подписи отображается в поле **Имя сертификата**. Если вы щелкнете кнопку **Удалить** в диалоговом окне цифровой подписи, Microsoft Excel также удалит цифровую подпись.  

## **Как добавить цифровую подпись в Excel**  

Aspose.Cells предоставляет модуль [**DigitalSignature**](https://reference.aspose.com/cells/javascript-cpp/digitalsignature/) для выполнения задачи (подписывать и проверять цифровые подписи). Модуль обладает полезными функциями для добавления и проверки цифровых подписей.  

Пожалуйста, посмотрите следующий пример кода, который описывает, как вы можете выполнить задачу, используя скрипт Aspose.Cells for JavaScript через API C++.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Digital Signature: Sign and Verify Workbook</h1>

        <label for="pfxInput">Select PFX Certificate (.pfx):</label>
        <input type="file" id="pfxInput" accept=".pfx" />
        <br /><br />

        <label for="certPassword">Certificate Password:</label>
        <input type="text" id="certPassword" value="aa" />
        <br /><br />

        <label for="signatureComment">Signature Comment:</label>
        <input type="text" id="signatureComment" value="test for sign" />
        <br /><br />

        <button id="runExample">Sign Workbook and Verify</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, DigitalSignature, DigitalSignatureCollection } = AsposeCells;

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
            const pfxInput = document.getElementById('pfxInput');
            if (!pfxInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a .pfx certificate file.</p>';
                return;
            }

            const password = document.getElementById('certPassword').value || "";
            const comment = document.getElementById('signatureComment').value || "";

            // Read the PFX file
            const pfxFile = pfxInput.files[0];
            const pfxArrayBuffer = await pfxFile.arrayBuffer();
            const pfxBytes = new Uint8Array(pfxArrayBuffer);

            // dsc is signature collection that contains one or more signatures needed to sign
            const dsc = new DigitalSignatureCollection();

            // Cert must contain a private key, constructed from the PFX bytes
            const cert = new DigitalSignature(pfxBytes, password, comment, new Date());
            dsc.add(cert);

            // Create a new workbook
            const wb = new Workbook();

            // wb.setDigitalSignature signs all signatures in dsc -> converted to property assignment
            wb.digitalSignature = dsc;

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'newfile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Signed Excel File';

            // Open the file from the generated data to verify signatures
            const wb2 = new Workbook(new Uint8Array(outputData));

            // isDigitallySigned property
            const signedStatus = wb2.isDigitallySigned;

            // Get digitalSignature collection from workbook
            const dsc2 = wb2.digitalSignature;
            let detailsHtml = `<p style="color: green;">Workbook signed: ${signedStatus}</p>`;

            if (dsc2 && dsc2.count > 0) {
                detailsHtml += '<h3>Signatures:</h3><ul>';
                for (let i = 0; i < dsc2.count; i++) {
                    const dst = dsc2.get(i);
                    const dstComments = dst.comments;
                    const dstSignTime = dst.signTime;
                    const dstIsValid = dst.isValid ? dst.isValid() : "N/A";
                    detailsHtml += `<li>
                        <strong>Signature ${i + 1}:</strong><br/>
                        Comments: ${dstComments}<br/>
                        Sign Time: ${dstSignTime}<br/>
                        Is Valid: ${dstIsValid}
                    </li>`;
                }
                detailsHtml += '</ul>';
            } else {
                detailsHtml += '<p>No digital signatures found in the workbook.</p>';
            }

            document.getElementById('result').innerHTML = detailsHtml;
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Добавить цифровую подпись к уже подписанному файлу Excel](/cells/ru/javascript-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Добавить строку подписи на лист](/cells/ru/javascript-cpp/add-signature-line/)  
- [Поддержка XAdES Signature](/cells/ru/javascript-cpp/support-for-xades-signature/)
