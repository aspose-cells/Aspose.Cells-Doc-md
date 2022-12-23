---
title: Получить DrawObject и Bound при рендеринге на PDF с помощью класса DrawObjectEventHandler
type: docs
weight: 60
url: /ru/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Возможные сценарии использования**

Aspose.Cells предоставляет абстрактный класс[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) который имеет[**рисовать()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) метод. Пользователь может реализовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)и использовать[**рисовать()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) метод получения[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)и**Граница**при рендеринге Excel в PDF или изображение. Вот краткое описание параметров[**рисовать()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) метод.

-  рисоватьОбъект:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)будет инициализирован и возвращен при рендеринге

- х: слева от[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- г: Вверху[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- ширина: Ширина[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- высота: Высота[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Если вы визуализируете файл Excel на PDF, вы можете использовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)класс с[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Точно так же, если вы визуализируете файл Excel в изображение, вы можете использовать[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)класс с[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Получить DrawObject и Bound при рендеринге в Pdf с помощью класса DrawObjectEventHandler**

См. следующий пример кода. Он загружает[образец файла Excel](64716843.xlsx)и сохраняет его как[вывод PDF](64716842.pdf). При рендеринге в PDF он использует[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)имущество и захватывает[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) и**Граница**существующих ячеек и объектов, например изображений и т. д. Если тип drawObject равен Cell, он печатает свои значения Bound и StringValue. И если типом drawObject является изображение, он печатает свое имя привязки и формы. Дополнительные сведения см. в выводе на консоль примера кода, приведенного ниже.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
