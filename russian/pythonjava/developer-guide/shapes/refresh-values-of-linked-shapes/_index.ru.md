---
title: Обновить значения связанных форм
type: docs
weight: 3200
url: /ru/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Иногда у вас есть связанная форма в файле Excel, связанная с какой-то ячейкой. В Microsoft Excel, изменение значения связанной ячейки также изменяет значение связанной формы. Это также работает отлично с Aspose.Cells, если вы хотите сохранить свою книгу в формате XLS или XLSX. Однако, если вы хотите сохранить свою книгу в формате PDF или HTML, тогда вам придется вызвать метод [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) для обновления значения связанной формы.

{{% /alert %}}

## Пример

На следующем снимке экрана показан исходный файл Excel, используемый в приведенном ниже образце кода. В нем есть связанное изображение, связанное с ячейками от A1 до E4. Мы изменим значение ячейки B4 с помощью Aspose.Cells, а затем вызовем метод [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) для обновления значения изображения и сохранения его в формате PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Вы можете скачать [исходный файл Excel](sampleRefreshValueOfLinkedShapes.xlsx) и [выходной PDF](95584292.pdf) по предоставленным ссылкам.

### Код C# для обновления значений связанных форм

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
