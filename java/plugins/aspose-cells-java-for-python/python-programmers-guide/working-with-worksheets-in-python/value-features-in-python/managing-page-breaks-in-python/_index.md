---
title: Managing Page Breaks in Python
type: docs
weight: 20
url: /java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Managing Page Breaks**
##### **Adding Page Breaks**
To add page breaks using **Aspose.Cells Java for Ruby**, call **add_page_breaks** method of **pagebreaks** module. Below you can see code example.

**Python Code**

{{< highlight python >}}

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
##### **Clearing All Page Breaks**
To clear all page breaks using **Aspose.Cells Java for Python**, call **clear_all_page_breaks** method of **pagebreaks** module. Below you can see code example.

**Python Code**

{{< highlight python >}}



def clear_all_page_breaks(self):

\# Instantiating a Workbook object

workbook = self.Workbook(self.dataDir + "Book1.xls")


workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Clear All Page Breaks.xls")

print "Clear all page breaks, please check the output file."


{{< /highlight >}}
##### **Removeing Specific Page Break**
To remove specific page break using **Aspose.Cells Java for Python**, call **remove_page_break** method of **pagebreaks** module. Below you can see code example.

**Python Code**

{{< highlight python >}}



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
## **Download Running Code**
Download **Managing Page Breaks (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
- [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)
