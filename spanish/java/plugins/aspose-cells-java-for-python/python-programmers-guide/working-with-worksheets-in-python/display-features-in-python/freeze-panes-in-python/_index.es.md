---
title: Congelar paneles en Python
type: docs
weight: 40
url: /es/java/freeze-panes-in-python/
---
## **Aspose.Cells - Congelar paneles**
 Para congelar paneles en el documento de hoja de cálculo usando**Aspose.Cells Java para Python** , simplemente invocar**FreezePanes** módulo.

**Código Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Hello World (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
