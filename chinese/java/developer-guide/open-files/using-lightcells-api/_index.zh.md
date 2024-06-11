---
title: 使用 LightCells API
type: docs
weight: 80
url: /zh/java/using-lightcells-api/
---

{{% alert color="primary" %}}

有时，您需要读取和写入包含大量数据或工作表中大量内容的大型 Microsoft Excel 文件。LightCells API 适用于创建大型 Excel 电子表格：使用它，您需要内存，并且可以获得更好的性能和效率。

{{% /alert %}}

## **事件驱动架构**

Aspose.Cells 提供 LightCells API，主要设计用于逐个处理单元格数据，而无需将完整的数据模型块（使用 Cell 集合等）构建到内存中。它以事件驱动模式工作。

在保存工作簿时，保存组件会直接提供逐个单元格的单元格内容，然后将其保存到输出文件。

在读取模板文件时，组件会解析每个单元格，并逐个提供它们的值。

在这两个过程中，处理一个 Cell 对象然后丢弃它，Workbook 对象不会保留集合。因此，在导入和导出具有大数据集的 Microsoft Excel 文件时，将节省内存。

即使 LightCells API 在 XLSX 和 XLS 文件上以相同的方式处理单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），但它对于 XLSX 文件比 XLS 文件更有效地节省内存，因为这两种格式的数据模型和结构不同。

但是，**对于 XLS 文件**，为了节省更多内存，开发人员可以指定在保存过程中保存生成的临时数据的临时位置。通常情况下，**使用 LightCells API 保存 XLSX 文件可能节省50%或更多内存**，**保存 XLS 可能节省大约20-40%内存**。

### **写入大型Excel文件**

Aspose.Cells提供了一个接口LightCellsDataProvider，需要在你的程序中实现。该接口代表了轻量级模式下保存大型电子表格文件的数据提供程序。

在这种模式下保存工作簿时，对工作簿中的每个工作表进行保存时会检查startSheet(int)。对于一个工作表，如果startSheet(int)返回true，则由此实现提供要保存的行和单元格的所有数据和属性。首先调用nextRow()以获取要保存的下一行索引。如果返回一个有效的行索引（行索引必须按升序排列以便保存行），则提供代表此行的Row对象以供实现通过startRow(Row)设置其属性。

对于一行，首先检查nextCell()。如果返回一个有效的列索引（列索引必须按升序排列以便保存一行中的所有单元格），则提供一个代表此单元格的Cell对象，以通过startCell(Cell)设置数据和属性。设置完此单元格的数据后，直接将此单元格保存到生成的电子表格文件中，然后将检查并处理下一个单元格。

下面的示例展示了LightCells API的工作原理。

下面的程序在工作表中创建了一个包含10万条记录的巨大文件，并填充了数据。我们在工作表的某些单元格中添加了一些超链接、字符串值、数值和公式。此外，我们也格式化了一系列单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **读取大型Excel文件**

Aspose.Cells提供了一个接口LightCellsDataHandler，需要在你的程序中实现。该接口代表了轻量级模式下读取大型电子表格文件的数据提供程序。

在此模式下读取工作簿时，将检查每个工作表的startSheet()。对于工作表，如果startSheet()返回true，则会检查并处理工作表行和列中所有单元格的所有数据和属性。对于每一行，都会调用startRow()以检查是否需要处理。如果需要处理行，则首先读取行的属性，开发人员可以通过processRow()访问其属性。

如果行的单元格也需要处理，则processRow()返回true，并且对于行中的每个现有单元格都会调用startCell()以检查是否需要处理。如果需要，则调用processCell()。

下面的示例代码说明了这个过程。该程序读取了一个包含数百万条记录的大型文件。读取工作簿中的每个工作表需要一些时间。示例代码读取文件并检索每个工作表的总单元格数、字符串数量和公式数量。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

实现LightCellsDataHandler接口的类

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
