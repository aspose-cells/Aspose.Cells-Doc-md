---
title: Dölj eller visa en arbetsblad i Python
type: docs
weight: 50
url: /sv/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Dölj eller visa en arbetsbok**
### **Dölja ett arbetsblad**
För att dölja arbetsbladet med Aspose.Cells Java för Ruby, anropa modulen **hideunhideworksheet**.

**Python-kod**

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
### **Visa ett arbetsblad**
Utvecklare kan göra ett arbetsblad synligt genom att ställa in *setVisible(* *true* *)* metoden för klassen **Worksheet**.

**Python-kod**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Dölj eller visa ett arbetsblad (Aspose.Cells)** från någon av de nedan angivna sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
