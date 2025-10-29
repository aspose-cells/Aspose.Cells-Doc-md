---
title: Автоматически обновлять Ole объекты через Microsoft Excel с помощью Golang через C++
linktitle: Автоматическое обновление Ole объекта
type: docs
weight: 270
url: /ru/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Изучите, как автоматически обновлять Ole объекты в Microsoft Excel с помощью Aspose.Cells с Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) для обновления Ole-объекта при открытии файла Excel в Microsoft Excel. Благодаря этому свойству Ole-объект будет отображать правильное изображение Ole, созданное Microsoft Excel.

{{% /alert %}}

Следующий пример кода загружает [образец файла Excel](5115231.xlsx), в котором есть нереальное Ole-изображение. Ole-объект на самом деле — документ Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Word. Однако, если открыть [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное Ole-изображение.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
