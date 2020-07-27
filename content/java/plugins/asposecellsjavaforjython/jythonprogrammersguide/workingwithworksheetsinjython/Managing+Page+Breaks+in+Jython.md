+++
title = "Managing Page Breaks in Jython" 
description = "" 
weight = 20812 
+++

Aspose.Cells for Java : Managing Page Breaks in Jython  

# Aspose.Cells for Java : Managing Page Breaks in Jython


## Aspose.Cells - Managing Page Breaks

To append documents using **Aspose.Cells Java for Jython**. Here you can see example code.

**Jython Code**

from aspose-cells import Settingsfrom com.aspose.cells import Workbookfrom com.aspose.cells import SaveFormatclass ManagingPageBreaks:    def \_\_init\_\_(self):                # Adding Page Breaks        self.add\_page\_breaks()        # Clearing All Page Breaks        self.clear\_all\_page\_breaks()        # Removing Specific Page Break        self.remove\_page\_break()            def add\_page\_breaks(dataDir):                dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'                # Instantiating a Workbook object        workbook = Workbook(dataDir + "Book1.xls")            worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        h\_page\_breaks = worksheet.getHorizontalPageBreaks()        h\_page\_breaks.add("Y30")        v\_page\_breaks = worksheet.getVerticalPageBreaks()        v\_page\_breaks.add("Y30")        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Add Page Breaks.xls")        print "Add page breaks, please check the output file."        def clear\_all\_page\_breaks(dataDir):                dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'                # Instantiating a Workbook object        workbook = Workbook(dataDir + "Book1.xls")            workbook.getWorksheets().get(0).getHorizontalPageBreaks().clear()        workbook.getWorksheets().get(0).getVerticalPageBreaks().clear()                # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Clear All Page Breaks.xls")        print "Clear all page breaks, please check the output file."        def remove\_page\_break(dataDir):            dataDir = Settings.dataDir + 'WorkingWithWorksheets/ManagingPageBreaks/'                # Instantiating a Workbook object        workbook = Workbook(dataDir + "Book1.xls")        worksheets = workbook.getWorksheets()        worksheet = worksheets.get(0)        h\_page\_breaks = worksheet.getHorizontalPageBreaks()        h\_page\_breaks.removeAt(0)        v\_page\_breaks = worksheet.getVerticalPageBreaks()        v\_page\_breaks.removeAt(0)        # Saving the modified Excel file in default (that is Excel 2003) format        workbook.save(dataDir + "Remove Page Break.xls")        print "Remove page break, please check the output file."    if \_\_name\_\_ == '\_\_main\_\_':            ManagingPageBreaks()

## Download Running Code

Download **Append Documents (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [CodePlex](https://asposewordsjavajython.codeplex.com/releases/view/619260)
*   [GitHub](https://github.com/asposewords/Aspose_Words_Java/releases/tag/Aspose.Words_Java_for_Jython-v1.0.0)

