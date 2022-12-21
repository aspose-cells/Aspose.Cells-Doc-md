---
title: Python でタブを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - 表示非表示タブ**
### **タブを非表示にする**
を使用してタブを非表示にするには**Aspose.Cells Ruby の場合は Java**、 電話**表示非表示タブ**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **タブを表示する**
Workbook クラスの setSheetTabBarHidden(false) メソッドでタブを表示します。

**Python コード**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Hello World (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
