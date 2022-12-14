---
title: Копирование строк и столбцов в Jython
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Копирование строк и столбцов**
 Для добавления документов с помощью**Aspose.Cells Java для Jython**. Здесь вы можете увидеть пример кода.

**Код Jython**

{{< highlight "java" >}}

 из настроек импорта aspose-cells

из com.aspose.cells импортировать книгу

класс РовсандКолоннс:

 деф__в этом__(себя):



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # Копирование строк

 self.copy_rows()

 # Копирование столбцов

 self.copy_columns()



 защита copy_rows (каталог данных):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Создание экземпляра объекта Workbook по пути к файлу excel

 рабочая книга = рабочая книга (каталог данных + 'Book1.xls')

 # Доступ к первому рабочему листу в файле Excel

 рабочий лист = рабочая книга.getWorksheets (). получить (0)

 # Скопируйте вторую строку с данными, форматированием, изображениями и объектами рисования

 # до 12-й строки рабочего листа.

 рабочий лист.getCells().copyRow(worksheet.getCells(),1,11)

 # Сохранение измененного файла Excel в формате по умолчанию (то есть Excel 2003)

workbook.save (каталог данных + «Копировать строки.xls»)

 print "Скопировать строки успешно."



 def copy_columns (каталог данных):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Создание экземпляра объекта Workbook по пути к файлу excel

 рабочая книга = рабочая книга ()

 # Доступ к первому рабочему листу в файле Excel

 рабочий лист = рабочая книга.getWorksheets (). получить (0)

 # Поместите некоторые данные в строки заголовков (A1:A4)

 я = 0

 в то время как я< 5:

            worksheet.getCells().get(i, 0).setValue("Header Row #i")






        # Put some detail data (A5:A999)

        i = 5

        while i < 1000:

            worksheet.getCells().get(i, 0).setValue("Detail Row #i")



        # Create another Workbook.

        workbook1 = Workbook()

        # Get the first worksheet in the book.

        worksheet1 = workbook1.getWorksheets().get(0)

        # Copy the first column from the first worksheet of the first workbook into

        # the first worksheet of the second workbook.

        worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

        # Autofit the column.

        worksheet1.autoFitColumn(2)

        # Saving the modified Excel file in default (that is Excel 2003) format

        workbook.save(dataDir + "Copy Columns.xls")

        print "Copy Columns Successfully." 




if __name__ == '__main__':        

    RowsAndColumns()

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Добавить документы (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
