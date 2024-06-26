---
title: Gestione degli interruzioni di pagina in Python
type: docs
weight: 20
url: /it/java/managing-page-breaks-in-python/
---

## **Aspose.Cells - Gestisci interruzioni di pagina**
### **Aggiunta dei salti di pagina**
Per aggiungere interruzioni di pagina utilizzando **Aspose.Cells Java per Ruby**, chiama il metodo **add_page_breaks** del modulo **pagebreaks**. Di seguito puoi vedere un esempio di codice.

**Codice Python**

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
### **Cancellazione di tutte le interruzioni di pagina**
Per eliminare tutti i interruzioni di pagina utilizzando **Aspose.Cells Java for Python**, chiamare il metodo **clear_all_page_breaks** del modulo **pagebreaks**. Qui sotto puoi vedere un esempio di codice.

**Codice Python**

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
### **Rimuovere interruzione di pagina specifica**
Per rimuovere un'interruzione di pagina specifica utilizzando **Aspose.Cells Java for Python**, chiamare il metodo **remove_page_break** del modulo **pagebreaks**. Qui sotto puoi vedere un esempio di codice.

**Codice Python**

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
## **Scarica il codice in esecuzione**
Scarica **Gestione delle interruzioni di pagina (Aspose.Cells)** da uno dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
