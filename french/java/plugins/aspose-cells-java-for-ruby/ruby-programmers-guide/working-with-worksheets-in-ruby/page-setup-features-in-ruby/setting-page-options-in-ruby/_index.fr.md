---
title: Paramétrer les options de page en Ruby
type: docs
weight: 10
url: /fr/java/setting-page-options-in-ruby/
---

## **Aspose.Cells - Définition des options de page**
### **Orientation de la page**
Pour appliquer les paramètres d'orientation de page en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **page_orientation** du module **pagesetup**.

**Code Ruby**

{{< highlight ruby >}}

 def page_orientation()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the orientation to Portrait

    page_setup = sheet.getPageSetup()

    page_orientation_type = Rjb::import('com.aspose.cells.PageOrientationType')

    page_setup.setOrientation(page_orientation_type.PORTRAIT)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Page Orientation.xls")

    puts "Set page orientation, please check the output file."

end   

{{< /highlight >}}
### **Facteur d'échelle**
Pour appliquer une mise à l'échelle en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **scaling** du module **pagesetup**.

**Code Ruby**

{{< highlight ruby >}}

 def scaling()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')



    # Accessing the first worksheet in the Excel file

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    sheet = worksheets.get(sheet_index)

    # Setting the scaling factor to 100

    page_setup = sheet.getPageSetup()

    page_setup.setZoom(100)



    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Scaling.xls")

    puts "Set scaling, please check the output file."

end


{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Setting Page Options (Aspose.Cells)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagesetup.rb)
