---
title: Converting Excel to PDF Files in Python
type: docs
weight: 20
url: /java/converting-excel-to-pdf-files-in-python/
---

## **Aspose.Cells - Converting Excel To Pdf**
To convert Excel to Pdf file using Aspose.Cells for Java in Python, simply invoke excel_to_pdf() method of Converter module.

**Python Code**

{{< highlight python >}}

 saveFormat = self.SaveFormat

workbook = self.Workbook(self.dataDir + "Book1.xls")

#Save the document in PDF format

workbook.save(self.dataDir + "OutBook1.pdf", saveFormat.PDF)

\# Print message

print "\n Excel to PDF conversion performed successfully."

{{< /highlight >}}
## **Download Running Code**
Download **Converting Excel To Pdf (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
- [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)
