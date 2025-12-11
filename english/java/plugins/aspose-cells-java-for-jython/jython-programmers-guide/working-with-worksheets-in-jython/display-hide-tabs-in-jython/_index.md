---
title: Display Hide Tabs in Jython
type: docs
weight: 50
url: /java/display-hide-tabs-in-jython/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display Hide Tabs**
To hide tabs in a workbook using **Aspose.Cells Java for Jython**. Here is an example code.

**Jython Code**

{{< highlight java >}}
 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideTabs:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideTabs/'



        workbook = Workbook(dataDir + "Book1.xls")



        # Hiding the tabs of the Excel file
        workbook.getSettings().setShowTabs(False)

        # Saving the modified Excel file in the default (that is Excel 2003) format
        workbook.save(dataDir + "output.xls")

        # Print message
        print "Tabs are now hidden, please check the output file."

if __name__ == '__main__':
    DisplayHideTabs()
{{< /highlight >}}

## **Download Running Code**
Download the sample code (Aspose.Cells) from any of the social coding sites mentioned below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
