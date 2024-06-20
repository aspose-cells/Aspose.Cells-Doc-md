---
title: Python da Excel Dosyalarını PDF Dosyalarına Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Excel'i Pdf'e Dönüştürme**
Python'da Aspose.Cells for Java kullanarak Excel'i Pdf dosyasına dönüştürmek için, Converter modülünün excel_to_pdf() yöntemini basitçe çağırın.

**Python Kodu**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
Altta belirtilen sosyal kodlama sitelerinden herhangi birinden  **Excel'i Pdf'e Dönüştürme (Aspose.Cells)**'ı İndir

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
