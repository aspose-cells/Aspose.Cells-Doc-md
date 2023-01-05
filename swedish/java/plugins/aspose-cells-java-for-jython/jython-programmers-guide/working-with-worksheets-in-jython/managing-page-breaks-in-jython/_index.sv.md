---
title: Hantera sidbrytningar i Jython
type: docs
weight: 80
url: /sv/java/managing-page-breaks-in-jython/
---
## **Aspose.Cells - Hantera sidbrytningar**
 För att lägga till dokument med hjälp av**Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Code**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ManagingPageBreaks:

    def __init__(self):



        # Adding Page Breaks

        self.add_page_breaks()

        # Clearing All Page Breaks

        self.clear_all_page_breaks()

        # Removing Specific Page Break

        self.remove_page_break()



    def add_page_breaks(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'



        # Instantiating a Workbook object

        workbook = Workbook(dataDir + "Book1.xls")



        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        h_page_breaks = worksheet.getHorizontalPageBreaks()

        h_page_breaks.add("Y30")

        v_page_breaks = worksheet.getVerticalPageBreaks()

        v_page_breaks.add("Y30")

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Add Page Breaks.xls")

        print "Add page breaks, please check the output file."



    def clear_all_page_breaks(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'



        # Instantiating a Workbook object

        workbook = Workbook(dataDir + "Book1.xls")



        workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()

        workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()



        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Clear All Page Breaks.xls")

        print "Clear all page breaks, please check the output file."



    def remove_page_break(dataDir):



        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'



        # Instantiating a Workbook object

        workbook = Workbook(dataDir + "Book1.xls")

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        h_page_breaks = worksheet.getHorizontalPageBreaks()

        h_page_breaks.removeAt(0)

        v_page_breaks = worksheet.getVerticalPageBreaks()

        v_page_breaks.removeAt(0)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Remove Page Break.xls")

        print "Remove page break, please check the output file."



if __name__ == '__main__':        

    ManagingPageBreaks()

{{< /highlight >}}
## **Ladda ner Running Code**
 Ladda ner**Bifoga dokument (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/asposewords/Aspose_Words_Java/releases/tag/Aspose.Words_Java_for_Jython-v1.0.0)
