---
title: 保存文件
type: docs
weight: 20
url: /zh/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells 使创建和保存文件以及操作现有文件成为可能。本文介绍了保存文件的各种方式。

{{% /alert %}} 
## **保存文件的不同方法**
Aspose.Cells 提供了[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)它表示一个 Microsoft Excel 文件并提供处理 Excel 文件所需的方法。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类提供了[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)用于保存 Excel 文件的方法。这[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法有许多用于以不同方式保存文件的重载。文件保存的文件格式由[保存格式](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)枚举。
## **将文件保存到某个位置**
要将文件保存到存储位置，请指定文件名（包括存储路径）和所需的文件格式（来自[保存格式](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)枚举）调用时[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)对象的[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation.cpp" >}}


## **将文件保存到流**
要将文件保存到流中，请创建一个 MemoryStream 或 FileStream 对象，然后通过调用[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)对象的[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。使用指定所需的文件格式[保存格式](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)调用时的枚举[节省](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream.cpp" >}}
