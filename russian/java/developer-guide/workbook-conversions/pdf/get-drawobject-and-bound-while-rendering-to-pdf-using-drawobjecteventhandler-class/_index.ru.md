---
title: Получить объект DrawObject и Bound при рендеринге в PDF с использованием класса DrawObjectEventHandler
type: docs
weight: 60
url: /ru/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler), у которого есть метод [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-). Пользователь может реализовать [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) и использовать метод [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) для получения [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) и **Bound** при рендеринге Excel в PDF или изображение. Вот краткое описание параметров метода [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) будет инициализирован и возвращен при рендеринге

- x: слева от [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: сверху [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- ширина: ширина [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- высота: высота [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Если вы преобразуете файл Excel в PDF, то вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) с [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Аналогично, если вы преобразуете файл Excel в изображение, то вы можете использовать класс [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) с [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Получите объект DrawObject и Bound при рендеринге в Pdf с использованием класса DrawObjectEventHandler**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец Excel-файла](64716843.xlsx) и сохраняет его в формате [PDF файла](64716842.pdf). При преобразовании в PDF используется свойство [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) и захватываются [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) и **Bound** существующих ячеек и объектов, таких как изображения и т. д. Если тип объекта drawObject является Ячейкой (Cell), то печатается ее Bound и StringValue. Если тип объекта drawObject является Изображением (Image), то печатается его Bound и Имя формы. Пожалуйста, ознакомьтесь с консольным выводом приведенного ниже образца кода для получения более подробной справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
