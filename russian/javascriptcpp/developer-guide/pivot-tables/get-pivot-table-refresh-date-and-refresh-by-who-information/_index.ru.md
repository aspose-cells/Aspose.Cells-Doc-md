---
title: Получить дату обновления сводной таблицы и информацию о том, кем она обновлялась
type: docs
weight: 100
url: /ru/javascript-cpp/get-pivot-table-refresh-date-and-refresh-by-who-information/
description: Как получить дату обновления сводной таблицы и информацию о том, кто обновил, с помощью Aspose.Cells for JavaScript для C++.
keywords: Aspose.Cells for JavaScript для Excel, библиотека Excel JavaScript, получение даты обновления сводной таблицы и информации о пользователе, обновившем ее, с помощью Aspose.Cells for JavaScript.
---

{{% alert color="primary" %}}

Теперь Aspose.Cells for JavaScript для C++ поддерживает получение даты обновления и информации о том, кто обновил из книги.

{{% /alert %}}

## **Как получить дату обновления сводной таблицы и информацию о том, кем было выполнено обновление**
[**PivotTable.refreshDate**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshDate--) возвращает дату последнего обновления сводного отчета. Аналогично свойство [**PivotTable.refreshedByWho**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshedByWho--) возвращает имя пользователя, который последний раз обновлял отчет. Приведенный ниже пример демонстрирует эту функцию, и образец файла можно загрузить по следующей ссылке.

[SourcePivotTable.xlsx](77496335.xlsx)

**Пример кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Info</title>
    </head>
    <body>
        <h1>Pivot Table Information</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);
            const pivotTable = worksheet.pivotTables.get(0);

            const refreshedByWho = pivotTable.refreshedByWho;
            const refreshDate = pivotTable.refreshDate;

            console.log("Pivot table refresh by who = " + refreshedByWho);
            console.log("Pivot table refresh date = " + refreshDate);

            document.getElementById('result').innerHTML = `
                <p>Pivot table refresh by who = ${refreshedByWho}</p>
                <p>Pivot table refresh date = ${refreshDate}</p>
            `;
        });
    </script>
</html>
```
