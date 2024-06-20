---
title: Dividir paneles en Python
type: docs
weight: 70
url: /es/java/split-panes-in-python/
---

## **Aspose.Cells - Dividir paneles**
Para dividir paneles usando **Aspose.Cells Java for Python**, simplemente invoque el módulo **SplitPanes**.

**Código Python**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargue **Dividir paneles (Aspose.Cells)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
