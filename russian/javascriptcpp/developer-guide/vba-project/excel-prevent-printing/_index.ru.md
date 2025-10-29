---
title: Как предотвратить печать файла Excel с помощью JavaScript через C++
linktitle: Как предотвратить пользователей от печати файлов Excel
type: docs
weight: 600
url: /ru/javascript-cpp/how-to-prevent-printing-excel/
description: Узнайте, как предотвратить печать файлов Excel, используя Aspose.Cells for JavaScript через C++. 
keywords: печать excel, предотвращение печати excel, как предотвратить пользователей от печати excel, excel предотвращение печати, предотвращение печати рабочей книги, Предотвращение печати всей книги с помощью VBA.
---

## **Возможные сценарии использования**  
В нашей ежедневной работе в файле Excel может содержаться важная информация; чтобы защитить внутренние данные от распространения, компания не разрешит их печать. Этот документ расскажет, как предотвратить печать файлов Excel другими.  

## **Как предотвратить пользователей от печати файла в MS-Excel**  
Вы можете применить следующий VBA-код для защиты вашего конкретного файла от печати.  
1. Откройте свою книгу, которую вы не разрешаете печатать.  
1. Выберите вкладку "Developer" на ленте Excel и нажмите кнопку "View Code" в разделе "Controls". Или удерживайте клавиши ALT + F11 для открытия окна Microsoft Visual Basic for Applications.  
<br>  
<img src="1.png" width=70% />  
1. Затем в левом окне Обозревателя проекта дважды щелкните ЭтотРабочийКнига, чтобы открыть модуль, и добавьте некоторые VBA-коды.  
<br>  
<img src="2.png" width=70% />  
1. Затем сохраните и закройте этот код, вернитесь в рабочую книгу, и теперь при попытке распечатать файл образца выводится предупреждение:  
<br>  
<img src="3.png" width=70% />  

## **Как предотвратить печать файла Excel с помощью Aspose.Cells for JavaScript через C++**  

Следующий пример кода показывает, как предотвратить печать файла Excel:  

1. Загрузите [образец файла](sample.xlsx).  
1. Получите объект VbaModuleCollection из свойства VbaProject рабочей книги.  
1. Получите объект VbaModule через имя "ThisWorkbook".  
1. Установите свойство codes объекта VbaModule.  
1. Сохраните образец файла в формате [xlsm](out.xlsm).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update VBA Module Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing VBA project and its modules
            const modules = workbook.vbaProject.modules;
            const module = modules.get("ThisWorkbook");

            // Setting module codes (converted from setCodes -> codes assignment)
            module.codes = "Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n";

            // Saving the modified workbook as macro-enabled workbook
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
