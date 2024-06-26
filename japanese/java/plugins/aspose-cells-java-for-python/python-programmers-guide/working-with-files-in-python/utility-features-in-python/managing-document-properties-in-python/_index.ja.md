---
title: Python で文書のプロパティを管理する
type: docs
weight: 60
url: /ja/java/managing-document-properties-in-python/
---

## **Aspose.Cells - ドキュメントプロパティの管理**
開発者は、以下の例に示すように、カスタムプロパティの**custom_properties**コレクションから特定のプロパティを取得するために、プロパティの**Index**または**Name**を利用できます。

**Pythonコード**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Retrieve a list of all custom document properties of the Excel file

customProperties = workbook.getWorksheets().getCustomDocumentProperties()

#Accessing a custom document property by using the property index

#customProperty1 = customProperties.get(3)

#Accessing a custom document property by using the property name

customProperty2 = customProperties.get("Owner")


#Adding a custom document property to the Excel file

publisher = customProperties.add("Publisher", "Aspose")

#Save the file

workbook.save(self.dataDir + "Test_Workbook.xls")

#Removing a custom document property

customProperties.remove("Publisher")

#Save the file

workbook.save(self.dataDir + "Test_Workbook_RemovedProperty.xls")

\# Print message

print "Excel file's custom properties accessed successfully."

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**Hello World (Aspose.Cells)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
