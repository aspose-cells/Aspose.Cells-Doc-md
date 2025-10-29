---
title: Ограничение количества сгенерированных страниц при преобразовании Excel в PDF
type: docs
weight: 180
url: /ru/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить количество создаваемых страниц при преобразовании Excel в PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Ограничить количество создаваемых страниц при сохранении Excel в PDF с помощью Python, установить количество создаваемых страниц при преобразовании Excel в PDF с помощью Python, Установить количество создаваемых страниц при преобразовании Excel в PDF с помощью Python, Управлять количеством создаваемых страниц для Excel в формате PDF в Python
---

{{% alert color="primary" %}}

Иногда вы хотите напечатать диапазон страниц в выходной PDF-файл. Aspose.Cells для Python via .NET имеет возможность установить ограничение на количество создаваемых страниц при преобразовании электронной таблицы Excel в формат PDF.

{{% /alert %}}

## **Ограничение количества сгенерированных страниц**

В следующем примере показано, как отображать диапазон страниц (3 и 4) в файле Microsoft Excel в формате PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Если электронная таблица содержит формулы, лучше всего вызвать метод [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) прямо перед преобразованием ее в PDF. Это обеспечит пересчет значений, зависящих от формулы, и верное отображение значений в выходном файле.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
