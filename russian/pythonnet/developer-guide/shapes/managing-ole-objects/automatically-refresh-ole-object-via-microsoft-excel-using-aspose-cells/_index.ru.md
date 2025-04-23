---
title: Автоматическое обновление Ole объекта
type: docs
weight: 270
url: /ru/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET предоставляет свойство [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) для обновления OLE-объекта при открытии файла Excel в Microsoft Excel. Благодаря этому свойству, OLE-объект будет отображать правильное изображение OLE, созданное Microsoft Excel.

{{% /alert %}}

Следующий образец кода загружает [образец файла Excel](5115231.xlsx), который содержит ненастоящее изображение OLE. Объект OLE на самом деле является документом Microsoft Word, но образец файла Excel показывает изображение животного вместо изображения Microsoft Word. Но если вы откроете [выходной файл Excel](5115225.xlsx), вы увидите, что Microsoft Excel отображает правильное изображение OLE.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
