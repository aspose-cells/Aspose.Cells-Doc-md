---
title: Получить или установить класс идентификатор встроенного OLE объекта с помощью JavaScript через C++
linktitle: Получение или установка идентификатора класса встроенного объекта OLE
type: docs
weight: 200
url: /ru/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Узнайте, как получать или устанавливать класс идентификатор встроенных OLE объектов с помощью Aspose.Cells через C++.
---

## **Возможные сценарии использования**  
Aspose.Cells предоставляет свойство [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--), которое можно использовать для получения или установки класс-идентификатора встроенного OLE-объекта. Идентификаторы класса OLE-объектов представляют собой GUIDы, то есть Глобальные Уникальные Идентификаторы. GUID всегда длиной 16 байт; поэтому, идентификаторы класса тоже длинной 16 байт. Они часто описаны в реестре Windows и предоставляют приложению информацию о том, как открывать встроенные OLE-объекты с различными встроенными ресурсами внутри клиентского приложения.

## **Получение или установка идентификатора класса встроенного объекта OLE**  
Следующий скриншот показывает идентификатор класса объекта OLE, т.е. GUID, который был считан из [пример файла Excel](5115190.xls), содержащего встроенный PowerPoint OLE-объект.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Образец кода**  
Пожалуйста, смотрите следующий пример кода, выполненный с [примером файла Excel](5115190.xls), и его выводом в консоль, который печатает идентификатор класса OLE-объекта, т.е. GUID. Выведенный GUID точно такой же, как отображается на скриншоте.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Вывод в консоль**  
Это вывод консоли указанного выше примера кода при выполнении с [примером файла Excel](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
