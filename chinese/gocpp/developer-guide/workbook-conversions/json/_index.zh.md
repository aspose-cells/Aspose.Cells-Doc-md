---
title: 使用 Golang 通过 C++ 将工作簿转换为 JSON
linktitle: 将工作簿转换为JSON
type: docs
weight: 300
url: /zh/go-cpp/convert-workbook-to-json/
description: 学习如何用Aspose.Cells for C++将Excel工作簿转换为JSON格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持将工作簿转换为JSON（JavaScript对象表示法）文件。

{{% /alert %}}

## **将Excel工作簿转换为JSON**

Aspose.Cells API支持将电子表格转换为JSON格式。将工作簿导出为JSON，只需将[**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)作为[**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法的第二个参数传递。也可以使用[**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)类来设置导出工作表为JSON的其他参数。

以下的代码示例演示了如何使用 [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) 枚举成员将活动工作表导出为 JSON。请查看代码以将【源文件】(book1.xlsx)转换为由代码生成的【输出 JSON 文件】(book1.json)作为参考。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## ** 高级主题**
- [将CSV转换为JSON](/cells/zh/cpp/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/cpp/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/cpp/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/cpp/convert-json-to-excel/)
