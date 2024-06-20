---
title: Gestione dei fogli di lavoro in Ruby
type: docs
weight: 10
url: /it/java/managing-worksheets-in-ruby/
---

## **Aspose.Cells - Gestione dei fogli di lavoro**
### **Aggiungere fogli di lavoro a un nuovo file Excel**
Per aggiungere un foglio di lavoro a un nuovo file Excel usando **Aspose.Cells Java per Ruby**, basta chiamare il metodo **add_worksheet** del modulo **MangingWorksheets**.

**Codice Ruby**

{{< highlight ruby >}}

 def add_worksheet()

    # Instantiating a Workbook object

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book.out.xls")

    puts "Sheet added successfully."

end 

{{< /highlight >}}
### **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**
Il processo di aggiunta di fogli di lavoro a un foglio di calcolo designer è esattamente lo stesso dell'approccio sopra tranne che il file Excel è già creato e abbiamo bisogno di aprire prima quel file Excel prima di aggiungere il foglio di lavoro ad esso.

**Codice Ruby**

{{< highlight ruby >}}

 def add_worksheet_to_designer_spreadsheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Adding a new worksheet to the Workbook object

    worksheets = workbook.getWorksheets()

    sheet_index = worksheets.add()

    worksheet = worksheets.get(sheet_index)

    # Setting the name of the newly added worksheet

    worksheet.setName("My Worksheet")

    # Saving the modified Excel file in default (that is Excel 2003) format

    workbook.save(@data_dir + "book1.out.xls")

end  

{{< /highlight >}}
### **Accesso ai fogli di lavoro utilizzando il nome del foglio**
Per accedere al foglio di lavoro per nome foglio utilizzando **Aspose.Cells Java per Ruby**, basta chiamare il metodo **get_worksheet** del modulo **MangingWorksheets**.

**Codice Ruby**

{{< highlight ruby >}}

 def get_worksheet()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Accessing a worksheet using its sheet name

    worksheet = workbook.getWorksheets().get("Sheet1")

    puts worksheet.to_string

end

{{< /highlight >}}
### **Rimozione dei fogli di lavoro utilizzando il nome del foglio**
Per rimuovere il foglio di lavoro per nome foglio utilizzando **Aspose.Cells Java per Ruby**, basta chiamare il metodo **remove_worksheet_by_name** del modulo **MangingWorksheets**.

**Codice Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_name()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt("Sheet1")



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end


{{< /highlight >}}
### **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**
Per rimuovere il foglio di lavoro per indice foglio utilizzando **Aspose.Cells Java per Ruby**, basta chiamare il metodo **remove_worksheet_by_index** del modulo **MangingWorksheets**.

**Codice Ruby**

{{< highlight ruby >}}

 def remove_worksheet_by_index()

    # Creating a file stream containing the Excel file to be opened

    fstream = IO.sysopen(@data_dir + 'book1.xls', "w")

    # Instantiating a Workbook object with the stream

    workbook = Rjb::import('com.aspose.cells.Workbook').new(fstream)

    # Removing a worksheet using its sheet name

    workbook.getWorksheets().removeAt(0)



    # Saving the Excel file

    workbook.save(@data_dir + "book.out.xls")



    # Print Message

    puts "Sheet removed successfully."

end 

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Gestione dei fogli di lavoro (Aspose.Cells)** da uno qualsiasi dei siti di codici sociali menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/managingworksheets.rb)
