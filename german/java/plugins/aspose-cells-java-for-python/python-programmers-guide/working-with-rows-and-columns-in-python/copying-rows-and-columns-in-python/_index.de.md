---
title: Kopieren von Zeilen und Spalten in Python
type: docs
weight: 30
url: /de/java/copying-rows-and-columns-in-python/
---
## **Aspose.Cells – Kopieren von Zeilen und Spalten**
### **Zeilen kopieren**
Aspose.Cells stellt die Methode copyRow der Klasse Cells bereit. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln, Werte, Kommentare, Zellformate, ausgeblendete Zellen, Bilder und andere Zeichenobjekte aus der Quellzeile in die Zielzeile.

Die copyRow-Methode akzeptiert die folgenden Parameter:

- das Quellobjekt Cells,
- den Quellzeilenindex und
- der Zielzeilenindex.

**Python Code**

{{< highlight "java" >}}

 def copy_rows(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

\# Copy the second row with data, formattings, images and drawing objects

\# to the 12th row in the worksheet.

worksheet.getCells().copyRow(worksheet.getCells(),1,11)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Rows.xls")

print "Copy Rows Successfully." 

{{< /highlight >}}
### **Spalten kopieren**
Aspose.Cells stellt die Methode copyColumn der Klasse Cells bereit. Diese Methode kopiert alle Arten von Daten, einschließlich Formeln – mit aktualisierten Verweisen – und Werten, Kommentaren, Zellformaten, ausgeblendeten Zellen, Bildern und anderen Zeichnungsobjekten aus der Quellspalte in die Zielspalte.

Die copyColumn-Methode übernimmt die folgenden Parameter:

- das Quellobjekt Cells,
- Quellspaltenindex und
- der Zielspaltenindex.

**Python Code**

{{< highlight "ruby" >}}



def copy_columns(selbst):

\# Instanziieren eines Workbook-Objekts nach Excel-Dateipfad

Arbeitsmappe = self.Workbook()

\# Zugriff auf das erste Arbeitsblatt in der Excel-Datei

Arbeitsblatt = Arbeitsmappe.getWorksheets().get(0)

\# Einige Daten in Kopfzeilen einfügen (A1:A4)

ich = 0

 während ich< 5:

worksheet.getCells().get(i, 0).setValue("Header Row #i")





\# Put some detail data (A5:A999)

i = 5

while i < 1000:

worksheet.getCells().get(i, 0).setValue("Detail Row #i")


\# Create another Workbook.

workbook1 = Workbook()

\# Get the first worksheet in the book.

worksheet1 = workbook1.getWorksheets().get(0)

\# Copy the first column from the first worksheet of the first workbook into

\# the first worksheet of the second workbook.

worksheet1.getCells().copyColumn(worksheet.getCells(),0,2)

\# Autofit the column.

worksheet1.autoFitColumn(2)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Copy Columns.xls")

print "Copy Columns Successfully." 

{{< /highlight >}}
## **Laufcode herunterladen**
 Download**Zeilen und Spalten kopieren (Aspose.Cells)** von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
