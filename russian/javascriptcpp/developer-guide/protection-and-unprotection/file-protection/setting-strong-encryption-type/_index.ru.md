---
title: Настройка типа сильного шифрования с помощью JavaScript через C++
linktitle: Установка сильного типа шифрования
type: docs
weight: 60
url: /ru/javascript-cpp/setting-strong-encryption-type/
description: Узнайте, как установить типы сильного шифрования для файлов Excel с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) позволяет вам шифровать и защищать паролем электронные таблицы. Для этого используются алгоритмы, предоставленные поставщиком криптосервисов. Криптосервис (или CSP) представляет собой набор криптографических алгоритмов с различными свойствами. CSP по умолчанию - "Совместимое с Office 97/2000". Это CSP с некоторыми публично известными проблемами безопасности. Таблицы, защищенные "слабым шифрованием (XOR)" или шифрованием типа "Совместимое с Office 97/2000", могут быть легко взломаны.

Чтобы преодолеть эту проблему, используйте один из сильных типов шифрования, предоставленных Microsoft Excel. Вы можете изменить тип шифрования на самый сильный из доступных CSP. Для сильного шифрования требуется минимальная длина ключа 128 бит, например, 'Microsoft Strong Cryptographic Provider'.

Вы также можете шифровать и защищать паролем файлы Excel с сильным типом шифрования с использованием API Aspose.Cells.

{{% /alert %}}  
## **Применение шифрования с помощью Microsoft Excel**  
Для реализации шифрования файлов в Microsoft Excel (например, 2007):

1. В меню **Сервис** выберите **Параметры**.  
1. Выберите вкладку **Безопасность**.  
1. Введите значение для поля **Пароль для открытия**.  
1. Нажмите **Дополнительно**.  
1. Выберите тип шифрования и подтвердите пароль.  

## **Применение шифрования с помощью Aspose.Cells**  
Приведенные ниже примеры кода применяют сильное шифрование к файлу и устанавливают пароль.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
