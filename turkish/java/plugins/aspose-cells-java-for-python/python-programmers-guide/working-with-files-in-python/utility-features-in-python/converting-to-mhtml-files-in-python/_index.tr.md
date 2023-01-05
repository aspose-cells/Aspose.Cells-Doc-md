---
title: Python'deki MHTML Dosyalarına Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - MHTML'e Dönüştürme**
Python'de Aspose.Cells for Java'i kullanarak Worksheet'i MHTML dosyasına dönüştürmek için worksheet'i çağırmanız yeterlidir_ile_Dönüştürücü modülünün mhtml() yöntemi.

**Python Kod**

{{< highlight "java" >}}

 saveFormat = self.SaveFormat

# Specify the file path

filePath = self.dataDir + "Book1.xlsx"

# Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

# Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

# Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**MHTML'e Dönüştürme (Aspose.Cells)** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
