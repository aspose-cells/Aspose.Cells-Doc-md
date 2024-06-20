---
title: Geler les volets en Ruby
type: docs
weight: 50
url: /fr/java/freeze-panes-in-ruby/
---

## **Aspose.Cells - Figer les volets**
Pour geler les volets dans le document de feuille de calcul en utilisant Aspose.Cells Java pour Ruby, il suffit d'invoquer le module FreezePanes.

**Code Ruby**

{{< highlight ruby >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

\# Instantiating a Workbook object by excel file path

workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

\# Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(data_dir + "output.xls")

puts "Apply freeze panes settings, please check the output file."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Figer les volets (Aspose.Cells)** sur l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/freezepanes.rb)
