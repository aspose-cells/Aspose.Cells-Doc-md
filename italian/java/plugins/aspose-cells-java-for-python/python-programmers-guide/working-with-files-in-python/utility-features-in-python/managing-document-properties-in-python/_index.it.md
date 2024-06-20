---
title: Gestione delle Proprietà del Documento in Python
type: docs
weight: 60
url: /it/java/managing-document-properties-in-python/
---

## **Aspose.Cells - Gestión de propiedades del documento**
Gli sviluppatori possono utilizzare l'**Indice** o il **Nome** della proprietà per ottenere una proprietà specifica da una collezione di **custom_properties** come mostrato di seguito nell'esempio.

**Codice Python**

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
## **Scarica il codice in esecuzione**
Scarica **Hello World (Aspose.Cells)** da uno dei siti di codifica sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
