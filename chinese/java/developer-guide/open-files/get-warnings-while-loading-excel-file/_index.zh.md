---
title: 加载Excel文件时获取警告
type: docs
weight: 60
url: /zh/java/get-warnings-while-loading-excel-file/
---

## **可能的使用场景**

有时用户尝试加载某种有些损坏但可加载的工作簿。在这种情况下，Aspose.Cells在加载工作簿时会引发警告。您可以通过实现**[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)**接口并设置**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**属性来捕获这些警告。

## **加载 Excel 文件时获取警告**

以下示例代码解释了如何在加载Excel文件时获取警告。该代码加载[示例Excel文件](sampleDuplicateDefinedName.xlsx)，它在加载时引发**[DuplicateDefinedName](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)**警告。然后通过**[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))**方法来捕获此警告，该方法会在控制台上打印警告消息。然后，代码将工作簿保存为[输出Excel文件](outputDuplicateDefinedName.xlsx)。如果您在Microsoft Excel中打开示例Excel文件，它也会显示此警告，如下方截图所示。还请查看下方所提供的代码的控制台输出，以了解更多信息。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **控制台输出**

执行上述代码时，以下是控制台输出的代码，提供了 [示例excel文件](sampleDuplicateDefinedName.xlsx)。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
