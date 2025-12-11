---  
title: Converting to MHTML Files in Ruby  
type: docs  
weight: 50  
url: /java/converting-to-mhtml-files-in-ruby/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Converting to MHTML Files**  
To convert a worksheet to an MHTML file using Aspose.Cells for Java in Ruby, simply invoke the `worksheet_to_mhtml()` method of the Converter module.  

**Ruby Code**  

{{< highlight ruby >}}  

def worksheet_to_mhtml(workbook)  

    save_format = Rjb::import('com.aspose.cells.SaveFormat')  

    # Specify the HTML saving options  

    sv = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)  

    # Save the document  

    workbook.save(@data_dir + "convert.mht", sv)  

    puts "MHTML saved successfully."  

end  

{{< /highlight >}}  

## **Download Running Code**  
Download **Converting to MHTML Files (Aspose.Cells)** from any of the social coding sites listed below:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
