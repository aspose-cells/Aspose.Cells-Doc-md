---
title : "Converting Excel to PDF Files in Ruby" 
description : "" 
weight : 24702 
toc : false
type: docs
url: /java/plugins/ruby/guide/files/utility/converting+excel+to+pdf+files+in+ruby/
---

# Aspose.Cells for Java : Converting Excel to PDF Files in Ruby


## Aspose.Cells - Converting Excel to PDF Files

To convert Excel to Pdf file using Aspose.Cells for Java in Ruby, simply invoke excel\_to\_pdf() method of Converter module.

**Ruby Code**

{{< code lang="cs" >}}
def excel_to_pdf(workbook)
    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format
    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."
end 
{{< /code >}}

## Download Running Code

Download **Converting Excel to PDF Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)

