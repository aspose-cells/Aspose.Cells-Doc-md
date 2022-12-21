---
title: Ruby でのドキュメント プロパティの管理
type: docs
weight: 90
url: /ja/java/managing-document-properties-in-ruby/
---
## **Aspose.Cells - ドキュメント プロパティへのアクセス**
開発者は、**索引**また**名前**から特定のプロパティを取得するためのプロパティの**custom_properties**以下の例で示されているコレクション。

**ルビーコード**

{{< highlight "ruby" >}}

 def get_properties()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Accessng a custom document property by using the property index

    puts "Property By Index: " +  custom_properties.get(1).to_string

    # Accessng a custom document property by using the property name

    puts "Property By Name: " + custom_properties.get("Publisher").to_string

end

{{< /highlight >}}
## **Aspose.Cells - カスタム プロパティの追加**
Ruby の Aspose.Cells Java を使用してカスタム ドキュメント プロパティを追加するには、次のように呼び出します。**add_custom_property**の方法**書類**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 def add_custom_property()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file

    custom_properties.add("Publisher", "Aspose")

    # Save the document in PDF format

    workbook.save(data_dir + "Add_Property.xls")

    puts "Added custom property successfully."

end   

{{< /highlight >}}
## **Aspose.Cells - カスタム プロパティの削除**
Ruby の Aspose.Cells Java を使用してカスタム ドキュメント プロパティを削除するには、次のように呼び出します。**remove_custom_property**の方法**書類**モジュール。

**ルビーコード**

{{< highlight "ruby" >}}

 def remove_custom_property()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file

    custom_properties.remove("Publisher")

    # Save the document in PDF format

    workbook.save(data_dir + "Removed_Property.xls")

    puts "Removed custom property successfully."

end   

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ドキュメント プロパティへのアクセス (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)
