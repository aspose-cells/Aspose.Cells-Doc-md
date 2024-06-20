---
title: Python da MHTML Dosyalarına Dönüştürme
type: docs
weight: 30
url: /tr/java/converting-to-mhtml-files-in-python/
---

## **Aspose.Cells - MHTML'ye Dönüştürme**
Python'da Aspose.Cells for Java kullanarak Çalışsayfayı MHTML dosyasına dönüştürmek için, Converter modülünün worksheet_to_mhtml() yöntemini basitçe çağırın.

**Python Kodu**

{{< highlight java >}}

 saveFormat = self.SaveFormat

#Specify the file path

filePath = self.dataDir + "Book1.xlsx"

#Specify the HTML saving options

sv = self.HtmlSaveOptions(saveFormat.M_HTML)

#Instantiate a workbook and open the template XLSX file

wb = self.Workbook(filePath)

#Save the MHT file

wb.save(filePath + ".out.mht", sv)

\# Print message

print "Excel to MHTML conversion performed successfully."

{{< /highlight >}}
## **Çalışan Kodu İndir**
Altta belirtilen sosyal kodlama sitelerinden herhangi birinden  **MHTML'ye Dönüştürme (Aspose.Cells)**'ı İndir

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
