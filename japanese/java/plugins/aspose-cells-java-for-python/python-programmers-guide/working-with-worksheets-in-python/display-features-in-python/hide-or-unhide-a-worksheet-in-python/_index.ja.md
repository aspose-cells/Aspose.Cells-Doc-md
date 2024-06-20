---
title: Pythonでワークシートを非表示または表示する
type: docs
weight: 50
url: /ja/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - ワークシートを非表示または表示する**
### **ワークシートを非表示にする**
Aspose.Cells Java for Rubyを使用してモジュール**hideunhideworksheet**を呼び出してワークシートを非表示にします。

**Pythonコード**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **ワークシートを表示する**
開発者は、WorksheetクラスのsetVisible(true)メソッドを設定することで、ワークシートを表示できます。

**Pythonコード**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hide or Unhide a Worksheet (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
