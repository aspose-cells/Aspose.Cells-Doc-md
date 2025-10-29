---
title: 保存文件
type: docs
weight: 20
url: /zh/cpp/saving-files/
---

{{% alert color="primary" %}} 

Aspose.Cells可以创建和保存文件，以及操作现有文件。本文解释了文件可以保存的各种方式。

{{% /alert %}} 
## **不同的文件保存方式**
Aspose.Cells提供了[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，它代表Microsoft Excel文件，并提供处理Excel文件所需的方法。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法，用于保存Excel文件。[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法具有许多重载，用于以不同方式保存文件。保存文件的文件格式由[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举决定。
## **将文件保存到某个位置**
要将文件保存到存储位置，请在调用[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法时指定文件名（包括存储路径）和所需的文件格式（来自[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举）。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToSomeLocation-new.cpp" >}}


## **将文件保存到流**
要将文件保存到流，请创建MemoryStream或FileStream对象，并通过调用[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法将文件保存到该流对象。在调用[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法时使用[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举指定所需的文件格式。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToStream-new.cpp" >}}

## **将文件保存为 PDF**
要使用Aspose.Cells for C++库将所需内容保存到PDF文件，请创建新的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象或通过读取现有的Excel文件来构建[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象，然后通过调用[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)对象的Save方法将文件保存为PDF。在调用Save方法时，使用[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)枚举来指定所需的文件格式。


{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-SavingFiles-SavingFileToPdf-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
