---
title: Python da Sekmeleri Göster veya Gizle.
type: docs
weight: 30
url: /tr/java/display-or-hide-tabs-in-python/
---

## **Aspose.Cells - Sekmeleri Göster veya Gizle**
### **Sekmeleri Gizleme**
Aspose.Cells Java for Ruby ile sekmeleri gizlemek için **displayhidetabs** modülünü çağırın.

**Python Kodu**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

#Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Sekmeleri Görünür Yapma**
workbook sınıfının setSheetTabBarHidden(false) metodunu kullanarak sekmeleri görünür yapın.

**Python Kodu**

{{< highlight python >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Merhaba Dünya (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
