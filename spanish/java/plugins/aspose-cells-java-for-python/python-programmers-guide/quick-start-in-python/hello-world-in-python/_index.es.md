---
title: Hola Mundo en Python
type: docs
weight: 10
url: /es/java/hello-world-in-python/
---

## **Aspose.Cells - Hello World**
Hola Mundo usando Aspose.Cells Java en Python, simplemente invoque el método HelloWorld() de la clase Document y especifique el segundo documento para añadir al final.

**Código Python**

{{< highlight java >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Hola Mundo (Aspose.Cells)** desde cualquiera de los siguientes sitios de codificación social mencionados:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
