---
title: Фильтрация данных при загрузке книги из файла шаблона
type: docs
weight: 400
url: /ru/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 Иногда вам нужно указать, какие данные следует загружать при создании книги из файла шаблона. Фильтрация загружаемых данных может повысить производительность для ваших специальных целей, особенно при использовании[API-интерфейсы LightCells](/cells/ru/net/using-lightcells-api/) . Пожалуйста, используйте[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) имущество для этой цели.

{{% /alert %}}

Следующий пример кода загружает только объекты формы при загрузке книги из[файл шаблона](5115552.xlsx) который вы можете скачать по указанной ссылке. На следующем снимке экрана показано[файл шаблона](5115552.xlsx)содержимое, а также объясняет, что данные красного цвета и желтого фона не будут загружены, потому что[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)свойство установлено на[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![дело:изображение_альтернативный_текст](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показано[вывод PDF](5115555.pdf) который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данных красного цвета и желтого фона нет, но все фигуры есть.

![дело:изображение_альтернативный_текст](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
