﻿---
title: 在 Python 中显示或隐藏选项卡
type: docs
weight: 30
url: /zh/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - 显示隐藏标签**
### **隐藏标签**
隐藏选项卡使用**Aspose.Cells Java 红宝石**， 称呼**显示隐藏选项卡**模块。

**Python 代码**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **使选项卡可见**
使用 Workbook 类的 setSheetTabBarHidden(false) 方法使选项卡可见。

**Python 代码**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **下载运行代码**
下载**Hello World (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
