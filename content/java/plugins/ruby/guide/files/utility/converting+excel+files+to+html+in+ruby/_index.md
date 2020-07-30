---
title : "Converting Excel Files to HTML in Ruby" 
description : "" 
weight : 24701 
toc : false
type: docs
url: /java/plugins/ruby/guide/files/utility/converting+excel+files+to+html+in+ruby/
---

# Aspose.Cells for Java : Converting Excel Files to HTML in Ruby


## Aspose.Cells - Converting Excel Files to HTML

To convert Excel to HTML using Aspose.Cells for Java in Ruby, simply invoke worksheet\_to\_html() method of Converter module.

**Ruby Code**

{{< code lang="cs" >}}
def worksheet_to_html(workbook)
    save_format = Rjb::import('com.aspose.cells.SaveFormat')
    # Specify the HTML saving options
    save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)

    # Save the document
    workbook.save(@data_dir + "output.html", save)

    puts "HTML saved successfully."
end 
{{< /code >}}

## Download Running Code

Download **Converting Excel Files to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)

