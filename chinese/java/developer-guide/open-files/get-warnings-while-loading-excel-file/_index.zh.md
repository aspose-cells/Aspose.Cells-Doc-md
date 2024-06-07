---
title: 加载Excel文件时获取警告
type: docs
weight: 60
url: /zh/java/get-warnings-while-loading-excel-file/
---

## **可能的使用场景**

有时用户尝试加载略微损坏但可加载的工作簿。在这种情况下，Aspose.Cells在加载工作簿时会发出警告。您可以通过实现 **[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** 接口并设置 **[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)** 属性来捕获这些警告。

## **加载Excel文件时获取警告**

以下示例代码说明了如何在加载excel文件时获取警告。该代码加载了 [样本excel文件](sampleDuplicateDefinedName.xlsx) ，加载时会引发 **[DuplicateDefinedName](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** 警告。然后此警告由 **[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))** 方法捕捉，并在控制台上打印警告消息。代码随后将工作簿保存为 [输出excel文件](outputDuplicateDefinedName.xlsx)。如果您在Microsoft Excel中打开这个样本excel文件，也会显示出现的警告，如下面的截图所示。请还要查看下面给出的代码的控制台输出，以便更好地理解。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **控制台输出**

上述代码在使用提供的示例Excel文件时执行时的控制台输出。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
