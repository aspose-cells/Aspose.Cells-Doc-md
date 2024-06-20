---
title: Visa eller dölj rullningsfält i Python
type: docs
weight: 20
url: /sv/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Visa eller dölj rullningsfält**
### **Gömma rad-/kolumnrubriker**
För att dölja rad/kolumnhuvuden med **Aspose.Cells Java för Python**, använd modulen **DisplayHideRowColumnHeaders**.

**Python-kod**

{{< highlight python >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

#Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Göra rad-/kolumnrubriker synliga**
Gör rad- och kolumnhuvuden synliga genom att använda klassen Worksheet metod setRowColumnHeadersVisible(true).

**Python-kod**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Hello World (Aspose.Cells)** från någon av nedan nämnda sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
