---
title: Kopiera rader och kolumner i Jython
type: docs
weight: 30
url: /sv/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells - Kopiera rader och kolumner**
 För att lägga till dokument med hjälp av**Aspose.Cells Java för Jython**. Här kan du se exempelkod.

**Jython Code**

{{< highlight "java" >}}

 från aspose-celler importera inställningar

från com.aspose.cells import arbetsbok

klass RowsAndColumns:

 def__i det__(själv):



dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # Kopiera rader

 self.copy_rows()

 # Kopiera kolumner

 self.copy_columns()



 def copy_rows(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Instantiera ett arbetsboksobjekt med excel-filsökväg

 arbetsbok = Arbetsbok(dataDir + 'Book1.xls')

 # Åtkomst till det första kalkylbladet i Excel-filen

 arbetsblad = workbook.getWorksheets().get(0)

 # Kopiera den andra raden med data, formatering, bilder och ritobjekt

 # till 12:e raden i arbetsbladet.

 workheet.getCells().copyRow(worksheet.getCells(),1,11)

 # Sparar den modifierade Excel-filen i standardformat (det vill säga Excel 2003).

 workbook.save(dataDir + "Copy Rows.xls")

 print "Kopiera rader framgångsrikt."



def copy_columns(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Instantiera ett arbetsboksobjekt med excel-filsökväg

 arbetsbok = Arbetsbok()

 # Åtkomst till det första kalkylbladet i Excel-filen

 arbetsblad = workbook.getWorksheets().get(0)

 # Lägg några data i rubrikrader (A1:A4)

 i = 0

 medan jag< 5:

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
## **Ladda ner Running Code**
 Ladda ner**Bifoga dokument (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
