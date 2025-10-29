---
title: Удалить неиспользуемые стили внутри книги
type: docs
weight: 340
url: /ru/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Неиспользуемые стили в файле Excel занимают не только место, но и вызывают снижение производительности при конвертации в другие форматы, такие как PDF, HTML и др. Aspose.Cells для Python via .NET предоставляет метод [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) для удаления всех неиспользуемых стилей внутри рабочей книги.

{{% /alert %}}

В следующем коде объясняется использование [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). Код загружает [файл-шаблон Excel](5115520.xlsx), который вы можете скачать по предоставленной ссылке. Он содержит неиспользуемый стиль с именем **AsposeStyle**, этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
