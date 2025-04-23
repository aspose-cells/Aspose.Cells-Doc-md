---
title: Обновить значения связанных форм
type: docs
weight: 3000
url: /ru/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Иногда в вашем файле Excel есть связанная форма, связанная с некоторой ячейкой. В Microsoft Excel изменение значения связанной ячейки также изменяет значение связанной формы. Это также работает хорошо с Aspose.Cells, если вы хотите сохранить ваш рабочий книгу в формате XLS или XLSX. Однако, если вы хотите сохранить вашу рабочую книгу в формате PDF или HTML, то вам нужно вызвать метод [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--), чтобы обновить значение связанной формы.

{{% /alert %}}

## Пример

На следующем скриншоте показан исходный файл Excel, используемый в примере кода ниже. В нем есть связанное **Изображение 1** связанное с ячейкой A1. Мы изменим значение ячейки A1 с помощью Aspose.Cells, а затем вызовем метод [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) для обновления значения **Изображения 1** и сохранения его в формате PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Вы можете загрузить [исходный файл Excel](5472956.xlsx) и [выходной PDF](5472955.pdf) по указанным ссылкам.

### Java-код для обновления значений связанных форм

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
