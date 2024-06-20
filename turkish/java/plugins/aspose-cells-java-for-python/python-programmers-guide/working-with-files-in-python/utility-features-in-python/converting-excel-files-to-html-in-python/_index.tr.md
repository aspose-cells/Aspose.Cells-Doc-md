---
title: Python da Excel Dosyalarını HTML e Dönüştürme
type: docs
weight: 10
url: /tr/java/converting-excel-files-to-html-in-python/
---

## **Aspose.Cells - Excel Dosyasını HTML'e Dönüştürme**
Python'da **Aspose.Cells for Java**'i kullanarak Excel'i HTML'e dönüştürmek için, sadece Converter modülünün worksheet_to_html() yöntemini çağırın.

**Python Kodu**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Excel Dosyasını HTML'e Dönüştürme (Aspose.Cells)**'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
