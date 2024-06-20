---
title: Configurer les options de la page en Python
type: docs
weight: 10
url: /fr/java/setting-page-options-in-python/
---

## **Aspose.Cells - Définition des options de page**
### **Orientation de la page**
Pour appliquer les paramètres d'orientation de page en utilisant **Aspose.Cells Java pour Ruby**, appelez la méthode **page_orientation** du module **pagesetup**.

**Code Python**

{{< highlight java >}}

 def page_orientation(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the orientation to Portrait

page_setup = sheet.getPageSetup()

page_orientation_type = self.PageOrientationType

page_setup.setOrientation(page_orientation_type.PORTRAIT)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Page_Orientation.xls")

print "Set page orientation, please check the output file."


{{< /highlight >}}
### **Facteur d'échelle**
Pour appliquer la mise à l'échelle à l'aide d'**Aspose.Cells Java pour Python**, appelez la méthode **scaling** du module **pagesetup**.

**Code Python**

{{< highlight python >}}

 def scaling(self):        

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the scaling factor to 100

page_setup = sheet.getPageSetup()

page_setup.setZoom(100)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Scaling.xls")

print "Set scaling, please check the output file."

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Configurer les options de la page (Aspose.Cells)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
