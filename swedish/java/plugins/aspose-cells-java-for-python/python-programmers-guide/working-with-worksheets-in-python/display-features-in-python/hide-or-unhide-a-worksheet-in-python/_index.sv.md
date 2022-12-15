---
title: Dölj eller visa ett kalkylblad i Python
type: docs
weight: 50
url: /sv/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - Dölj eller visa ett kalkylblad**
### **Dölja ett arbetsblad**
 För att dölja kalkylblad med Aspose.Cells Java för Ruby, ring**hideunhideworksheet** modul.

**Python Kod**

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
### **Visar ett arbetsblad**
Utvecklare kan göra ett kalkylblad synligt genom att ställa in*setVisible(* *Sann* *)*metod för**Arbetsblad**klass.

**Python Kod**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Dölj eller visa ett kalkylblad (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
