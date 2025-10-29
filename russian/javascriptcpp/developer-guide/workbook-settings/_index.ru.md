---
title: Управляйте настройками файлов Excel с помощью JavaScript через C++
linktitle: Настройки книги
type: docs
weight: 185
url: /ru/javascript-cpp/workbook-settings/
description: Управляйте настройками файлов Excel с помощью Aspose.Cells for JavaScript через C++.
---

## **Обзор настроек книги**
Работа с файлами Excel включает различные настройки, которые могут быть управляемы программно с помощью Aspose.Cells for JavaScript через C++. В этом документе описывается, как эффективно управлять этими настройками.

## **Возможные сценарии использования**
Следующие сценарии показывают, когда может потребоваться управление настройками книги:
- Настройка параметров отображения
- Установка режима вычислений
- Настройка параметров макета страницы

## **Управление настройками рабочей книги с помощью Aspose.Cells for JavaScript через C++**
Этот пример демонстрирует управление настройками книги, такими как параметры вычислений и отображения.

1. Создайте новую книгу или откройте существующую.
2. Настройте параметры книги в соответствии с вашими требованиями.
3. Сохраните книгу для сохранения изменений.

### **Пример кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Workbook Settings Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Create a new workbook
            const workbook = new Workbook();

            // Access the settings of the workbook
            const settings = workbook.settings;
            settings.calculationMode = 1; // Manual calculation

            // Display options
            settings.showGridLines = false; // Disable gridlines

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookSettingsExample.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Ключевые свойства и методы настройки книги**
Aspose.Cells for JavaScript через C++ предоставляет ряд свойств и методов для настройки параметров рабочей книги:
- **Workbook.settings**: доступ к настройкам рабочей книги.
- **Settings.calculationMode**: устанавливает режим вычислений для рабочей книги.
- **Settings.showGridLines**: включает или отключает отображение сетки.

## **Заключение**
Управление настройками рабочей книги в Aspose.Cells for JavaScript через C++ простое и предоставляет множество вариантов для настройки поведения файла Excel. Используя доступные настройки, вы можете адаптировать рабочую книгу под свои конкретные требования.
