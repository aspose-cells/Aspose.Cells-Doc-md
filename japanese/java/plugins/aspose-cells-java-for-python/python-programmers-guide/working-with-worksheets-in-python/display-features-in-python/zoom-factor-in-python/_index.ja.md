---
title: Python のズーム倍率
type: docs
weight: 80
url: /ja/java/zoom-factor-in-python/
---
## **Aspose.Cells - ズーム係数**
を使用してズーム係数を設定するには**Aspose.Cells Java for Python**、単に呼び出す**ズーム係数**モジュール。

**Python コード**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ズーム倍率 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
