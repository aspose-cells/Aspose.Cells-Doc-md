##Zoom Factor in Ruby
## **Aspose.Cells - Zoom Factor**
To set Zoom Factor using **Aspose.Cells Java for Ruby**, simply invoke **ZoomFactor** module.
**Ruby Code**
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
\# Instantiating a Workbook object by excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')
\# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
worksheet = worksheets.get(0)
\# Setting the zoom factor of the worksheet to 75
worksheet.setZoom(75)
\# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(data_dir + "output.xls")
puts "Set zoom factor, please check the output file."
## **Download Running Code**
Download **Zoom Factor (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
