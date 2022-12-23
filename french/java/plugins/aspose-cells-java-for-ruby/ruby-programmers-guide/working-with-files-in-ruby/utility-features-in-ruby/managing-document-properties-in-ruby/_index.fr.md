---
title: Gestion des propriétés de document dans Ruby
type: docs
weight: 90
url: /fr/java/managing-document-properties-in-ruby/
---
## **Aspose.Cells - Accès aux propriétés du document**
Les développeurs peuvent utiliser le**Indice**ou alors**Nom** de la propriété pour obtenir une propriété spécifique d'un**propriétés_personnalisées**collection comme démontré ci-dessous dans l'exemple.

**Code rubis**

{{< highlight "ruby" >}}

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
## **Aspose.Cells - Ajout de propriétés personnalisées**
Pour ajouter des propriétés de document personnalisées à l'aide de Aspose.Cells Java pour Ruby, appelez**add_custom_property** méthode de la**Document** module.

**Code rubis**

{{< highlight "ruby" >}}

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
## **Aspose.Cells - Suppression des propriétés personnalisées**
 Pour supprimer les propriétés de document personnalisées à l'aide de Aspose.Cells Java pour Ruby, appelez**remove_custom_property** méthode de la**Document** module.

**Code rubis**

{{< highlight "ruby" >}}

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
## **Télécharger le code d'exécution**
 Télécharger**Accès aux propriétés du document (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/document.rb)
