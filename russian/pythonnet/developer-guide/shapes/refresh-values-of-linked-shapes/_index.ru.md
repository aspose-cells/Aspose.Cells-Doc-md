---
title: Обновить значения связанных форм
type: docs
weight: 3200
url: /ru/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Иногда у вас есть связанная фигура в файле Excel, которая связана с ячейкой. В Microsoft Excel изменение значения связанной ячейки также изменяет значение связанной фигуры. Это также работает хорошо с Aspose.Cells для Python via .NET, если вы хотите сохранить рабочую книгу в форматах XLS или XLSX. Однако, если вы хотите сохранить рабочую книгу в формате PDF или HTML, вам потребуется вызвать метод [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) для обновления значения связанной фигуры.

{{% /alert %}}

## Пример

Следующий скриншот показывает исходный файл Excel, используемый в приведенном ниже примере кода. В нем есть связанная картинка, связанная с ячейками A1 по E4. Мы изменим значение ячейки B4 с помощью Aspose.Cells for Python via .NET, а затем вызовем [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) метод для обновления значения картинки и сохранения в PDF формате.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Вы можете скачать [исходный файл Excel](95584291.xlsx) и [выходной PDF](95584292.pdf)  по следующим ссылкам.

### Код C# для обновления значений связанных форм

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
