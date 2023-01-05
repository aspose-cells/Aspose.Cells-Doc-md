---
title: Aperçu des sauts de page dans Ruby
type: docs
weight: 70
url: /fr/java/page-break-preview-in-ruby/
---
## **Aspose.Cells - Aperçu des sauts de page**
 Pour définir la feuille de calcul sur l'aperçu des sauts de page à l'aide de**Aspose.Cells Java pour rubis** , invoquez simplement**Aperçu du saut de page** module.

**Code rubis**

{{< highlight "ruby" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

worksheet = worksheets.get(sheet_index)

\# Displaying the worksheet in page break preview

worksheet.setPageBreakPreview(true)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set page break preview, please check the output file."

{{< /highlight >}}
## **Télécharger le code d'exécution**
Télécharger**Aperçu des sauts de page (Aspose.Cells)**à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/pagebreakpreview.rb)
