---
title: تحويل ورقة العمل إلى SVG في جايثون
type: docs
weight: 40
url: /ar/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - تحويل ورقة العمل إلى SVG**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 من إعدادات استيراد الخلايا غير المقصودة

من com.aspose.cells import Workbook

من com.aspose.cells استيراد ImageFormat

من com.aspose.cells استيراد ImageOrPrintOptions

من com.aspose.cells استيراد شيتريندر

من com.aspose.cells استيراد SaveFormat



فئة ConvertingWorksheetToSVG:

 def__فيه__(الذات):

 dataDir = Settings.dataDir + 'WorkingWithFiles / ConvertingWorksheetToSVG /'



 saveFormat = SaveFormat

 المصنف = المصنف (dataDir + "Book1.xls")

 #Convert كل ورقة عمل إلى تنسيق svg في صفحة واحدة.

 imgOptions = ImageOrPrintOptions ()

 imgOptions.setSaveFormat (saveFormat.SVG)

 imgOptions.setOnePagePerSheet (صواب)

 # تحويل كل ورقة عمل إلى تنسيق svg

 sheetCount = workbook.getWorksheets (). getCount ()

 # من أجل (أنا = 0 ؛ أنا<sheetCount; i++)

        for i in range(sheetCount):



            sheet = workbook.getWorksheets().get(i)

            sr = SheetRender(sheet, imgOptions)

            pageCount = sr.getPageCount()

            #for (k = 0 k < pageCount k++)

            for k in range(pageCount):



                #Output the worksheet into Svg image format

                sr.toImage(k, dataDir + sheet.getName() + ".out.svg")





        # Print message

        print "Excel to SVG conversion completed successfully."



if __name__ == '__main__':        

    ConvertingWorksheetToSVG()

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
