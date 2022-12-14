---
title: Ocultar o mostrar una hoja de trabajo en Python
type: docs
weight: 50
url: /es/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - Ocultar o mostrar una hoja de trabajo**
### **Ocultar una hoja de trabajo**
 Para ocultar la hoja de trabajo usando Aspose.Cells Java para Ruby, llame**ocultarunhideworksheet** módulo.

**Código Python**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Mostrando una hoja de trabajo**
Los desarrolladores pueden hacer que una hoja de trabajo sea visible configurando el*establecerVisible(* *verdadero* *)*metodo de la**Hoja de cálculo**clase.

**Código Python**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Descargar código de ejecución**
 Descargar**Ocultar o mostrar una hoja de trabajo (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
