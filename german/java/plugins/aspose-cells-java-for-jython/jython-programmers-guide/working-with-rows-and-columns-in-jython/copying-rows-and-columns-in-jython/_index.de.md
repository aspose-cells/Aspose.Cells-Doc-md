---
title: Kopieren von Zeilen und Spalten in Jython
type: docs
weight: 30
url: /de/java/copying-rows-and-columns-in-jython/
---
## **Aspose.Cells – Kopieren von Zeilen und Spalten**
 Zum Anhängen von Dokumenten mit**Aspose.Cells Java für Jython**. Hier sehen Sie Beispielcode.

**Jython-Code**

{{< highlight "java" >}}

 aus aspose-cells Importeinstellungen

aus com.aspose.cells import Workbook

Klasse RowsAndColumns:

 def__drin__(selbst):



 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns'



 # Zeilen kopieren

 self.copy_rows()

 # Spalten kopieren

 self.copy_columns()



 def copy_rows(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Instanziieren eines Workbook-Objekts nach Excel-Dateipfad

 Arbeitsmappe = Arbeitsmappe (dataDir + 'Book1.xls')

 # Zugriff auf das erste Arbeitsblatt in der Excel-Datei

 Arbeitsblatt = Arbeitsmappe.getWorksheets().get(0)

 # Kopieren Sie die zweite Zeile mit Daten, Formatierungen, Bildern und Zeichenobjekten

 # in die 12. Zeile im Arbeitsblatt.

 Arbeitsblatt.getCells().copyRow(Arbeitsblatt.getCells(),1,11)

 # Speichern der geänderten Excel-Datei im Standardformat (dh Excel 2003).

workbook.save(dataDir + "Zeilen kopieren.xls")

 print "Zeilen erfolgreich kopieren."



 def copy_columns(dataDir):

 dataDir = Settings.dataDir + 'WorkingWithRowsAndColumns/RowsAndColumns/'

 # Instanziieren eines Workbook-Objekts nach Excel-Dateipfad

 Arbeitsmappe = Arbeitsmappe()

 # Zugriff auf das erste Arbeitsblatt in der Excel-Datei

 Arbeitsblatt = Arbeitsmappe.getWorksheets().get(0)

 # Einige Daten in Kopfzeilen einfügen (A1:A4)

 ich = 0

 während ich< 5:

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
## **Laufcode herunterladen**
 Download**Dokumente anhängen (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithRowsAndColumns/RowsAndColumns.py)
