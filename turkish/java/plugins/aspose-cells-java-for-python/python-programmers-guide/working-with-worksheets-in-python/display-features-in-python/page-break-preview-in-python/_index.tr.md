---
title: Python da Sayfa Aralığı Önizlemesi
type: docs
weight: 60
url: /tr/java/page-break-preview-in-python/
---

## **Aspose.Cells - Hello World**
**Aspose.Cells Java for Python** kullanarak çalışma sayfasını sayfa aralığı önizlemesine ayarlamak için basitçe **PageBreakPreview** modülünü çağırın.

**Python Kodu**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Adding a new worksheet to the Workbook object

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(True)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Page break preview is enabled for sheet 1, please check the output document." 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi bir sosyal kodlama sitesinden **Sayfa Aralığı Önizlemesi (Aspose.Cells)**'ı indirin

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
