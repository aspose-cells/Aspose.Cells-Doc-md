---
title: Фильтрация типа данных при загрузке книги из файла шаблона
type: docs
weight: 400
url: /ru/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Иногда при создании рабочей книги из шаблона или загрузке данных вы хотите указать, какие данные необходимо загрузить. Фильтрация загруженных данных может повысить производительность для вашей конкретной задачи. Используйте для этого свойство [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter).

{{% /alert %}}

Приведенный ниже образец кода загружает только объекты формы при загрузке книги из [файла шаблона](5115552.xlsx), который вы можете скачать по указанной ссылке. На следующем снимке экрана показано содержимое [файла шаблона](5115552.xlsx) и также объясняется, что данные красного цвета и с желтым фоном не будут загружены, потому что свойство [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) установлено на [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показан [выходной PDF](5115555.pdf), который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

