---  
title: Managing Document Properties in Ruby  
type: docs  
weight: 90  
url: /java/managing-document-properties-in-ruby/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Accessing Document Properties**  
Developers can make use of the **Index** or **Name** of the property to get a specific property from a **custom_properties** collection, as demonstrated in the example below.  

**Ruby Code**  

{{< highlight ruby >}}  

def get_properties()  

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'  

  

    # Instantiating a Workbook object by Excel file path  

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')  

    # Retrieve a list of all custom document properties of the Excel file  

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()  

    # Accessing a custom document property by using the property index  

    puts "Property By Index: " +  custom_properties.get(1).to_string  

    # Accessing a custom document property by using the property name  

    puts "Property By Name: " + custom_properties.get("Publisher").to_string  

end  

{{< /highlight >}}  

## **Aspose.Cells - Adding Custom Properties**  
To add custom document properties using Aspose.Cells Java for Ruby, call the **add_custom_property** method of the **Document** module.  

**Ruby Code**  

{{< highlight ruby >}}  

def add_custom_property()  

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'  

  

    # Instantiating a Workbook object by Excel file path  

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')  

    # Retrieve a list of all custom document properties of the Excel file  

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()  

    # Adding a custom document property to the Excel file  

    custom_properties.add("Publisher", "Aspose")  

    # Save the document in PDF format  

    workbook.save(data_dir + "Add_Property.xls")  

    puts "Added custom property successfully."  

end    

{{< /highlight >}}  

## **Aspose.Cells - Removing Custom Properties**  
To remove custom document properties using Aspose.Cells Java for Ruby, call the **remove_custom_property** method of the **Document** module.  

**Ruby Code**  

{{< highlight ruby >}}  

def remove_custom_property()  

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'  

  

    # Instantiating a Workbook object by Excel file path  

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')  

    # Retrieve a list of all custom document properties of the Excel file  

    custom_properties = workbook.getWorksheets().getCustomDocumentProperties()  

    # Removing a custom document property from the Excel file  

    custom_properties.remove("Publisher")  

    # Save the document in PDF format  

    workbook.save(data_dir + "Removed_Property.xls")  

    puts "Removed custom property successfully."  

end    

{{< /highlight >}}  

## **Download Running Code**  
Download **Accessing Document Properties (Aspose.Cells)** from any of the social coding sites mentioned below:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)
