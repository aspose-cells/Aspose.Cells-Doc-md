---
title: إدارة خصائص الوثيقة في Python
type: docs
weight: 60
url: /ar/java/managing-document-properties-in-python/
---
## **Aspose.Cells - إدارة خصائص الوثيقة**
يمكن للمطورين الاستفادة من**فِهرِس**أو**اسم** من العقار للحصول على عقار معين من أ**خصائص_مخصصة**المجموعة كما هو موضح أدناه في المثال.

**Python كود**

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
## **قم بتنزيل كود التشغيل**
 تحميل**Hello World (Aspose.Cells)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
