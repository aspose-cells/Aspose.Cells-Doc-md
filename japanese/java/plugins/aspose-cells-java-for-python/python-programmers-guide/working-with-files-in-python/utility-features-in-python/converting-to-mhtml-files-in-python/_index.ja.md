---
title: Python の MHTML ファイルへの変換
type: docs
weight: 30
url: /ja/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - MHTML への変換**
Python の Aspose.Cells for Java を使用してワークシートを MHTML ファイルに変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの mhtml() メソッド。

**Python コード**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**MHTML に変換中 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
