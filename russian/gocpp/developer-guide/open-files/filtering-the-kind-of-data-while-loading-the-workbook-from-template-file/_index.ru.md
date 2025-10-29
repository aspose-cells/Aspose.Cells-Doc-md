---
title: Фильтрация типа данных при загрузке рабочей книги из шаблонного файла с помощью Golang через C++
linktitle: Фильтрация данных при загрузке книги
type: docs
weight: 400
url: /ru/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Научитесь фильтровать конкретные типы данных при загрузке рабочей книги из шаблонного файла с помощью Aspose.Cells на Golang через C++.
---

{{% alert color="primary" %}}

Иногда вы хотите указать, какой именно вид данных должен быть загружен при построении книги из файла-шаблона. Фильтрация загруженных данных может улучшить производительность для ваших целей, особенно при использовании [LightCells API](/cells/ru/cpp/using-lightcells-api/). Пожалуйста, используйте свойство [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) для этой цели.

{{% /alert %}}

Приведенный ниже образец кода загружает только объекты формы при загрузке книги из [файла шаблона](5115552.xlsx), который вы можете скачать по указанной ссылке. На следующем снимке экрана показано содержимое [файла шаблона](5115552.xlsx) и также объясняется, что данные красного цвета и с желтым фоном не будут загружены, потому что свойство [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) установлено на [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

На следующем снимке экрана показан [выходной PDF](5115555.pdf), который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
