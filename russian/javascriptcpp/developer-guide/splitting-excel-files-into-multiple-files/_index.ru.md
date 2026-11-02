---
title: Разделение файлов Excel на несколько файлов
linktitle: Разделение файлов Excel на несколько файлов
description: Aspose.Cells for JavaScript via C++ — это библиотека JavaScript via C++ для работы с файлами электронных таблиц, которая поддерживает разделение одного файла Excel на несколько файлов. В этой статье будет представлено, как разделять файлы Excel, копируя каждый рабочий лист в отдельную рабочую книгу и копируя определённые диапазоны ячеек в другие рабочие книги.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ library, таблица, разделить файл Excel, копировать рабочий лист, копировать диапазон, несколько рабочих книг, сохранить как отдельные файлы
type: docs
weight: 195
url: /ru/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ поддерживает разделение одного файла Excel на несколько файлов. Существует два основных способа сделать это: (1) копировать каждый рабочий лист исходной рабочей книги в новую рабочую книгу и сохранять каждую как отдельный файл, и (2) копировать определённый диапазон ячеек из листа в новую рабочую книгу. Оба подхода полезны, когда необходимо распределить подмножества данных, создать более мелкие отчёты для разных получателей или изолировать данные для отдельной обработки.
{{% /alert %}}

## **Введение**
Существует множество реальных сценариев, когда разработчику необходимо разбить один файл Excel на несколько более мелких файлов. Например, рабочая книга может содержать один рабочий лист на каждый отдел, и каждому руководителю отдела нужно получить только свой лист. В иных случаях может потребоваться извлечь конкретную таблицу или блок данных из листа и отправить его как отдельный файл по электронной почте, не раскрывая остальную часть рабочей книги. Большие консолидированные рабочие книги также могут потребовать разделения на более мелкие части для удобства работы, более быстрой загрузки или последующей обработки другими системами.  
Aspose.Cells for JavaScript via C++ предоставляет два гибких подхода для этой задачи. Первый подход перебирает каждый рабочий лист в исходной рабочей книге и копирует его содержимое в новый экземпляр `Workbook`, сохраняя каждый как отдельный файл. Второй подход сосредоточен на конкретном диапазоне ячеек внутри листа и копирует только этот диапазон в новую рабочую книгу. В обоих случаях общий процесс одинаков: загрузить исходную рабочую книгу с помощью класса `Workbook`, получить доступ к нужным данным через объекты `Worksheet` и `Cells`, перенести содержимое в целевую `Workbook` и затем сохранить целевую книгу на диск.

## **Разделение файла Excel путем копирования каждого рабочего листа в новую рабочую книгу**

### **Обзор подхода**
В этом подходе исходная рабочая книга открывается один раз, после чего для каждого `Worksheet` из её коллекции `Worksheets` создаётся новая целевая `Workbook`. Содержимое рабочего листа‑источника копируется в первый рабочий лист целевой рабочей книги, а целевая книга сохраняется в файл, имя которого берётся из имени рабочего листа‑источника. В результате получаем один выходной файл на каждый рабочий лист, каждый из которых содержит данные единственного рабочего листа‑источника.  
Метод подходит, когда каждый рабочий лист в исходной рабочей книге представляет логически независимую единицу информации (например, отдел, регион, месяц или продуктовую линейку) и её нужно передавать или обрабатывать отдельно.

### **Шаги**
Следующие шаги описывают, как разделить файл Excel, копируя каждый рабочий лист в новую рабочую книгу:
1. Откройте исходный файл Excel, создав объект `Workbook` и передав в конструктор путь к файлу.  
2. Переберите коллекцию `Workbook.Worksheets` с помощью цикла `for` или `for...of`, чтобы обработать каждый `Worksheet` в исходном файле.  
3. Внутри цикла создайте новый объект целевой `Workbook` (пустую рабочую книгу) для текущего рабочего листа.  
5. Скопируйте содержимое рабочего листа‑источника в целевой лист. Это можно выполнить, перебирая ячейки коллекции `Cells` рабочего листа‑источника и записывая их значения в соответствующие ячейки целевого листа, либо используя метод `Cells.Copy` для передачи целого диапазона сразу.  
6. Сформируйте путь к выходному файлу, включив в него имя рабочего листа‑источника (например, `dataDir + worksheet.Name + ".xls"`), чтобы каждый создаваемый файл имел уникальное имя.  
7. Вызовите метод `Workbook.Save` целевой книги, чтобы записать файл на диск.  
8. Повторяйте шаги 3‑7 для следующего рабочего листа, пока не будут обработаны все листы.

### **Пример кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Ожидаемый результат — набор новых файлов в каталоге данных, по одному файлу на каждый рабочий лист исходной рабочей книги. Каждый файл назван в соответствии с соответствующим листом‑источником и содержит данные (и при желании форматирование) этого единственного листа.

## **Разделение файла Excel путем копирования диапазона в новую рабочую книгу**

### **Обзор подхода**
Иногда данные, которые требуется разделить, не соответствуют целому листу, а представляют собой конкретный прямоугольный регион листа, например `A1:D10` или именованный диапазон, представляющий определённую таблицу. В этих случаях копирование целых листов является избыточным, и нужен более точный подход: определить исходный диапазон, скопировать только его в новую рабочую книгу и сохранить новый файл.  
Этот подход идеален, когда нужно извлечь одну таблицу, блок отчёта или область данных из большого листа, отбрасывая всё несвязанное содержание. Он также полезен для экспорта выбранных пользователем областей листа в виде самостоятельных файлов.

### **Шаги**
Следующие шаги описывают, как разделить файл Excel, копируя определённый диапазон в новую рабочую книгу:
1. Откройте исходный файл Excel, создав объект `Workbook` с указанием пути к файлу.  
2. Получите целевой `Worksheet`, содержащий диапазон для копирования, либо по индексу (например, первый лист), либо по имени из коллекции `Worksheets`.  
3. Определите диапазон для копирования. Это может быть жёстко заданный диапазон ячеек, например `A1:C10`, именованный диапазон, полученный через коллекцию `Worksheet.Cells`, или диапазон, созданный методом `Worksheet.Cells.CreateRange`.  
4. Создайте новый объект целевой `Workbook`.  
5. Получите первый `Worksheet` целевой рабочей книги (лист по умолчанию).  
6. Скопируйте исходный диапазон в целевой лист, обычно начиная с ячейки `A1`. Для копирования целого диапазона можно использовать метод `Cells.Copy` коллекции целевых `Cells`, либо перебрать ячейки исходного диапазона и записать их значения в целевые ячейки с помощью `PutValue`. При необходимости можно передать `CopyOptions`, чтобы управлять тем, что копируется (только значения, значения и стили, формулы и т.д.).  
7. Сохраните целевую рабочую книгу в новый путь на диске, вызвав метод `Workbook.Save`.

### **Пример кода**
Ожидаемый результат — один новый файл в каталоге данных, содержащий только значения (и при желании форматирование) указанного диапазона, извлечённого из исходной рабочей книги. У целевого файла нет связи с другими данными исходного файла; он содержит лишь извлечённый диапазон, начинающийся с ячейки `A1` первого листа.

## Related Articles
- [Добавить поля фильтра к сводной таблице в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/add-page-field-in-pivot-table/)
- [Применить стили к сводным таблицам в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/apply-style-to-pivot-table/)
- [Изменить макет полей страниц в сводной таблице](/cells/ru/javascript-cpp/change-page-field-layout/)
- [Преобразовать Sparkline в изображение и HTML в Aspose.Cells for JavaScript via C++](/cells/ru/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Преобразование Excel в формат OFD](/cells/ru/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}