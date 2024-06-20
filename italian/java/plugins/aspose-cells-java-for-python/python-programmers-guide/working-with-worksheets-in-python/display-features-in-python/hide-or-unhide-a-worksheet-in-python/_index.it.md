---
title: Nascondi o Mostra un Foglio di Lavoro in Python
type: docs
weight: 50
url: /it/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Nascondi o Mostra un Foglio**
### **Nascondere un foglio di lavoro**
Per nascondere il foglio utilizzando Aspose.Cells Java per Ruby, chiama il modulo **hideunhideworksheet**.

**Codice Python**

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
### **Visualizzazione di un Foglio**
Gli sviluppatori possono rendere visibile un foglio impostando il metodo *setVisible(true)* della classe **Worksheet**.

**Codice Python**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Nascondi o Mostra un Foglio di Lavoro (Aspose.Cells)** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
