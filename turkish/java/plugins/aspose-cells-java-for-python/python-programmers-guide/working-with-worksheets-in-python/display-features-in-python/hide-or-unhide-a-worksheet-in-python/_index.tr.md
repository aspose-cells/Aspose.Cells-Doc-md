---
title: Python'de bir Çalışma Sayfasını Gizle veya Göster
type: docs
weight: 50
url: /tr/java/hide-or-unhide-a-worksheet-in-python/
---
## **Aspose.Cells - Bir Çalışma Sayfasını Gizle veya Göster**
### **Bir Çalışma Sayfasını Gizleme**
 Ruby için Aspose.Cells Java kullanarak çalışma sayfasını gizlemek için arayın**çalışma sayfasını gizle** modül.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the first worksheet of the Excel file

worksheet.setVisible(True)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Worksheet 1 is now hidden, please check the output document."

{{< /highlight >}}
### **Çalışma Sayfası Gösterme**
Geliştiriciler, ayarlayarak bir çalışma sayfasını görünür yapabilir.*setVisible(* *doğru* *)*yöntemi**Çalışma kağıdı**sınıf.

**Python Kod**

{{< highlight "python" >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Bir Çalışma Sayfasını Gizle veya Göster (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
