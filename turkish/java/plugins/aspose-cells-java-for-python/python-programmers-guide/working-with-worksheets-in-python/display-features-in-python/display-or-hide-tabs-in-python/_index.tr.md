---
title: Python'de Sekmeleri Görüntüle veya Gizle
type: docs
weight: 30
url: /tr/java/display-or-hide-tabs-in-python/
---
## **Aspose.Cells - Gizlenen Sekmeleri Görüntüle**
### **Sekmeleri Gizleme**
 kullanarak sekmeleri gizlemek için**Yakut için Aspose.Cells Java** , Arama**sekmeleri göster** modül.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(False)

# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Tabs are now hidden, please check the output file."

{{< /highlight >}}
### **Sekmeleri Görünür Hale Getirmek**
Workbook sınıfının setSheetTabBarHidden(false) yöntemiyle sekmeleri görünür yapın.

**Python Kod**

{{< highlight "python" >}}

 # Displaying the tabs of the Excel file

workbook.getSettings().setSowTabs(true)

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Hello World (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
