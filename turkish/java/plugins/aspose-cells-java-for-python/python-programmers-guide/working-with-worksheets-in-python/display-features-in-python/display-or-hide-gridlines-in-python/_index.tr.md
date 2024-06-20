---
title: Python da Izgaraları Gösterme veya Gizleme
type: docs
weight: 10
url: /tr/java/display-or-hide-gridlines-in-python/
description: Aspose.Cells for Python Via Java API üzerinden ızgaraları görüntülemeyi veya gizlemeyi öğrenin.
keywords: Python Via Java da ızgaraları görüntüleme veya gizleme, Python Via Java da ızgaraları görüntüleme veya gizleme, Python ile İzgaraları Gösterme veya Gizleme. 
---

## **Aspose.Cells -  Izgaraları Göstermeyi veya Gizlemeyi Nasıl Yapılır**
### **Izgaraları Nasıl Gizlersiniz**
**Aspose.Cells Java for Ruby** kullanarak çalışma sayfasını gizlemek için **displayhidegridlines** modülünü çağırın.

**Python Kodu**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

#Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
### **Izgaraları Nasıl Gösterirsiniz**
Izgaraları görünür yapmak için **Worksheet** sınıfının **setGridlinesVisible(true)** metodunu kullanın.

**Python Kodu**

{{< highlight python >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **DisplayHideGridlines (Aspose.Cells)**'ı indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
