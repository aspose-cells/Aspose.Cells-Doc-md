---
title: Python'de Bölme Bölmeleri
type: docs
weight: 70
url: /tr/java/split-panes-in-python/
---
## **Aspose.Cells - Bölmeli Bölmeler**
 Kullanarak Bölmeleri Bölmek için**Aspose.Cells Java for Python** , sadece çağırmak**Bölünmüş Paneller** modül.

**Python Kod**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat;

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Set the active cell

workbook.getWorksheets().get(0).setActiveCell("A20");

# Split the worksheet window

workbook.getWorksheets().get(0).split();

# Save the excel file

workbook.save(self.dataDir + "book.out.xls", saveFormat.EXCEL_97_TO_2003);

# Print Message

print "Panes split successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Bölünmüş Bölmeler (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
