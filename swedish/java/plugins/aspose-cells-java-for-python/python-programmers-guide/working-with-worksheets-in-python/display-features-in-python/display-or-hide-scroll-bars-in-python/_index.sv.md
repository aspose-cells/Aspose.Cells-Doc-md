---
title: Visa eller dölj rullningslister i Python
type: docs
weight: 20
url: /sv/java/display-or-hide-scroll-bars-in-python/
---
## **Aspose.Cells - Visa eller dölj rullningslister**
### **Döljer rad-/kolumnrubriker**
 För att dölja rad-/kolumnrubriker med hjälp av**Aspose.Cells Java för Python** , ringa upp**DisplayHideRowColumnHeaders** modul.

**Python-kod**

{{< highlight "python" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(False)

# Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Scroll bars are now hidden, please check the output document."

{{< /highlight >}}
### **Gör rad-/kolumnrubriker synliga**
Gör rad- och kolumnrubriker synliga genom att använda arbetsbladsklassens setRowColumnHeadersVisible(true) metod.

**Python-kod**

{{< highlight "python" >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Hello World (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
