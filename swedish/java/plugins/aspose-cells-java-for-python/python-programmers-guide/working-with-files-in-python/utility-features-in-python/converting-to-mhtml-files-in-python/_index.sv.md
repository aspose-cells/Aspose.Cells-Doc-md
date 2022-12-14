---
title: Konvertera till MHTML-filer i Python
type: docs
weight: 30
url: /sv/java/converting-to-mhtml-files-in-python/
---
## **Aspose.Cells - Konvertering till MHTML**
För att konvertera kalkylblad till MHTML-fil med Aspose.Cells för Java i Python, anropa kalkylblad_till_mhtml()-metoden för konverteringsmodulen.

**Python-kod**

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
## **Ladda ner Running Code**
 Ladda ner**Konvertera till MHTML (Aspose.Cells)** från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
