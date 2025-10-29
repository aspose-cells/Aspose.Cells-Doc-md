---
title: 用 Golang 通过 C++ 设置图表的数据源
linktitle: 数据源
type: docs
weight: 10
url: /zh/go-cpp/data-formatting-in-charts/
description: 了解Aspose.Cells for C++支持的各种数据源。我们的指南将引导您了解不同类型的数据源，以及如何连接和从中检索数据以填充工作表。
keywords: Aspose.Cells for C++、图表、数据格式、标签、颜色、字体、外观、易用性。
---

在之前的主题中，我们已经提供了许多示例，演示如何为您的图表设置数据源。在本主题中，我们将提供有关可为图表设置的数据类型的更多详细信息。

## **设置图表数据**

使用Aspose.Cells处理图表时，有以下两种数据类型需要处理：

 - 图表数据。
 - 类别数据。

### **图表数据**

图表数据是我们用作图表数据源的数据。我们可以通过调用 [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) 对象的 [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) 方法来添加包含图表数据的单元格范围。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **分类数据**

类别数据用于标记图表数据，并且可以通过其 [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/) 属性添加到 [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) 中。下面提供了一个完整的示例，演示了如何使用图表和分类数据。执行以上示例代码后，工作表将添加一个柱状图，如下所示。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **高级主题**
- [复制行或区域时更改图表的数据源到目标工作表](/cells/zh/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/cpp/create-dynamic-charts/)
- [使用 Chart.SetChartDataRange 方法设置图表的简单方法](/cells/zh/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的X和Y值类型](/cells/zh/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
