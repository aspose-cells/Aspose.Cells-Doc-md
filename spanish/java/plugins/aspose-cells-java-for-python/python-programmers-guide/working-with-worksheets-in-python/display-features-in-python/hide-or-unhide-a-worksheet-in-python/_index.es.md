---
title: Ocultar o Mostrar una Hoja de Cálculo en Python
type: docs
weight: 50
url: /es/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Ocultar o mostrar una hoja de trabajo**
### **Ocultar una hoja de trabajo**
Para ocultar una hoja de cálculo usando Aspose.Cells Java para Ruby, llama al módulo **hideunhideworksheet**.

**Código Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Mostrando una hoja de cálculo**
Los desarrolladores pueden hacer que una hoja de cálculo sea visible configurando el método *setVisible(* *true* *)* de la clase **Hoja de cálculo**.

**Código Python**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Ocultar o Mostrar una Hoja de Cálculo (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social mencionados:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
