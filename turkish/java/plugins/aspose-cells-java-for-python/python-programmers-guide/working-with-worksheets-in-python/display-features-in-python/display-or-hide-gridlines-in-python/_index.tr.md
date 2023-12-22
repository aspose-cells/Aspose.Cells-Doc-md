---
title: Python'de Kılavuz Çizgilerini Görüntüleme veya Gizleme
type: docs
weight: 10
url: /tr/java/display-or-hide-gridlines-in-python/
description: Aspose.Cells for Python Via Java API aracılığıyla Kılavuz Çizgilerini nasıl Görüntüleyeceğinizi veya Gizleyeceğinizi öğrenin.
keywords: How to Display or Hide Gridlines in Python Via Java, Display or Hide Gridlines using Python Via Java, Python Show or Hide Gridlines. 
---
##  **Aspose.Cells - Kılavuz Çizgileri Nasıl Görüntülenir veya Gizlenir**
###  **Kılavuz Çizgileri Nasıl Gizlenir?**
 Çalışma sayfasını kullanarak gizlemek için**Ruby** için Aspose.Cells Java'i arayın, **displayhideggridlines'ı arayın** modülü.

**Python Kodu**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Hiding the grid lines of the first worksheet of the Excel file

worksheet.setGridlinesVisible(False)

# Saving the modified Excel file in default (that is Excel 2000) format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Grid lines are now hidden on sheet 1, please check the output document."

{{< /highlight >}}
###  **Kılavuz Çizgileri Nasıl Görüntülenir?**
Kılavuz çizgilerini görünür kılmak için Worksheet sınıfının setGridlinesVisible(true) yöntemini kullanın.

**Python Kodu**

{{< highlight "python" >}}

 # Displaying the gridlines of the worksheet

worksheet.setGridlinesVisible(True)

{{< /highlight >}}
##  **Çalışan Kodu İndir**
 İndirmek**DisplayHideGridlines (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
