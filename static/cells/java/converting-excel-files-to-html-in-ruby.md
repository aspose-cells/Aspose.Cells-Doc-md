##Converting Excel Files to HTML in Ruby
## **Aspose.Cells - Converting Excel Files to HTML**
To convert Excel to HTML using Aspose.Cells for Java in Ruby, simply invoke worksheet_to_html() method of Converter module.
**Ruby Code**
def worksheet_to_html(workbook)
save_format = Rjb::import('com.aspose.cells.SaveFormat')
# Specify the HTML saving options
save = Rjb::import('com.aspose.cells.HtmlSaveOptions').new(save_format.M_HTML)
# Save the document
workbook.save(@data_dir + "output.html", save)
puts "HTML saved successfully."
end
## **Download Running Code**
Download **Converting Excel Files to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
