---
title: Gestion des feuilles de calcul en Ruby
type: docs
weight: 10
url: /fr/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Gestion des feuilles de calcul**
### **Ajout de feuilles de calcul à un nouveau fichier Excel**
Pour ajouter une feuille de calcul à un nouveau fichier Excel en utilisant Aspose.Cells Java pour Ruby, appeler simplement la méthode add_worksheet du module MangingWorksheets.

**Code Ruby**

{{< highlight ruby >}}

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
Le processus d'ajout de feuilles de calcul à une feuille de calcul conçue est entièrement identique à celui de l'approche ci-dessus, sauf que le fichier Excel est déjà créé et nous devons d'abord ouvrir ce fichier Excel avant d'ajouter une feuille de calcul.

**Code Ruby**

{{< highlight ruby >}}

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
### **Accéder aux feuilles de calcul en utilisant le nom de la feuille**
Pour accéder à une feuille de calcul par son nom de feuille en utilisant Aspose.Cells Java pour Ruby, appeler simplement la méthode get_worksheet du module MangingWorksheets.

**Code Ruby**

{{< highlight ruby >}}

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
### **Suppression des feuilles de calcul en utilisant le nom de la feuille**
Pour supprimer une feuille de calcul par son nom de feuille en utilisant Aspose.Cells Java pour Ruby, appeler simplement la méthode remove_worksheet_by_name du module MangingWorksheets.

**Code Ruby**

{{< highlight ruby >}}

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
### **Suppression des feuilles de calcul en utilisant l'indice de la feuille**
Pour supprimer une feuille de calcul par son indice de feuille en utilisant Aspose.Cells Java pour Ruby, appeler simplement la méthode remove_worksheet_by_index du module MangingWorksheets.

**Code Ruby**

{{< highlight ruby >}}

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
## **Télécharger le code en cours d'exécution**
Téléchargez **Managing Worksheets (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
