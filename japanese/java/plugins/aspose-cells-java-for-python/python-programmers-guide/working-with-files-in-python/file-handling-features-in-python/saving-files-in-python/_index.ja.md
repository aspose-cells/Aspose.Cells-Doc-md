---
title: ファイルを Python に保存しています
type: docs
weight: 20
url: /ja/java/saving-files-in-python/
---
## **Aspose.Cells - ファイルの保存**
### **ファイルをある場所に保存する**
開発者がファイルを保存する必要がある場合**Aspose.Cells Java for Python**ある保存場所に移動すると、ファイル名 (完全な保存パスを含む) と目的のファイル形式 (**ファイル形式の種類**列挙) の呼び出し中**セーブ**方法**ワークブック**物体。

**Python コード**

{{< highlight "python" >}}

 fileFormatType = self.FileFormatType


# Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

# Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

# Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

# Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

ダウンロード**ファイルの保存 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
