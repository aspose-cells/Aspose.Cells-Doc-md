---
title: Управление свойствами документа в Python
type: docs
weight: 60
url: /ru/java/managing-document-properties-in-python/
---
## **Aspose.Cells — Управление свойствами документа**
Разработчики могут использовать**Показатель**или же**Имя** собственности, чтобы получить конкретную собственность от**custom_properties**коллекции, как показано ниже в примере.

**Python Код**

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
## **Скачать рабочий код**
 Скачать**Hello World (Aspose.Cells)** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
