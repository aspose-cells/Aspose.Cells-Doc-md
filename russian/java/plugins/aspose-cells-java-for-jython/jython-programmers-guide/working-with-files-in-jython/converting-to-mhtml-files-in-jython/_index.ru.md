---
title: Преобразование в файлы Mhtml на Jython
type: docs
weight: 20
url: /ru/java/converting-to-mhtml-files-in-jython/
---

## **Aspose.Cells - Преобразование в файлы Mhtml**
Для добавления документов с помощью **Aspose.Cells Java для Jython**. Здесь вы можете увидеть примерный код.

**Код Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import HtmlSaveOptions

from com.aspose.cells import SaveFormat


class ConvertingToMhtmlFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'



        saveFormat = SaveFormat

        #Specify the file path

        filePath = dataDir + "Book1.xlsx"

        #Specify the HTML saving options

        sv = HtmlSaveOptions(saveFormat.M_HTML)

        #Instantiate a workbook and open the template XLSX file

        wb = Workbook(filePath)

        #Save the MHT file

        wb.save(filePath + ".out.mht", sv)

        # Print message

        print "Excel to MHTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToMhtmlFiles()

{{< /highlight >}}
## **Скачать работающий код**
Загрузите **Append Documents (Aspose.Cells)** c любого из упомянутых ниже социальных сайтов для кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
