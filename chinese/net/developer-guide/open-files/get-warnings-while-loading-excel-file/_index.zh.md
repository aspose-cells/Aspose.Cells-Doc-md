---
title: 加载Excel文件时获取警告
type: docs
weight: 110
url: /zh/net/get-warnings-while-loading-excel-file/
---

## **可能的使用场景**

有时用户尝试加载略有损坏但可加载的工作簿。在这种情况下，Aspose.Cells在加载工作簿时会抛出警告。您可以通过实现 [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) 接口并设置 [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback) 属性来捕获这些警告。

## **加载 Excel 文件时获取警告**

以下示例代码解释了如何在加载excel文件时获取警告。该代码加载[示例excel文件](sampleDuplicateDefinedName.xlsx)，在加载时会生成 [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) 警告。然后通过 [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) 方法捕获该警告并在控制台上打印警告消息。代码然后将工作簿保存为[输出excel文件](outputDuplicateDefinedName.xlsx)。如果您在Microsoft Excel中打开示例excel文件，它也会显示您此警告，如下图所示。还请检查下面给出的代码的控制台输出以获取更多理解。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **控制台输出**

执行上述代码时，以下是控制台输出的代码，提供了 [示例excel文件](sampleDuplicateDefinedName.xlsx)。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
