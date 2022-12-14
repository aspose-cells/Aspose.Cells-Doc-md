---
title: Gestion des feuilles de calcul dans Ruby
type: docs
weight: 10
url: /fr/java/managing-worksheets-in-ruby/
---
## **Aspose.Cells - Gestion des feuilles de travail**
### **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour ajouter une feuille de calcul à un nouveau fichier Excel à l'aide**Aspose.Cells Java pour rubis** , il suffit d'appeler**add_worksheet** méthode de**Gestion des feuilles de calcul** module.

**Code rubis**

{{< highlight "ruby" >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Ajout de feuilles de calcul à une feuille de calcul Designer**
Le processus d'ajout de feuilles de calcul à une feuille de calcul de concepteur est entièrement identique à celui de l'approche ci-dessus, sauf que le fichier Excel est déjà créé et que nous devons d'abord ouvrir ce fichier Excel avant d'y ajouter une feuille de calcul.

**Code rubis**

{{< highlight "ruby" >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Accéder aux feuilles de calcul à l'aide du nom de la feuille**
 Pour accéder à la feuille de calcul par nom de feuille à l'aide de**Aspose.Cells Java pour rubis** , il suffit d'appeler**get_worksheet** méthode de**Gestion des feuilles de calcul** module.

**Code rubis**

{{< highlight "ruby" >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Suppression de feuilles de calcul à l'aide du nom de la feuille**
 Pour supprimer une feuille de calcul par nom de feuille à l'aide de**Aspose.Cells Java pour rubis** , il suffit d'appeler**remove_worksheet_by_name** méthode de**Gestion des feuilles de calcul** module.

**Code rubis**

{{< highlight "ruby" >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Suppression de feuilles de calcul à l'aide de l'index des feuilles**
 Pour supprimer une feuille de calcul par index de feuille à l'aide de**Aspose.Cells Java pour rubis** , il suffit d'appeler**remove_worksheet_by_index** méthode de**Gestion des feuilles de calcul** module.

**Code rubis**

{{< highlight "ruby" >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Gestion des feuilles de travail (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
