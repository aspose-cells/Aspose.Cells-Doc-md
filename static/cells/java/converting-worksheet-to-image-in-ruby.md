##Converting Worksheet to Image in Ruby
## **Aspose.Cells - Converting Worksheet to Image**
To convert Worksheet to Image using Aspose.Cells for Java in Ruby, simply invoke Converter module.
**Ruby Code**
def worksheet_to_image(workbook)
#Create an object for ImageOptions
img_options = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new
# Set the image type
image_format = Rjb::import('com.aspose.cells.ImageFormat')
img_options.setImageFormat(image_format.getPng())
# Get the first worksheet.
sheet = workbook.getWorksheets().get(0)
# Create a SheetRender object for the target sheet
sr = Rjb::import('com.aspose.cells.SheetRender').new(sheet, img_options)
j = 0
while j < sr.getPageCount()
# Generate an image for the worksheet
sr.toImage(j, @data_dir + "mysheetimg_#{j}.png")
j +=1
end
puts "Image saved successfully."
end
## **Download Running Code**
Download **Converting Worksheet to Image (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
