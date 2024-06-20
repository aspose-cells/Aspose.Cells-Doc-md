---
title: Python da Bir Çalışma Sayfasını Gizle veya Göster
type: docs
weight: 50
url: /tr/java/hide-or-unhide-a-worksheet-in-python/
---

## **Aspose.Cells - Bir Çalışsayı Gizle veya Göster**
### **Bir Çalışsayıyı Gizleme**
Aspose.Cells Java for Ruby kullanarak çalışsayıyı gizlemek için **hideunhideworksheet** modülünü çağırın.

**Python Kodu**

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
### **Bir Çalışsayıyı Gösterme**
Geliştiriciler, **Worksheet** sınıfının *setVisible(true)* metodunu kullanarak bir çalışsayıyı görünür yapabilirler.

**Python Kodu**

{{< highlight python >}}

 # Displaying the worksheet of the Excel file

worksheet.setVisible(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Çalışma Sayfasını Gizle veya Göster (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
