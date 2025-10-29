---
title: 支持在用Golang通过C++加载HTML到Excel工作簿时的DIV标签布局
linktitle: 支持DIV标签布局
type: docs
weight: 50
url: /zh/go-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
description: 学习在将HTML加载到Excel工作簿时支持DIV标签布局的方法，使用Aspose.Cells for C++。
---

{{% alert color="primary" %}} 

通常在用Golang通过C++将HTML加载到Excel工作簿对象时会忽略DIV标签布局，但如果需要保留，应将 [GetSupportDivTag()](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getsupportdivtag/) 属性设置为**true**。此属性的默认值为**false**。

{{% /alert %}} 

以下示例代码展示了[GetSupportDivTag()](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getsupportdivtag/)属性的用法。请下载输入HTML中使用的[阿斯普斯徽标](5115218.png)和由代码生成的[输出Excel文件](5115220.xlsx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SupportTheLayoutOfDivTagsWhileLoadingHtmlToExcelWorkbook.go" >}}
