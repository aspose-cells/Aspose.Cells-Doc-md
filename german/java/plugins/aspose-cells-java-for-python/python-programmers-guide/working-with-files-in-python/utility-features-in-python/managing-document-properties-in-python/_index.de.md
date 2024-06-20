---
title: Dokumenteigenschaften in Python verwalten
type: docs
weight: 60
url: /de/java/managing-document-properties-in-python/
---

## **Aspose.Cells - Dokumenteigenschaften verwalten**
Entwickler können den **Index** oder den **Namen** der Eigenschaft verwenden, um eine bestimmte Eigenschaft aus einer **custom_properties**-Sammlung wie im folgenden Beispiel gezeigt zu erhalten.

**Python-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Hello World (Aspose.Cells)** von einer der unten genannten sozialen Codierungsseiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
