---
title: Загрузите и настройте Aspose.Cells в Jython
type: docs
weight: 10
url: /ru/java/download-and-configure-aspose-cells-in-jython/
---

## **Загрузка**

**Загрузить примеры с веб-сайтов для социального программирования**

Ниже приведены релизы запущенных примеров, доступные для скачивания на всех указанных ниже сайтах социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**Загрузить компонент Aspose.Cells for Java**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **Установка**

- Поместите загруженный файл Aspose.Cells for Java jar в каталог "lib".
- Замените "your-lib" на имя загруженного jar файла в файле _*init*_.py.

## **Использование**

Вы можете создать документ HelloWorld, используя следующий пример кода:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}
