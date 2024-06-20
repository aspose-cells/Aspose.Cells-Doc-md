---
title: Python で MHTML ファイルに変換する
type: docs
weight: 30
url: /ja/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - MHTML に変換する**
PythonでAspose.Cells for Javaを使用してWorksheetをMHTMLファイルに変換するには、Converterモジュールのworksheet_to_mhtml()メソッドを単純に呼び出します。

**Pythonコード**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**MHTML に変換する (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
