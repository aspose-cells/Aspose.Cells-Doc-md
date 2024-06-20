---
title: Verwalten von Dokumenteigenschaften in Ruby
type: docs
weight: 90
url: /de/java/managing-document-properties-in-ruby/
---

## **Aspose.Cells - Zugriff auf Dokumenteigenschaften**
Entwickler können den **Index** oder den **Namen** der Eigenschaft verwenden, um eine bestimmte Eigenschaft aus einer **custom_properties**-Sammlung wie im folgenden Beispiel gezeigt zu erhalten.

**Ruby-Code**

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
## **Aspose.Cells - Hinzufügen von benutzerdefinierten Eigenschaften**
Um benutzerdefinierte Dokumenteigenschaften mithilfe von Aspose.Cells Java für Ruby hinzuzufügen, rufen Sie die Methode **add_custom_property** des **Document**-Moduls auf.

**Ruby-Code**

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
## **Aspose.Cells - Entfernen von benutzerdefinierten Eigenschaften**
Um benutzerdefinierte Dokumenteigenschaften mithilfe von Aspose.Cells Java für Ruby zu entfernen, rufen Sie die Methode **remove_custom_property** des **Document**-Moduls auf.

**Ruby-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Zugriff auf Dokumenteigenschaften (Aspose.Cells)** von einer der unten genannten Social-Coding-Seiten herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)
