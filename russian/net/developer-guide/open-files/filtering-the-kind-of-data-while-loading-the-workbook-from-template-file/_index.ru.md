---
title: Фильтрация типа данных при загрузке книги из файла шаблона
type: docs
weight: 400
url: /ru/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Иногда вы хотите указать, какой тип данных должен быть загружен при построении книги из файла шаблона. Фильтрация загруженных данных может улучшить производительность для вашей специфической цели, особенно при использовании [API LightCells](/cells/ru/net/using-lightcells-api/). Пожалуйста, используйте свойство [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) для этой цели.

{{% /alert %}}

Приведенный ниже образец кода загружает только объекты формы при загрузке книги из [файла шаблона](5115552.xlsx), который вы можете скачать по указанной ссылке. На следующем снимке экрана показано содержимое [файла шаблона](5115552.xlsx) и также объясняется, что данные красного цвета и с желтым фоном не будут загружены, потому что свойство [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) установлено на [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показан [выходной PDF](5115555.pdf), который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
