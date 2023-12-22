---
title: Ограничить количество создаваемых страниц — преобразование Excel до PDF
type: docs
weight: 180
url: /ru/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Узнайте, как ограничить количество страниц, создаваемых при рендеринге Excel, до PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

Иногда вам нужно напечатать диапазон страниц в выходной файл PDF. Aspose.Cells for Python via .NET имеет возможность установить ограничение на количество страниц, создаваемых при преобразовании электронной таблицы Excel в формат файла PDF.

{{% /alert %}}

##  **Ограничение количества генерируемых страниц**

В следующем примере показано, как преобразовать диапазон страниц (3 и 4) в файле Excel с номером Microsoft в номер PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше всего вызвать[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) метод непосредственно перед его рендерингом в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а правильные значения будут отображены в выходном файле.

{{% /alert %}}
