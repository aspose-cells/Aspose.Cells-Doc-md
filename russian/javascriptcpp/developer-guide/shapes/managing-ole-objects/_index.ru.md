---
title: Управление объектами OLE с помощью JavaScript через C++
linktitle: Управление объектами OLE
type: docs
weight: 50
url: /ru/javascript-cpp/managing-ole-objects/
description: Узнайте, как управлять объектами OLE в Aspose.Cells for JavaScript через C++. Добавляйте, извлекайте и изменяйте объекты OLE внутри таблиц.
---

## **Введение**  

OLE (Object Linking and Embedding) — это платформа для технологии составных документов. Вкратце, составной документ — это что-то вроде рабочего стола, который может содержать визуальные и информационные объекты всех видов: текст, календари, анимации, звук, движущееся видео, 3D, постоянно обновляемые новости, элементы управления и т.д. Каждый объект рабочего стола — это независимый программный элемент, который может взаимодействовать с пользователем и также обмениваться данными с другими объектами на рабочем столе.  

OLE поддерживается многими программами и используется для обеспечения совместного использования контента, созданного в одной программе, в другой. Например, вы можете вставить документ Microsoft Word в Microsoft Excel. Чтобы посмотреть, какие типы контента можно вставлять, нажмите **Объект** в меню **Вставка**. В списке **Тип объекта** отображаются только программы, установленные на компьютере и поддерживающие объекты OLE.  

### **Вставка объектов OLE в лист**  

Aspose.Cells for JavaScript через C++ поддерживает добавление, извлечение и управление объектами OLE в таблицах. Поэтому в Aspose.Cells есть класс [**OleObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/oleobjectcollection), используемый для добавления нового объекта OLE в коллекцию. Другой класс, [**OleObject**](https://reference.aspose.com/cells/javascript-cpp/oleobject), представляет объект OLE. Он содержит важные члены:  

- Свойство [**imageData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#imageData--) задает изображение (иконку) в виде массива байтов. Это изображение отображается для отображения OLE-объекта в листе.  
- Свойство [**objectData**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#objectData--) задает данные объекта в виде массива байтов. Эти данные будут отображаться в соответствующей программе при двойном щелчке по иконке OLE-объекта.  

Нижеприведенный пример показывает, как добавить объект(ы) OLE в лист Excel.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add OLE Object Example</title>
    </head>
    <body>
        <h1>Add OLE Object Example</h1>
        <p>
            Select an image to display for the OLE object (e.g., logo.jpg) and a file to embed into the OLE object (e.g., book1.xls).
        </p>
        <label>Image (for OLE display): <input type="file" id="imageInput" accept="image/*" /></label>
        <br/>
        <label>Object to embed (e.g., .xls): <input type="file" id="objectInput" accept=".xls,.xlsx,.doc,.docx,.pdf" /></label>
        <br/>
        <button id="runExample">Add OLE Object and Save</button>
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
            const imageInput = document.getElementById('imageInput');
            const objectInput = document.getElementById('objectInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file for the OLE display.</p>';
                return;
            }
            if (!objectInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select a file to embed into the OLE object.</p>';
                return;
            }

            // Read files
            const imageFile = imageInput.files[0];
            const objectFile = objectInput.files[0];

            const imageBuffer = await imageFile.arrayBuffer();
            const objectBuffer = await objectFile.arrayBuffer();

            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Add an Ole object into the worksheet with the image shown in MS Excel.
            // Position: row 14, column 3, width 200, height 220 (same as JavaScript example)
            sheet.oleObjects.add(14, 3, 200, 220, new Uint8Array(imageBuffer));

            // Set embedded ole object data (converted setter to property assignment)
            sheet.oleObjects.get(0).objectData = new Uint8Array(objectBuffer);

            // Save the excel file (Excel97To2003 format to match .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">OLE object added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **Извлечение объектов OLE в книге**  

В следующем примере показано, как извлекать объекты OLE в книге. Пример получает различные объекты OLE из существующего файла XLS и сохраняет различные файлы (DOC, XLS, PPT, PDF и т. д.) на основе типа формата файла объекта OLE.  

После выполнения кода мы можем сохранить разные файлы на основе их соответствующих типов формата объектов OLE.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Extract OLE Objects</title>
    </head>
    <body>
        <h1>Extract OLE Objects from Excel</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb" />
        <button id="runExample">Extract OLE Objects</button>
        <div id="downloadContainer"></div>
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
            const downloadContainer = document.getElementById('downloadContainer');
            const result = document.getElementById('result');
            downloadContainer.innerHTML = '';
            result.innerHTML = '';

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the OleObject Collection in the first worksheet.
            const worksheet = workbook.worksheets.get(0);
            const oles = worksheet.oleObjects;

            // Loop through all the oleobjects and extract each object.
            for (let i = 0; i < oles.count; i++) {
                const ole = oles.get(i);

                // Specify the output filename.
                let ext = 'jpg';

                // Specify each file format based on the oleobject format type.
                switch (ole.fileFormatType) {
                    case AsposeCells.FileFormatType.Doc:
                        ext = "doc";
                        break;
                    case AsposeCells.FileFormatType.Xlsx:
                        ext = "xlsx";
                        break;
                    case AsposeCells.FileFormatType.Ppt:
                        ext = "ppt";
                        break;
                    case AsposeCells.FileFormatType.Pdf:
                        ext = "pdf";
                        break;
                    case AsposeCells.FileFormatType.Unknown:
                        ext = "jpg";
                        break;
                    default:
                        ext = "bin";
                        break;
                }

                const fileName = `ole_${i}.${ext}`;

                // Save the oleobject as a new excel file if the object type is xlsx.
                if (ole.fileFormatType === AsposeCells.FileFormatType.Xlsx) {
                    const ms = new Uint8Array(ole.objectData);
                    const oleBook = new Workbook(ms);
                    oleBook.settings.isHidden = false;
                    const outputData = oleBook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = `Excel_File${i}.out.xlsx`;
                    link.textContent = `Download Excel_File${i}.out.xlsx`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                } else {
                    // Create the files based on the oleobject format types.
                    const data = ole.objectData;
                    const blob = new Blob([data]);
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    downloadContainer.appendChild(link);
                }
            }

            result.innerHTML = '<p style="color: green;">OLE object extraction completed. Use the links above to download the files.</p>';
        });
    </script>
</html>
```  

### **Извлечение встроенного файла MOL**  

Aspose.Cells for JavaScript через C++ поддерживает извлечение объектов необычных типов, таких как MOL (файл молекулярных данных, содержащий информацию о атомах и связях). Следующий пример кода демонстрирует извлечение встроенного файла MOL и его сохранение на диск с помощью этого [образца файла Excel](94896196.xlsx).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Extract OLE Objects Example</title>
    </head>
    <body>
        <h1>Extract OLE Objects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            let index = 1;

            const worksheets = workbook.worksheets;
            const sheetCount = worksheets.count;
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            for (let i = 0; i < sheetCount; i++) {
                const sheet = worksheets.get(i);
                const oles = sheet.oleObjects;
                const oleCount = oles.count;
                for (let j = 0; j < oleCount; j++) {
                    const ole = oles.get(j);
                    const data = ole.objectData;
                    const blob = new Blob([data], { type: 'application/octet-stream' });
                    const url = URL.createObjectURL(blob);
                    const fileName = `OleObject${index}.mol`;
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = fileName;
                    link.textContent = `Download ${fileName}`;
                    link.style.display = 'block';
                    resultDiv.appendChild(link);
                    index++;
                }
            }

            if (!resultDiv.hasChildNodes()) {
                resultDiv.innerHTML = '<p>No OLE objects found in the workbook.</p>';
            } else {
                const info = document.createElement('p');
                info.style.color = 'green';
                info.textContent = 'OLE objects extracted. Click the links to download the extracted .mol files.';
                resultDiv.insertBefore(info, resultDiv.firstChild);
            }
        });
    </script>
</html>
```  

## **Продвинутые темы**  
- [Доступ и изменение отображаемой метки связанного объекта OLE](/cells/ru/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)  
- [Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells](/cells/ru/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)  
- [Извлечение объектов OLE из книги](/cells/ru/javascript-cpp/extract-ole-objects-from-workbook/)  
- [Получение или установка идентификатора класса встроенного объекта OLE](/cells/ru/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)  
- [Вставка файла WAV в качестве объекта OLE](/cells/ru/javascript-cpp/inserting-a-wav-file-as-an-ole-object/)
