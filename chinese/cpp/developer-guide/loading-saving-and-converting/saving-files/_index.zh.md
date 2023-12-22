---
title: 保存文件
type: docs
weight: 20
url: /zh/cpp/saving-files/
---
{{% alert color="primary" %}} 

Aspose.Cells 可以创建和保存文件以及操作现有文件。本文介绍了保存文件的各种方式。

{{% /alert %}} 
##  **保存文件的不同方法**
 Aspose.Cells 提供[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)它代表一个 Microsoft Excel 文件，并提供使用 Excel 文件所需的方法。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)用于保存 Excel 文件的方法。这[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法有许多重载，用于以不同的方式保存文件。文件保存的文件格式由[保存格式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举。
##  **将文件保存到某个位置**
要将文件保存到存储位置，请指定文件名（包含存储路径）和所需的文件格式（来自[保存格式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举）调用时[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


##  **将文件保存到流**
要将文件保存到流，请创建 MemoryStream 或 FileStream 对象，然后通过调用以下方法将文件保存到该流对象：[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。使用指定所需的文件格式[保存格式](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)调用时的枚举[节省](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}
