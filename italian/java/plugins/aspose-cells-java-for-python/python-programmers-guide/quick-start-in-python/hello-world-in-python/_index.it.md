---
title: Hello World nel Python
type: docs
weight: 10
url: /it/java/hello-world-in-python/
---
## **Aspose.Cells - Hello World**
Hello World utilizzando Aspose.Cells Java in Python, richiamare semplicemente il metodo HelloWorld() della classe Document e specificare il secondo documento da aggiungere alla fine.

**Python Cod**

{{< highlight "java" >}}

 workbook = self.Workbook()

sheet = workbook.getWorksheets().get(0)

cell = sheet.getCells().get("A1")

cell.setValue("Hello World!")

file_format_type = self.FileFormatType

workbook.save(self.dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Hello World (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
