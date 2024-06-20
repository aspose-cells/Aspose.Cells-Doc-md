---
title: Pythonでタブを表示または非表示にする
type: docs
weight: 30
url: /ja/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - タブを表示または非表示にする**
### **タブを非表示にする**
Aspose.Cells Java for Rubyを使用してタブを非表示にするには、displayhidetabsモジュールを呼び出します。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **タブを表示する**
WorkbookクラスのsetSheetTabBarHidden(false)メソッドを使用して、タブを表示する

**Pythonコード**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hello World (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
