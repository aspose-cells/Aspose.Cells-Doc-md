---
title: 在设置Style.Custom属性时检查自定义数字格式
linktitle: 在设置Style.Custom属性时检查自定义数字格式
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库，支持在样式设置时检查自定义数字格式。本文将展示如何使用 Aspose.Cells 库检查自定义数字格式，以确保样式正确。
keywords: Aspose.Cells，Node.js 库，电子表格，样式，自定义数字格式，检查，验证
type: docs
weight: 170
url: /zh/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **可能的使用场景**

如果你为 [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) 方法分配了无效的自定义数字格式，Aspose.Cells for Node.js via C++ 不会抛出任何异常。但如果你希望 Aspose.Cells 检查所分配的自定义数字格式是否有效，请将 [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) 方法设置为 **true**。

## **在调用 Style.setCustom(string) 方法时检查自定义数字格式**

以下示例代码为 [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) 方法分配了无效的自定义数字格式。由于我们已将 [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) 方法设置为 **true**，因此会抛出异常，例如无效的数字格式。请阅读代码内的注释以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
