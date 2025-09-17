##Display or Hide Gridlines in Ruby
## **Aspose.Cells - Display or Hide Gridlines**
### **Hiding Gridlines**
To hide worksheet using **Aspose.Cells Java for Ruby**, call **displayhidegridlines** module.
**Ruby Code**
data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
\# Instantiating a Workbook object by excel file path
workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')
\# Accessing the first worksheet in the Excel file
worksheets = workbook.getWorksheets()
sheet_index = worksheets.add()
worksheet = worksheets.get(sheet_index)
\# Hiding the gridlines of the first worksheet of the Excel file
worksheet.setGridlinesVisible(false)
\# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(data_dir + "output.xls")
puts "Gridlines are now hidden, please check the output file."
### **Making Gridlines Visible**
To make gridlines visible, use the the Worksheet class' setGridlinesVisible(true) method.
**Ruby Code**
# Displaying the gridlines of the worksheet
worksheet.setGridlinesVisible(true)
## **Download Running Code**
Download **Display or Hide Gridlines (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/displayhidegridlines.rb)
