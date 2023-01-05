---
title: Автоматически обновлять объект OLE через Microsoft Excel, используя Aspose.Cells
type: docs
weight: 270
url: /ru/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**ОлеОбъект.Автозагрузка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) свойство для обновления объекта OLE при открытии файла Excel в Microsoft Excel. Из-за этого свойства объект OLE будет отображать правильное изображение OLE, созданное Microsoft Excel.

{{% /alert %}}

 Следующий пример кода загружает[образец эксель файла](5115231.xlsx) который имеет ненастоящее изображение OLE. Объект OLE на самом деле является документом Word Microsoft, но образец файла Excel показывает изображение животного вместо изображения Microsoft Word. Но если открыть[выходной файл excel](5115225.xlsx), вы увидите Microsoft Excel отображает правильное изображение OLE.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
