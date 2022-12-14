---
title: Преобразование рабочего листа в SVG в Jython
type: docs
weight: 40
url: /ru/java/converting-worksheet-to-svg-in-jython/
---
## **Aspose.Cells - Преобразование рабочего листа в SVG**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 из настроек импорта aspose-cells

из com.aspose.cells импортировать книгу

из com.aspose.cells импортировать ImageFormat

из com.aspose.cells импортировать ImageOrPrintOptions

из com.aspose.cells импортировать SheetRender

из com.aspose.cells импортировать SaveFormat



класс ConvertingWorksheetToSVG:

 деф__в этом__(себя):

 dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingWorksheetToSVG/'



 saveFormat = СохранитьФормат

 рабочая книга = рабочая книга (каталог данных + "Book1.xls")

#Преобразуйте каждый рабочий лист в формат svg на одной странице.

 imgOptions = ImageOrPrintOptions()

 imgOptions.setSaveFormat(saveFormat.SVG)

 imgOptions.setOnePagePerSheet(Истина)

 # Преобразовать каждый рабочий лист в формат svg

 SheetCount = рабочая книга.getWorksheets().getCount()

 #для(я=0; я<sheetCount; i++)

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
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingWorksheetToSVG.py)
