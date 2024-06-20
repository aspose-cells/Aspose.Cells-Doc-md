---
title: Pythonでのファイルの保存
type: docs
weight: 20
url: /ja/java/saving-files-in-python/
---

## **Aspose.Cells - ファイルの保存**
### **開発者がファイルをストレージに保存する必要がある場合、**Aspose.Cells Java for Ruby**を使用して**Workbook**オブジェクトの**save**メソッドを呼び出す際に、ファイル名(完全なストレージパスを含む)と希望のファイル形式(**FileFormatType**列挙型を使用)を単純に指定することができます。**
開発者が**Aspose.Cells Java for Python**を使用してファイルを特定のストレージ場所に保存する必要がある場合、**Workbook**オブジェクトの**save**メソッドを呼び出す際に、完全な保存パスと所望のファイル形式（**FileFormatType**列挙型を使用）を指定するだけです。

**Pythonコード**

{{< highlight python >}}

 fileFormatType = self.FileFormatType


#Creating an Workbook object with an Excel file path

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save in default (Excel2003) format

workbook.save(self.dataDir + "book.default.out.xls")

#Save in Excel2003 format

workbook.save(self.dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

#Save in Excel2007 xlsx format

workbook.save(self.dataDir + "book.out.xlsx", fileFormatType.XLSX)

#Save in SpreadsheetML format

workbook.save(self.dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)

#Print Message

print("<BR>")

print("Worksheets are saved successfully.")

{{< /highlight >}}

以下のいずれかのソーシャルコーディングサイトから、**Aspose.Cells**の**ファイルの保存**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
