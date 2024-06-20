---
title: Gestionar Propiedades de Documentos en Python
type: docs
weight: 60
url: /es/java/managing-document-properties-in-python/
---

## **Aspose.Cells - Gestionar Propiedades de Documentos**
Los desarrolladores pueden hacer uso del **Índice** o el **Nombre** de la propiedad para obtener una propiedad específica de una colección de **propiedades personalizadas**, como se muestra a continuación en el ejemplo.

**Código Python**

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
## **Descargar Código en Ejecución**
Descargar **Hola Mundo (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social mencionados:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
