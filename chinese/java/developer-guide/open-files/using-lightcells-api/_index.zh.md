---
title: 使用LightCells API
type: docs
weight: 80
url: /zh/java/using-lightcells-api/
---

{{% alert color="primary" %}}

有时您需要读取和写入具有大量数据或工作表内容的大型Microsoft Excel文件。LightCells API对于创建大型Excel电子表格很有用：使用它，您需要占用更少的内存并获得更好的性能和效率。

{{% /alert %}}

## **事件驱动架构**

Aspose.Cells提供了LightCells API，主要设计用于在不构建完整数据模型块（使用单元格集合等）到内存中的情况下操作单元格数据。它以事件驱动模式工作。

保存工作簿时，在保存时逐个提供单元格内容，并且组件将其直接保存到输出文件。

在读取模板文件时，组件会逐个解析每个单元格并提供它们的值。

在这两种情况下，一个单元格对象会被处理然后丢弃，工作簿对象不会保留该集合。因此，在导入和导出包含大数据集的 Microsoft Excel 文件时，该模式能节省内存。

虽然 LightCells API 对 XLSX 和 XLS 文件的处理方式相同（实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但对于 XLSX 文件比 XLS 文件更有效地节省了内存，因为这两种格式的数据模型和结构有所不同。

然而，对于 XLS 文件，为了节省更多内存，开发人员可以指定一个用于保存保存过程中生成的临时数据的临时位置。通常情况下，使用 LightCells API 来保存 XLSX 文件可以比使用常规方式节省50%或更多内存，而保存 XLS 可以节省大约20-40%的内存。

### **写入大型Excel文件**

Aspose.Cells提供了一个接口LightCellsDataProvider，您需要在程序中实现它。该接口表示用于以轻量模式保存大型电子表格文件的数据提供程序。

在此模式下保存工作簿时，将对工作簿中的每个工作表进行检查。对于一个工作表，如果startSheet(int)返回true，则会由此实现提供此工作表中的所有行和单元格的数据和属性。首先调用nextRow()以获取要保存的下一行索引。如果返回有效的行索引（行索引必须是按升序排列的），则提供表示该行的Row对象以供实现设置其属性。使用startRow(Row)方法设置其属性。

对于一行，首先检查nextCell()。如果返回有效的列索引（所有行的所有单元格必须按升序排列），则提供表示该单元格的Cell对象以供用startCell(Cell)设置数据和属性。设置了该单元格的数据之后，将其直接保存到生成的电子表格文件中，并检查并处理下一个单元格。

以下示例说明了LightCells API的工作原理。

以下程序在工作表中创建包含10万条记录的大型文件，并填充了数据。我们向工作表中的某些单元格添加了一些超链接、字符串值、数值以及公式。此外，我们还对一系列单元格进行了格式化。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **读取大型Excel文件**

Aspose.Cells提供了一个接口LightCellsDataHandler，您需要在程序中实现它。该接口表示用于以轻量模式读取大型电子表格文件的数据提供程序。

在这种模式下读取工作簿时，将对工作簿中的每个工作表进行检查。对于工作表，如果startSheet()返回true，则将检查并处理该工作表中行和列的所有单元格的数据和属性。对于每一行，都会调用startRow()来检查是否需要处理。如需要处理，则首先读取该行的属性，并且开发人员可以使用processRow()方法访问其属性。

如果行的单元格也需要处理，则processRow()返回true，并且对该行中的每个现有单元格调用startCell()以检查是否需要处理。如果需要，则调用processCell()。

以下示例代码说明了这个过程。程序读取一个包含数百万条记录的大文件时会占用一些时间。示例代码读取文件并检索了每个工作表的总单元格数、字符串计数和公式计数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

实现LightCellsDataHandler接口的类

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
