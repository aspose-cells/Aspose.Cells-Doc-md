---
title: Получение предупреждений при загрузке файла Excel с помощью Node.js через C++
linktitle: Получать предупреждения при загрузке файла Excel
type: docs
weight: 110
url: /ru/nodejs-cpp/get-warnings-while-loading-excel-file/
description: Узнайте, как ловить предупреждения при загрузке файла Excel, используя Aspose.Cells for Node.js via C++. Эффективно обработайте поврежденные, но загружаемые рабочие книги.
---

## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая несколько повреждена, но все же загружается. В таких случаях Aspose.Cells выбрасывает предупреждения при загрузке. Вы можете ловить эти предупреждения, реализовав интерфейс [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) и установив свойство [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--).

## **Получение предупреждений при загрузке файла Excel**

Следующий пример кода показывает, как получать предупреждения при загрузке файла Excel. Код загружает [пример файла excel](sampleDuplicateDefinedName.xlsx), который вызывает предупреждение [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) при загрузке. Это предупреждение перехватывается методом [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-), который выводит сообщения предупреждений в консоль. Затем рабочая книга сохраняется как [выходной файл excel](outputDuplicateDefinedName.xlsx). Если открыть исходный файл в Microsoft Excel, он также отобразит это предупреждение, как показано на скриншоте. Также рекомендуем проверить вывод в консоль для лучшего понимания.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **Вывод в консоль**

Ниже приведен вывод консольного вывода вышеуказанного кода при выполнении с предоставленным [образцом файла Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
