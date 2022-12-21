---
title: Python でペインをフリーズ
type: docs
weight: 40
url: /ja/java/freeze-panes-in-python/
---
## **Aspose.Cells - フリーズペイン**
を使用してスプレッドシート ドキュメントのペインを固定するには**Aspose.Cells Java for Python**、単に呼び出す**FreezePanes**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Hello World (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
