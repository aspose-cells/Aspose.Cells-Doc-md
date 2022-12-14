---
title: Python'de Excel Dosyalarını HTML'ye Dönüştürme
type: docs
weight: 10
url: /tr/java/converting-excel-files-to-html-in-python/
---
## **Aspose.Cells - Excel Dosyasını HTML'ye Dönüştürme**
Aspose.Cells for Java'i Python'de kullanarak Excel'i HTML'ye dönüştürmek için çalışma sayfasını çağırmanız yeterlidir_ile_Dönüştürücü modülünün html() yöntemi.

**Python Kod**

{{< highlight "python" >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

# Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)

\# Print message

print "\n Excel to HTML conversion performed successfully."


{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Excel Dosyasını HTML'ye Dönüştürme (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
