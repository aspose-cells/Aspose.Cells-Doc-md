---
title: Impostazione delle opzioni della pagina in Jython
type: docs
weight: 130
url: /it/java/setting-page-options-in-jython/
---
## **Aspose.Cells - Impostazione Opzioni Pagina**
 Per aggiungere documenti utilizzando**Aspose.Cells Java per Jython**. Qui puoi vedere il codice di esempio.

**Codice Jython**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import PageOrientationType

from java.io import FileInputStream


class SettingPageOptions:

    def __init__(self):





        self.page_orientation()

        self.scaling()

    def page_orientation(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'

        # Instantiating a Workbook object by excel file path

        workbook = Workbook()

        # Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        sheet_index = worksheets.add()

        sheet = worksheets.get(sheet_index)

        # Setting the orientation to Portrait

        page_setup = sheet.getPageSetup()

        page_orientation_type = PageOrientationType

        page_setup.setOrientation(page_orientation_type.PORTRAIT)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Page Orientation.xls")

        print "Set page orientation, please check the output file."



    def scaling(dataDir):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/SettingPageOptions/'



        # Instantiating a Workbook object by excel file path

        workbook = Workbook(dataDir + 'Book1.xls')

        # Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        sheet_index = worksheets.add()

        sheet = worksheets.get(sheet_index)

        # Setting the scaling factor to 100

        page_setup = sheet.getPageSetup()

        page_setup.setZoom(100)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Scaling.xls")

        print "Set scaling, please check the output file."

if __name__ == '__main__':        

    SettingPageOptions()

{{< /highlight >}}
## **Scarica il codice in esecuzione**
 Scarica**Aggiungi documenti (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/SettingPageOptions.py)
