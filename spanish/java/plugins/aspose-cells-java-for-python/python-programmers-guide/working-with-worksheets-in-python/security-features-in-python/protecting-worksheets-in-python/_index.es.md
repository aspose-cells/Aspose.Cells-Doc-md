---
title: Protección de hojas de trabajo en Python
type: docs
weight: 10
url: /es/java/protecting-worksheets-in-python/
---
## **Aspose.Cells - Hojas de trabajo de protección**
 Para proteger la hoja de trabajo usando**Aspose.Cells Java para Python** , llamar**proteger_hoja de trabajo** método de**proteccion** módulo.

**Código Python**

{{< highlight "java" >}}

 #Instantiating a Excel object by excel file path

excel = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = excel.getWorksheets()

worksheet = worksheets.get(0)

protection = worksheet.getProtection()

# The following 3 methods are only for Excel 2000 and earlier formats

protection.setAllowEditingContent(False)

protection.setAllowEditingObject(False)

protection.setAllowEditingScenario(False)

# Protects the first worksheet with a password "1234"

protection.setPassword("1234")

# Saving the modified Excel file in default format

excel.save(self.dataDir + "output.xls")

# Print Message

print "Sheet protected successfully."

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Hojas de trabajo de protección (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
