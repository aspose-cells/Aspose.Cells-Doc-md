---
title: Mostra o Nascondi Barre di Scorrimento in Python
type: docs
weight: 20
url: /it/java/display-or-hide-scroll-bars-in-python/
---

## **Aspose.Cells - Visualizza o Nascondi Barre di Scorrimento**
### **Nascondere le intestazioni di riga/colonna**
Per nascondere gli header di riga/colonna utilizzando **Aspose.Cells Java per Python**, chiama il modulo **DisplayHideRowColumnHeaders**.

**Codice Python**

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
### **Rendere visibili le intestazioni di riga/colonna**
Rendi visibili header di riga e colonna utilizzando il metodo `setRowColumnHeadersVisible(true)` della classe `Worksheet`.

**Codice Python**

{{< highlight python >}}

 # Displaying the headers of rows and columns

worksheet.setRowColumnHeadersVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Hello World (Aspose.Cells)** da uno dei siti di codifica sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
