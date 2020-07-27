+++
title = "Managing Document Properties in Ruby" 
description = "" 
weight = 24708 
+++

Aspose.Cells for Java : Managing Document Properties in Ruby  

# Aspose.Cells for Java : Managing Document Properties in Ruby


## Aspose.Cells - Accessing Document Properties

Developers can make use of the**Index**or**Name**of the property to get a specific property from a **custom\_properties**collection as demonstrated below in the example.

**Ruby Code**

{{< code lang="cs" >}}
def get_properties()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file
    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Accessng a custom document property by using the property index
    puts "Property By Index: " +  custom_properties.get(1).to_string

    # Accessng a custom document property by using the property name
    puts "Property By Name: " + custom_properties.get("Publisher").to_string
end
{{< /code >}}

## Aspose.Cells - Adding Custom Properties

To add custom document properties using Aspose.Cells Java for Ruby, call**add****\_custom\_property** method of the **Document** module.

**Ruby Code**

{{< code lang="cs" >}}
def add_custom_property()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file
    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file
    custom_properties.add("Publisher", "Aspose")

    # Save the document in PDF format
    workbook.save(data_dir + "Add_Property.xls")

    puts "Added custom property successfully."
end   
{{< /code >}}

## Aspose.Cells - Removing Custom Properties

To remove custom document properties using Aspose.Cells Java for Ruby, call **remove****\_custom\_property** method of the **Document** module.

**Ruby Code**

{{< code lang="cs" >}}
def remove_custom_property()
    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'
    
    # Instantiating a Workbook object by excel file path
    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Retrieve a list of all custom document properties of the Excel file
    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()

    # Adding a custom document property to the Excel file
    custom_properties.remove("Publisher")

    # Save the document in PDF format
    workbook.save(data_dir + "Removed_Property.xls")

    puts "Removed custom property successfully."
end   
{{< /code >}}

## Download Running Code

Download **Accessing Document Properties (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)

