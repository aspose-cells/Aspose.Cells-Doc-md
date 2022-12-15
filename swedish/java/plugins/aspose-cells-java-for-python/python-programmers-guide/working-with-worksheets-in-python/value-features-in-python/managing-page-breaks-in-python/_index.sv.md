---
title: Hantera sidbrytningar i Python
type: docs
weight: 20
url: /sv/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - Hantera sidbrytningar**
### **Lägga till sidbrytningar**
 För att lägga till sidbrytningar med hjälp av**Aspose.Cells Java för Ruby** , ringa upp**add_page_breaks** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Python Kod**

{{< highlight "python" >}}

 def add_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.add("Y30")

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.add("Y30")

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Add Page Breaks.xls")

print "Add page breaks, please check the output file."


{{< /highlight >}}
### **Rensa alla sidbrytningar**
 För att rensa alla sidbrytningar med**Aspose.Cells Java for Python** , ringa upp**rensa_alla_sidebrytningar** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Python Kod**

{{< highlight "python" >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
### **Ta bort specifik sidbrytning**
 För att ta bort specifik sidbrytning med**Aspose.Cells Java for Python** , ringa upp**remove_page_break** metod av**sidbrytningar** modul. Nedan kan du se kodexempel.

**Python Kod**

{{< highlight "python" >}}



def remove_page_break(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

h_page_breaks = worksheet.getHorizontalPageBreaks()

h_page_breaks.removeAt(0)

v_page_breaks = worksheet.getVerticalPageBreaks()

v_page_breaks.removeAt(0)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Remove Page Break.xls")

print "Remove page break, please check the output file."


{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Hantera sidbrytningar (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
