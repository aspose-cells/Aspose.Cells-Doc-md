---
title: Python でのドキュメント プロパティの管理
type: docs
weight: 60
url: /ja/java/managing-document-properties-in-python/
---
## **Aspose.Cells - ドキュメント プロパティの管理**
開発者は、**索引**また**名前**から特定のプロパティを取得するためのプロパティの**custom_properties**以下の例で示されているコレクション。

**Python コード**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Retrieve a list of all custom document properties of the Excel file

customProperties = workbook.getWorksheets().getCustomDocumentProperties()

# Accessing a custom document property by using the property index

# customProperty1 = customProperties.get(3)

# Accessing a custom document property by using the property name

customProperty2 = customProperties.get("Owner")


# Adding a custom document property to the Excel file

publisher = customProperties.add("Publisher", "Aspose")

# Save the file

workbook.save(self.dataDir + "Test_Workbook.xls")

# Removing a custom document property

customProperties.remove("Publisher")

# Save the file

workbook.save(self.dataDir + "Test_Workbook_RemovedProperty.xls")

\# Print message

print "Excel file's custom properties accessed successfully."

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Hello World (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
