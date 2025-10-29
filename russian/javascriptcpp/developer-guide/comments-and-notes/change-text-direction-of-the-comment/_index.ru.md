---
title: Изменить направление текста комментария с помощью JavaScript через C++
linktitle: Изменение направления текста комментария
type: docs
weight: 10
url: /ru/javascript-cpp/change-text-direction-of-the-comment/
description: Узнайте, как изменить направление текста комментариев с помощью Aspose.Cells for JavaScript через C++. Эффективно настройте параметры выравнивания комментариев.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям добавлять комментарии к ячейкам для добавления дополнительной информации и выделения данных. Разработчикам может понадобиться настроить комментарий, чтобы указать параметры выравнивания и направления текста. Aspose.Cells for JavaScript через C++ предоставляет API для выполнения этой задачи.

{{% /alert %}}

Aspose.Cells for JavaScript через C++ предоставляет свойство [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) для установки направления текста комментария. Следующий пример кода демонстрирует использование свойства [**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--) для установки направления текста комментария.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
