---
title: 使用C++和Golang通过抽象计算引擎返回值范围
linktitle: 使用AbstractCalculationEngine返回一系列值
description: 介绍如何通过C++和Golang使用Aspose.Cells库实现返回值范围的抽象计算引擎。加载现有Excel文件或创建新Excel文件，利用Aspose.Cells提供的方法获取值范围并返回结果。最后，将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 返回一系列值的抽象计算引擎
type: docs
weight: 55
url: /zh/go-cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells提供[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)类，用于实现Microsoft Excel不支持的用户定义或自定义函数。

本文将解释如何从[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)返回值范围。

{{% /alert %}}

 以下代码演示了如何使用[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)类及其方法返回值范围。

 创建一个具有`CalculateCustomFunction`函数的类。该类实现了[**AbstractCalculationEngine**](https://reference.aspose.com/cells/go-cpp/abstractcalculationengine/)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine.go" >}}
 现在在您的程序中使用上述函数。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReturningARangeOfValuesUsingAbstractcalculationengine-1.go" >}}
