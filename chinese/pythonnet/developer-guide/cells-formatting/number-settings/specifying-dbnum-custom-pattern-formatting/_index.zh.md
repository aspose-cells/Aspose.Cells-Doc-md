---
title: 指定使用DBNum自定义模式格式
description: Aspose.Cells是支持使用自定义格式模板（如 g 和 ge ）渲染日期的Python库。本文将介绍如何使用 Aspose.Cells 库指定 dbnum 自定义格式模式，让用户对数字的显示方式拥有更多控制权。
keywords: Aspose.Cells，Python库，电子表格，自定义格式模式，格式化， dbnum ，控制显示
type: docs
weight: 110
url: /zh/python-net/specifying-dbnum-custom-pattern-formatting/
---

## **可能的使用场景**

Aspose.Cells for Python via .NET支持*DBNum* 自定义模式格式。例如，如果您的单元格值为123，并将其自定义格式指定为[DBNum2][$-804]General，那么它将显示为壹佰贰拾叁。您可以使用[**Cell.get_style()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style/#)方法和[**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom)属性为单元格指定自定义格式。

## **示例代码**

以下示例代码说明了如何指定 *DBNum* 自定义模式格式。请检查其 [输出PDF](43352081.pdf) 以获取更多帮助。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SpecifyingDBNumCustomPatternFormatting.py" >}}

{{< app/cells/assistant language="python-net" >}}
