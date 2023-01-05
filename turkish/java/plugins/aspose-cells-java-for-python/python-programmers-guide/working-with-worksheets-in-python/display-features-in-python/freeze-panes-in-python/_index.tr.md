---
title: Python'de Bölmeleri Dondur
type: docs
weight: 40
url: /tr/java/freeze-panes-in-python/
---
## **Aspose.Cells - Bölmeleri Dondur**
 Kullanarak Elektronik Tablo Belgesindeki Bölmeleri Dondurmak için**Aspose.Cells Java for Python** , sadece çağırmak**Donma bölmeleri** modül.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

# Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Hello World (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
