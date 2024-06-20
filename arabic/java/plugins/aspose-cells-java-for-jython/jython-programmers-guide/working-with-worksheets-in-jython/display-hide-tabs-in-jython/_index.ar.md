---
title: إظهار إخفاء علامات التبويب في Jython
type: docs
weight: 50
url: /ar/java/display-hide-tabs-in-jython/
---

## **Aspose.Cells - عرض إخفاء علامات التبويب**
لإلحاق المستندات باستخدام **Aspose.Cells Java for Jython**. هنا يمكنك رؤية رمز المثال.

**رمز Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class DisplayHideTabs:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/DisplayHideTabs/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Hiding the tabs of the Excel file

        workbook.getSettings().setShowTabs(False)

        #Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Tabs are now hidden, please check the output file."

if __name__ == '__main__':        

    DisplayHideTabs()

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **مستندات الإضافة (Aspose.Cells)** من أي من المواقع الاجتماعية للترميز الواردة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/DisplayHideTabs.py)
