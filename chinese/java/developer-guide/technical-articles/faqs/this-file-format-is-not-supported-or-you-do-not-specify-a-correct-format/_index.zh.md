---
title: 此文件格式不受支持，或者您没有指定正确的格式
type: docs
weight: 10
url: /zh/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **此文件格式不受支持，或者您没有指定正确的格式**
如果用户在从模板文件创建工作簿时指定了文件格式，通常这个错误是因为指定的文件格式与模板文件的实际文件格式不符。如果用户未指定文件格式，通常是因为文件名扩展名不代表该文件的实际文件格式，且无法自动检测文件格式，例如没有任何特殊标识符的csv/tsv文件。当然，不受Cells支持的文件格式也会报告此错误。
{{< app/cells/assistant language="java" >}}
