---
title: Facteur de zoom en Ruby
type: docs
weight: 90
url: /fr/java/zoom-factor-in-ruby/
---

## **Aspose.Cells - Facteur de zoom**
Pour définir le facteur de zoom en utilisant Aspose.Cells Java pour Ruby, il suffit d'invoquer le module ZoomFactor.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Setting the zoom factor of the worksheet to 75     

worksheet.setZoom(75)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Set zoom factor, please check the output file."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez Zoom Factor (Aspose.Cells) à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/zoomfactor.rb)
