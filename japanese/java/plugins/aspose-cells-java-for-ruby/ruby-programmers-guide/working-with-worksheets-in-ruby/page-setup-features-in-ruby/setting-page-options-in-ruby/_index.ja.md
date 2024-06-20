---
title: Rubyでのページオプションの設定
type: docs
weight: 10
url: /ja/java/setting-page-options-in-ruby/
---

## **Aspose.Cells - ページオプションの設定**
### **ページの向き**
**Aspose.Cells Java for Ruby** を使用してページの向き設定を適用するには、**pagesetup** モジュールの **page_orientation** メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def page_orientation()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait

    page_setup = sheet.getPageSetup()

    page_orientation_type = Rjb::import('com.aspose.cells.PageOrientationType')

    page_setup.setOrientation(page_orientation_type.PORTRAIT)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Page Orientation.xls")

    puts "Set page orientation, please check the output file."

end   

{{< /highlight >}}
### **拡大/縮小率**
Aspose.Cells Java for Rubyを使用してスケーリングを適用するには、**pagesetup**モジュールの**scaling**メソッドを呼び出します。

**Ruby Code**

{{< highlight ruby >}}

 def scaling()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100

    page_setup = sheet.getPageSetup()

    page_setup.setZoom(100)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Scaling.xls")

    puts "Set scaling, please check the output file."

end


{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のどちらかのソーシャルコーディングサイトから、**Aspose.Cells**の**ページオプションの設定**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagesetup.rb)
