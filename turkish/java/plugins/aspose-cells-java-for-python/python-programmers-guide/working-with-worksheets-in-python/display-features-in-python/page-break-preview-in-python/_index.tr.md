---
title: Python'de Sayfa Sonu Önizlemesi
type: docs
weight: 60
url: /tr/java/page-break-preview-in-python/
---
## **Aspose.Cells - Hello World**
 Çalışma sayfasını kullanarak sayfa sonu önizlemesini ayarlamak için**Aspose.Cells Java for Python** , sadece çağırmak**PageBreakÖnizleme** modül.

**Python Kod**

{{< highlight "java" >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

# Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

# Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Sayfa Sonu Önizlemesi (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
