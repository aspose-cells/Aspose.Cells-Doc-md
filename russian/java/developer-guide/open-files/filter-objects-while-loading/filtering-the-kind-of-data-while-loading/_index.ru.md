---
title: Фильтрация типа данных при загрузке книги из файла шаблона
type: docs
weight: 680
url: /ru/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Иногда вы хотите указать, какие данные должны быть загружены при построении книги из файла шаблона. Фильтрация загруженных данных может повысить производительность для вашей специальной цели, особенно при использовании [API LightCells](/cells/ru/java/using-lightcells-api/). Пожалуйста, используйте свойство [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) для этой цели.

{{% /alert %}} 
## **Фильтрация типа данных при загрузке книги из файла шаблона**
В следующем образце кода загружаются только объекты формы при загрузке книги из [файла шаблона](5472556.xlsx), который можно скачать по указанной ссылке.

Ниже показано содержимое [файла шаблона](5472556.xlsx) и также объясняется, что данные красного цвета и с желтым фоном не будут загружены, потому что установлено свойство [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) в [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Ниже показан [выходной PDF](5472554.pdf), который можно скачать по указанной ссылке. Здесь вы можете увидеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
