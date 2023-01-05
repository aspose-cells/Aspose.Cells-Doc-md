---
title: تنزيل وتهيئة Aspose.Cells في جايثون
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-cells-in-jython/
---
## **جارى التحميل**

**تنزيل أمثلة من مواقع الترميز الاجتماعي**

الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل على جميع مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose-Cells-Java-for-Jython)

**تنزيل Aspose.Cells for Java المكون**

- [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)

## **التثبيت**

- ضع ملف جرة Aspose.Cells for Java الذي تم تنزيله في دليل "lib".
- استبدل "your-lib" باسم ملف jar الذي تم تنزيله في ملف _ * init * _. py.

## **استخدام**

يمكنك إنشاء مستند HelloWorld باستخدام رمز المثال التالي:

{{< highlight "java" >}}

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
