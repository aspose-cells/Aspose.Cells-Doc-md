---
title: Congelare le riquadre in Python
type: docs
weight: 40
url: /it/java/freeze-panes-in-python/
---

## **Aspose.Cells - Fissa i riquadri**
Per Congelare le riquadre nel documento foglio di calcolo utilizzando **Aspose.Cells Java per Python**, semplicemente invoca il modulo **FreezePanes**.

**Codice Python**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Hello World (Aspose.Cells)** da uno dei siti di codifica sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
