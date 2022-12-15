---
title: 您的第一个 Aspose.Cells 申请 - Hello World
type: docs
weight: 30
url: /zh/python-net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

这个初学者主题展示了开发人员如何使用 Aspose.Cells 和简单的 API 创建一个简单的第一个应用程序 (Hello World)。该应用程序创建一个 Microsoft Excel 文件，在工作表的指定单元格中包含单词 Hello World。

{{% /alert %}}

### **创建 Hello World 应用程序**

要使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建工作簿类的实例。
1. 申请许可证：
1. 如果您购买了许可证，则在您的应用程序中使用该许可证来访问 Aspose.Cells 的全部功能
1. 如果您使用的是组件的评估版（如果您使用的是 Aspose.Cells 无许可证），请跳过此步骤。
1. 创建一个新的 Microsoft Excel 文件，或打开一个现有文件，您要在其中添加/更新一些文本。
1. 访问 Microsoft Excel 文件中工作表的任何单元格。
1. 插入单词**Hello World!**进入访问的单元格。
1. 生成修改后的 Microsoft Excel 文件。

下面的示例演示了上述步骤。

#### **创建工作簿**

下面的示例从头开始创建一个新工作簿，写入单词“Hello World！”到第一个工作表的单元格 A1 中，并保存文件。

**生成的电子表格** 

![待办事项：图像_替代_文本](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

#### **打开现有文件**

以下示例打开名为 Microsoft 的现有 Excel 模板文件**book1.xls**，写下“Hello World！”在第一个工作表的单元格 A1 中，并将工作簿另存为新文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpeningExistingFile.py" >}}
