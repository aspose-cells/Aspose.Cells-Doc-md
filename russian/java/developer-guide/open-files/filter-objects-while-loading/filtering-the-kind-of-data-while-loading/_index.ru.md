---
title: Фильтрация данных при загрузке книги из файла шаблона
type: docs
weight: 680
url: /ru/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 Иногда вам нужно указать, какие данные следует загружать при создании книги из файла шаблона. Фильтрация загружаемых данных может повысить производительность для ваших специальных целей, особенно при использовании[API-интерфейсы LightCells](/cells/ru/java/using-lightcells-api/) . Пожалуйста, используйте[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) имущество для этой цели.

{{% /alert %}} 
## **Фильтрация данных при загрузке книги из файла шаблона**
Следующий пример кода загружает только объекты формы при загрузке книги из[файл шаблона](5472556.xlsx)который вы можете скачать по указанной ссылке.

На следующем снимке экрана показано[файл шаблона](5472556.xlsx) содержимое, а также объясняет, что данные красного цвета и желтого фона не будут загружены, поскольку[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)свойство установлено на[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![дело:изображение_альтернативный_текст](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показано[вывод PDF](5472554.pdf) который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данных красного цвета и желтого фона нет, но все фигуры есть.

![дело:изображение_альтернативный_текст](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
