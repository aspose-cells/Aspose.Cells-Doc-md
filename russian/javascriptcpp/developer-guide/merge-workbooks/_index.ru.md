---
title: Объединение нескольких рабочих книг в одну с помощью JavaScript через C++
linktitle: Слияние книг
type: docs
weight: 66
url: /ru/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Узнайте, как объединить несколько рабочих книг в одну с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Иногда необходима объединить рабочие книги с различным содержимым, таким как изображения, диаграммы и данные, в одну книгу. Aspose.Cells for JavaScript через C++ поддерживает эту функцию. Эта статья показывает, как создать консольное приложение и объединить рабочие книги с помощью нескольких простых строк кода, используя Aspose.Cells.

{{% /alert %}}

## **Объединение книг с изображениями и диаграммами**

Пример кода объединяет две рабочие книги в одну с помощью Aspose.Cells for JavaScript через C++. Код загружает исходные рабочие книги, использует метод [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) для их объединения и сохраняет итоговую книгу.

### **Исходные книги**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Выходные книги**

- [combined.xlsx](5473095.xlsx)

### **Скриншоты**

Ниже приведены скриншоты исходной и выходной книг.

{{% alert color="primary" %}}

Вы можете использовать любые исходные книги. Эти изображения приведены только в целях иллюстрации.

{{% /alert %}}

**Первый лист книги с диаграммами - столбцы** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Второй лист книги с диаграммами - линейный** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Первый лист книги с картинками - изображение** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Все три листа в объединенной книге - столбцы, линейный, изображение** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Объединение нескольких листов в один](/cells/ru/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Объединение файлов](/cells/ru/javascript-cpp/merge-files/)
