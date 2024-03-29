﻿---
title: Gestione delle interruzioni di pagina in Python
type: docs
weight: 20
url: /it/java/managing-page-breaks-in-python/
---
## **Aspose.Cells - Gestione interruzioni di pagina**
### **Aggiunta di interruzioni di pagina**
 Per aggiungere interruzioni di pagina utilizzando**Aspose.Cells Java per Rubino** , chiamata**add_page_breaks** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Python Cod**

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
### **Cancellazione di tutte le interruzioni di pagina**
 Per cancellare tutte le interruzioni di pagina utilizzando**Aspose.Cells Java for Python** , chiamata**cancella_tutte_le_interruzioni_di_pagina** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Python Cod**

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
### **Rimozione di un'interruzione di pagina specifica**
 Per rimuovere un'interruzione di pagina specifica utilizzando**Aspose.Cells Java for Python** , chiamata**remove_page_break** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Python Cod**

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
## **Scarica il codice in esecuzione**
 Scaricamento**Gestione interruzioni di pagina (Aspose.Cells)** da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
