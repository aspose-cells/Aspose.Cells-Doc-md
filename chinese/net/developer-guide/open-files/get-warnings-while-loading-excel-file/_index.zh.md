---
title: 加载Excel文件时获取警告
type: docs
weight: 110
url: /zh/net/get-warnings-while-loading-excel-file/
---

## **可能的使用场景**

有时用户尝试加载在某种程度上损坏但可加载的工作簿。在这种情况下，Aspose.Cells在加载工作簿时会发出警告。您可以通过实现IWarningCallback接口并设置LoadOptions.WarningCallback属性来捕获这些警告。

## **加载Excel文件时获取警告**

以下示例代码解释了如何在加载Excel文件时获取警告。该代码加载了在加载时会引发DuplicateDefinedName警告的示例Excel文件。然后，通过IWarningCallback.Warning()方法捕获该警告并在控制台上打印警告消息。代码然后将工作簿保存为输出Excel文件。如果您在Microsoft Excel中打开示例Excel文件，也会显示此警告，如下图所示。请查看下面给出的代码的控制台输出以获得更多理解。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **控制台输出**

上述代码在使用提供的示例Excel文件时执行时的控制台输出。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
