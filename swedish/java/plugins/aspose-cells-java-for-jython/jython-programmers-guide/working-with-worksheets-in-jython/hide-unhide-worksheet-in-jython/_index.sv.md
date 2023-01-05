---
title: Göm göm arbetsblad i Jython
type: docs
weight: 70
url: /sv/java/hide-unhide-worksheet-in-jython/
---
## **Aspose.Cells - Göm göm arbetsblad**
 För att lägga till dokument med hjälp av**Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Code**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class HideUnhideWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/HideUnhideWorksheet/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Hiding the first worksheet of the Excel file

        worksheet.setVisible(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Worksheet 1 is now hidden, please check the output document."

if __name__ == '__main__':        

    HideUnhideWorksheet()

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Bifoga dokument (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/HideUnhideWorksheet.py)
