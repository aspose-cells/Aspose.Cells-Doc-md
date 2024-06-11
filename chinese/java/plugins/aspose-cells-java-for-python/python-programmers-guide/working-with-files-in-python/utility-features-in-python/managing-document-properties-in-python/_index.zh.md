---
title: 在Python中管理文档属性
type: docs
weight: 60
url: /zh/java/managing-document-properties-in-python/
---

## **Aspose.Cells - 管理文档属性**
开发人员可以使用该示例中下面演示的**custom_properties**集合的**Index**或**Name**来获取特定属性。

**Python 代码**

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
## **下载运行代码**
从以下任何社交编码网站下载**Hello World（Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
