---
title: Получить DrawObject и Bound при рендеринге в PDF с помощью класса DrawObjectEventHandler
type: docs
weight: 70
url: /ru/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Возможные сценарии использования**

 Aspose.Cells предоставляет абстрактный класс[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) который имеет[**Рисовать()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)метод. Пользователь может реализовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) и использовать[**Рисовать()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) метод, чтобы получить[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)и Bound при рендеринге Excel в PDF или изображение. Вот краткое описание параметров[**Рисовать()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)метод.

-  рисоватьОбъект:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) будет инициализирован и возвращен при рендеринге

- х: слева от[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- г: Вверху[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- ширина: Ширина[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- высота: Высота[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Если вы конвертируете файл Excel в PDF, вы можете использовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)класс с[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . Точно так же, если вы визуализируете файл Excel в изображение, вы можете использовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)класс с[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Получить DrawObject и Bound при рендеринге в Pdf с использованием класса DrawObjectEventHandler**

 См. следующий пример кода. Он загружает[образец файла Excel](64716821.xlsx) и сохраняет его как[вывод PDF](64716822.pdf). При рендеринге в PDF он использует[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)имущество и захватывает[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) и Ограничение существующих ячеек и объектов, например, изображений и т. д. Если[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) тип Cell, он печатает свои Bound и StringValue. И если[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)тип — изображение, он печатает имя привязки и формы. Дополнительные сведения см. в выводе на консоль примера кода, приведенного ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
