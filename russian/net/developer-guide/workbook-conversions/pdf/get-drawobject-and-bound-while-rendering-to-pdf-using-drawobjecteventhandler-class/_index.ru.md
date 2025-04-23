---
title: Получить объект DrawObject и Bound при рендеринге в PDF с использованием класса DrawObjectEventHandler
type: docs
weight: 70
url: /ru/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler), который содержит метод [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw). Пользователь может реализовать [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) и использовать метод [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) для получения [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) и границ при рендеринге Excel в PDF или изображение. Вот краткое описание параметров метода [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: объект [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) будет инициализирован и возвращен при рендеринге

- x: слева от [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: сверху [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- ширина: ширина [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- высота: высота [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Если вы рендерите файл Excel в PDF, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) с [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). Аналогично, если вы рендерите файл Excel в изображение, вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) с [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Получите объект DrawObject и Bound при рендеринге в Pdf с использованием класса DrawObjectEventHandler**

Пожалуйста, посмотрите пример кода ниже. Он загружает [образец файла Excel](64716821.xlsx) и сохраняет его в [выходной PDF](64716822.pdf). При рендеринге в PDF используется свойство [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) и захватываются [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) и границы существующих ячеек и объектов, например изображений и т. д. Если тип [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) - ячейка, он выводит ее границы и StringValue. И если тип [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) - изображение, он выводит его границы и имя формы. Смотрите вывод консоли примера кода ниже для получения более подробной информации.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
