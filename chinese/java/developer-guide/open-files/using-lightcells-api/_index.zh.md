---
title: 使用 LightCells API
type: docs
weight: 80
url: /zh/java/using-lightcells-api/
---
{{% alert color="primary" %}}

有时您需要读取和写入工作表中包含大量数据或内容的大型 Microsoft Excel 文件。 LightCells API 对于创建巨大的 Excel 电子表格很有用：有了它，您需要内存并获得更好的性能和效率。

{{% /alert %}}

## **事件驱动架构**

Aspose.Cells 提供了LightCells API，主要是用来对cell数据进行逐个操作，而不需要将完整的数据模型块（使用Cell集合等）构建到内存中。它以事件驱动模式工作。

保存工作簿时，保存时逐格提供单元格内容，组件直接保存到输出文件中。

读取模板文件时，组件会解析每个单元格并一一提供它们的值。

在这两个过程中，一个 Cell 对象被处理然后被丢弃，Workbook 对象不保存集合。因此，在这种模式下，导入和导出具有大量数据集的 Microsoft Excel 文件时会节省内存，否则会占用大量内存。

即使 LightCells API 以相同的方式处理 XLSX 和 XLS 文件的单元格（它实际上并不将所有单元格加载到内存中，而是处理一个单元格然后丢弃它），它为 XLSX 文件比 XLS 文件更有效地节省内存，因为两种格式的不同数据模型和结构。

然而，**对于 XLS 文件**，为了节省更多的内存，开发者可以指定一个临时位置来保存Save过程中产生的临时数据。通常，**使用 LightCells API 保存 XLSX 文件可以节省 50% 或更多内存**比使用常见的方式，**保存 XLS 可能会节省大约 20-40% 的内存**.

### **编写大型 Excel 文件**

Aspose.Cells提供了一个接口LightCellsDataProvider，需要在你的程序中实现。该接口表示用于以轻量级模式保存大型电子表格文件的数据提供程序。

使用此模式保存工作簿时，会在保存工作簿中的每个工作表时检查 startSheet(int)。对于一张工作表，如果 startSheet(int) 为真，则此工作表要保存的所有行和单元格的数据和属性均由此实现提供。首先，调用 nextRow() 以获取要保存的下一行索引。如果返回有效的行索引（行索引必须按升序排列才能保存行），则提供表示该行的 Row 对象供实现，以通过 startRow(Row) 设置其属性。

对于一行，首先检查 nextCell()。如果返回有效的列索引（列索引必须按升序排列才能保存一行的所有单元格），则提供一个代表该单元格的 Cell 对象，以通过 startCell(Cell) 设置数据和属性。设置好该单元格的数据后，直接将该单元格保存到生成的电子表格文件中，对下一个单元格进行检查处理。

以下示例显示了 LightCells API 的工作原理。

以下程序在工作表中创建了一个包含 100,000 条记录的巨大文件，其中充满了数据。我们向工作表中的某些单元格添加了一些超链接、字符串值、数值和公式。此外，我们还格式化了一系列单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataProviderDemo-LightCellsDataProviderDemo.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-Demo-Demo.java" >}}

## **读取大型 Excel 文件**

Aspose.Cells 提供一个接口，LightCellsDataHandler，需要在你的程序中实现。该接口表示用于以轻量级模式读取大型电子表格文件的数据提供程序。

以这种模式读取工作簿时，会在读取工作簿中的每个工作表时检查 startSheet()。对于工作表，如果 startSheet() 返回 true，则检查并处理工作表的行和列中单元格的所有数据和属性。对于每一行，都会调用 startRow() 来检查它是否需要处理。如果需要处理一行，则首先读取该行的属性，开发人员可以使用 processRow() 访问其属性。

如果该行的单元格也需要处理，则 processRow() 返回 true 并为该行中的每个现有单元格调用 startCell() 以检查它是否需要处理。如果是，则调用 processCell()。

下面的示例代码说明了这个过程。该程序读取一个包含数百万条记录的大文件。阅读工作簿中的每张纸需要一点时间。示例代码读取文件并检索每个工作表的单元格总数、字符串计数和公式计数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsTest1-LightCellsTest1.java" >}}

实现 LightCellsDataHandler 接口的类

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LightCellsDataHandlerVisitCells-LightCellsDataHandlerVisitCells.java" >}}
