##Converting HTML files to Excel Spreadsheets in Ruby
## **Aspose.Cells - Converting HTML files to Excel Spreadsheets**
To convert HTML to Spreadsheet using Aspose.Cells for Java in Ruby, simply invoke html_to_excel() method of Converter module.
**Ruby Code**
def html_to_excel()
load_format = Rjb::import('com.aspose.cells.LoadFormat')
# Create an instance of HTMLLoadOptions and initiate it with appropriate LoadFormat
options = Rjb::import('com.aspose.cells.HTMLLoadOptions').new(load_format.HTML)
# Load the Html file through file path while passing the instance of HTMLLoadOptions class
workbook = Rjb::import('com.aspose.cells.Workbook').new(@data_dir + "index.html", options)
save_format = Rjb::import('com.aspose.cells.SaveFormat')
#Save the results to disc in Xlsx format
workbook.save(@data_dir + "output.xlsx", save_format.XLSX)
puts "XLSX saved successfully."
end
## **Download Running Code**
Download **Converting HTML files to Excel Spreadsheets (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
