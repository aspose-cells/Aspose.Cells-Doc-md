---
title: Converting Excel to PDF Files in Ruby
type: docs
weight: 30
url: /java/converting-excel-to-pdf-files-in-ruby/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Converting Excel to PDF Files**
To convert Excel to PDF files using Aspose.Cells for Java in Ruby, simply invoke the `excel_to_pdf()` method of the Converter module.

**Ruby Code**

{{< highlight ruby >}}
def excel_to_pdf(workbook)
    save_format = Rjb::import('com.aspose.cells.SaveFormat')
    # Save the document in PDF format
    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)
    puts "PDF saved successfully."
end
{{< /highlight >}}

## **Download Sample Code**
Download **Converting Excel to PDF Files (Aspose.Cells)** from any of the social coding sites listed below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
