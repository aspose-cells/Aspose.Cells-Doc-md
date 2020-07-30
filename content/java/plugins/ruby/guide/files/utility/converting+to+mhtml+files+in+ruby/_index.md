---
title : "Converting to MHTML Files in Ruby" 
description : "" 
weight : 24704 
toc : false
type: docs
url: /java/plugins/ruby/guide/files/utility/converting+to+mhtml+files+in+ruby/
---

# Aspose.Cells for Java : Converting to MHTML Files in Ruby


## Aspose.Cells - Converting to MHTML Files

To convert Worksheet to MHTML file using Aspose.Cells for Java in Ruby, simply invoke worksheet\_to\_mhtml() method of Converter module.

**Ruby Code**

{{< code lang="cs" >}}
def worksheet_to_mhtml(workbook)
    save_format = Rjb::import('com.aspose.cells.SaveFormat')
    # Specify the HTML saving options
    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document
    workbook.save(@data_dir + "convert.mht", sv)

    puts "MHTML saved successfully."
end
{{< /code >}}

## Download Running Code

Download **Converting to MHTML Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)

