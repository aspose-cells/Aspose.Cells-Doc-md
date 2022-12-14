---
title: Hello World à Python
type: docs
weight: 10
url: /fr/java/hello-world-in-python/
---
## **Aspose.Cells - Hello World**
Hello World en utilisant Aspose.Cells Java dans Python, invoquez simplement la méthode HelloWorld() de la classe Document et spécifiez le deuxième document à ajouter à la fin.

**Code Python**

{{< highlight "java" >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Hello World (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
