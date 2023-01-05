---
title: Python でのページ オプションの設定
type: docs
weight: 10
url: /ja/java/setting-page-options-in-python/
---
## **Aspose.Cells - ページ オプションの設定**
### **ページの向き**
を使用してページの向きの設定を適用するには**Aspose.Cells Ruby の場合は Java**、 電話**page_orientation**方法**ページ設定**モジュール。

**Python コード**

{{< highlight "java" >}}

 def page_orientation(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the orientation to Portrait

page_setup = sheet.getPageSetup()

page_orientation_type = self.PageOrientationType

page_setup.setOrientation(page_orientation_type.PORTRAIT)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Page_Orientation.xls")

print "Set page orientation, please check the output file."


{{< /highlight >}}
### **スケーリング係数**
を使用してスケーリングを適用するには**Aspose.Cells Java for Python**、 電話**スケーリング**方法**ページ設定**モジュール。

**Python コード**

{{< highlight "python" >}}

 def scaling(self):        

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the scaling factor to 100

page_setup = sheet.getPageSetup()

page_setup.setZoom(100)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Scaling.xls")

print "Set scaling, please check the output file."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ページオプションの設定 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
