---
title: 在使用 C++ 通过 Node.js 加载 Excel 文件时获取警告信息
linktitle: 加载Excel文件时获取警告
type: docs
weight: 110
url: /zh/nodejs-cpp/get-warnings-while-loading-excel-file/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 加载 Excel 文件时捕获警告。有效处理损坏但可加载的工作簿。
---

## **可能的使用场景**

 有时，用户尝试加载一个或有损坏但仍可加载的工作簿。在这种情况下，Aspose.Cells 在加载工作簿时会发出警告。您可以通过实现 [**IWarningCallback**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback) 接口并设置 [**LoadOptions.getWarningCallback()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getWarningCallback--) 属性来捕获这些警告。

## **加载 Excel 文件时获取警告**

 以下示例代码说明了如何在加载Excel文件时获取警告。代码加载会在加载时抛出 [**DuplicateDefinedName**](https://reference.aspose.com/cells/nodejs-cpp/warningtype) 警告的 [示例Excel文件](sampleDuplicateDefinedName.xlsx)。这个警告由 [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/nodejs-cpp/iwarningcallback/#warning-warninginfo-) 方法捕获，并在控制台输出警告信息。随后，代码将工作簿保存为 [输出Excel文件](outputDuplicateDefinedName.xlsx)。如果在Microsoft Excel中打开该示例文件，也会显示类似的警告。请同时查看下面的控制台输出以获取更多信息。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Implement IWarningCallback interface to catch warnings while loading workbook
class WarningCallback extends AsposeCells.IWarningCallback {
    warning(warningInfo) {
        if (warningInfo.getType() === AsposeCells.WarningType.DuplicateDefinedName) {
            console.log("Duplicate Defined Name Warning: " + warningInfo.getDescription());
        }
    }
}

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create load options and set the WarningCallback property 
// to catch warnings while loading workbook
const options = new AsposeCells.LoadOptions();
options.setWarningCallback(new WarningCallback());

// Load the source excel file
const book = new AsposeCells.Workbook(path.join(dataDir, "sampleDuplicateDefinedName.xlsx"), options);

// Save the workbook 
book.save(path.join(dataDir, "outputDuplicateDefinedName.xlsx"));
```

## **控制台输出**

执行上述代码时，以下是控制台输出的代码，提供了 [示例excel文件](sampleDuplicateDefinedName.xlsx)。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
