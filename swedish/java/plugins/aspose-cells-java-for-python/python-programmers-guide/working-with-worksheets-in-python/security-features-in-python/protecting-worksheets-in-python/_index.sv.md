---
title: Skyddar arbetsblad på Python
type: docs
weight: 10
url: /sv/java/protecting-worksheets-in-python/
---
## **Aspose.Cells - Skydda arbetsblad**
 För att skydda kalkylblad med hjälp av**Aspose.Cells Java for Python** , ringa upp**protect_worksheet** metod av**skydd** modul.

**Python Kod**

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
## **Ladda ner Running Code**
 Ladda ner**Skyddande arbetsblad (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
