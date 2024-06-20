---
title: Python da Panelleri Böl
type: docs
weight: 70
url: /tr/java/split-panes-in-python/
---

## **Aspose.Cells - Bölünmüş Panolar**
**Aspose.Cells Java for Python** kullanarak Panelleri Bölmek için basitçe **SplitPanes** modülünü çağırın.

**Python Kodu**

{{< highlight java >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

#Split the worksheet window

workbook.getWorksheets().get(0).split();

#Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

#Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Panelleri Böl (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
