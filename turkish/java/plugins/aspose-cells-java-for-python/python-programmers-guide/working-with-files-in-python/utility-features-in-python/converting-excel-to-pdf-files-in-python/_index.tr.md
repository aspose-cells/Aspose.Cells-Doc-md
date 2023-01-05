---
title: Python'de Excel'i PDF Dosyalarına Dönüştürme
type: docs
weight: 20
url: /tr/java/converting-excel-to-pdf-files-in-python/
---
## **Aspose.Cells - Excel'i PDF'ye Dönüştürme**
Aspose.Cells for Java'i Python'de kullanarak Excel'i PDF dosyasına dönüştürmek için excel'i çağırmanız yeterlidir_ile_Dönüştürücü modülünün pdf() yöntemi.

**Python Kod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Excel'i PDF'ye Dönüştürme (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
