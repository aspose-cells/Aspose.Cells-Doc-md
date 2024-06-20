---
title: Gestione delle proprietà del documento in Ruby
type: docs
weight: 90
url: /it/java/managing-document-properties-in-ruby/
---

## **Aspose.Cells - Accesso alle proprietà del documento**
Gli sviluppatori possono utilizzare l'**Indice** o il **Nome** della proprietà per ottenere una proprietà specifica da una collezione di **custom_properties** come mostrato di seguito nell'esempio.

**Codice Ruby**

{{< highlight ruby >}}

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

{{< /highlight >}}
## **Aspose.Cells - Aggiunta di proprietà personalizzate**
Per aggiungere proprietà del documento personalizzate usando Aspose.Cells Java per Ruby, chiamare il metodo **add_custom_property** del modulo **Documento**.

**Codice Ruby**

{{< highlight ruby >}}

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

{{< /highlight >}}
## **Aspose.Cells - Rimozione delle proprietà personalizzate**
Per rimuovere le proprietà del documento personalizzate usando Aspose.Cells Java per Ruby, chiamare il metodo **remove_custom_property** del modulo **Documento**.

**Codice Ruby**

{{< highlight ruby >}}

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

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Accesso alle proprietà del documento (Aspose.Cells)** da uno dei siti di codice sociale di seguito elencati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)
