---
title: Автоматическое обновление объекта OLE через Microsoft Excel с помощью Aspose.Cells
type: docs
weight: 270
url: /ru/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет свойство [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) для обновления объекта OLE при открытии файла Excel в Microsoft Excel. Благодаря этому свойству объект OLE будет отображать правильное изображение OLE, созданное Microsoft Excel.

{{% /alert %}}

Следующий образец кода загружает [образец файла Excel](5115231.xlsx), который содержит ненастоящее изображение OLE. Объект OLE на самом деле является документом Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Microsoft Word. Но если вы откроете [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное изображение OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
