---
title: Копирование строк и столбцов в Ruby
type: docs
weight: 30
url: /ru/java/copying-rows-and-columns-in-ruby/
---
## **Aspose.Cells - Копирование строк и столбцов**
### **Копирование строк**
Aspose.Cells предоставляет метод copyRow класса Cells. Этот метод копирует все типы данных, включая формулы, значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходной строки в целевую строку.

Метод copyRow принимает следующие параметры:

- исходный объект Cells,
- индекс исходной строки и
- индекс строки назначения.

**Рубиновый код**

{{< highlight "ruby" >}}

 def copy_rows()

    data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'



    # Instantiating a Workbook object by excel file path

    workbook = Rjb::import('com.aspose.cells.Workbook').new(data_dir + 'Book1.xls')

    # Accessing the first worksheet in the Excel file

    worksheet = workbook.getWorksheets().get(0)

    # Copy the second row with data, formattings, images and drawing objects

    # to the 12th row in the worksheet.

    worksheet.getCells().copyRow(worksheet.getCells(),1,11)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Rows.xls")

    puts "Copy Rows Successfully."

end

{{< /highlight >}}
### **Копирование столбцов**
Aspose.Cells предоставляет метод copyColumn класса Cells, этот метод копирует все типы данных, включая формулы — с обновленными ссылками — и значения, комментарии, форматы ячеек, скрытые ячейки, изображения и другие объекты рисования из исходного столбца в целевой столбец.

Метод copyColumn принимает следующие параметры:

- исходный объект Cells,
- индекс исходного столбца и
- индекс столбца назначения.

**Рубиновый код**

{{< highlight "ruby" >}}

 защита copy_columns()

данные_dir = File.dirname(File.dirname(File.dirname(__ФАЙЛ__))) + '/данные/'



# Создание экземпляра объекта Workbook по пути к файлу excel

книга = Rjb::import('com.aspose.cells.Workbook').новый

# Доступ к первому рабочему листу в файле Excel

рабочий лист = рабочая книга.getWorksheets (). получить (0)

# Поместите некоторые данные в строки заголовков (A1:A4)

я = 0

 в то время как я< 5

        worksheet.getCells().get(i, 0).setValue("Header Row #{i}")

        i +=1

    end

    # Put some detail data (A5:A999)

    i = 5

    while i < 1000

        worksheet.getCells().get(i, 0).setValue("Detail Row #{i}")

        i +=1

    end

    # Create another Workbook.

    workbook1 = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet in the book.

    worksheet1 = workbook1.getWorksheets().get(0)

    # Copy the first column from the first worksheet of the first workbook into

    # the first worksheet of the second workbook.

    worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

    # Autofit the column.

    worksheet1.autoFitColumn(2)

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(data_dir + "Copy Columns.xls")

    puts "Copy Columns Successfully."

end

{{< /highlight >}}
## **Скачать рабочий код**
Скачать**Копирование строк и столбцов (Aspose.Cells)**с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/rowsandcolumns.rb)
