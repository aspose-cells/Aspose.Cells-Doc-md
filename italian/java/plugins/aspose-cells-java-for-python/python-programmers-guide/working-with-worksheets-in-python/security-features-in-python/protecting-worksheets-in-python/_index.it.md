---
title: Protezione dei fogli di lavoro in Python
type: docs
weight: 10
url: /it/java/protecting-worksheets-in-python/
---
## **Aspose.Cells - Fogli protettivi**
 Per proteggere il foglio di lavoro utilizzando**Aspose.Cells Java for Python** , chiamata**proteggi_foglio di lavoro** metodo di**protezione** modulo.

**Python Cod**

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
## **Scarica il codice in esecuzione**
 Scaricamento**Protezione dei fogli di lavoro (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
