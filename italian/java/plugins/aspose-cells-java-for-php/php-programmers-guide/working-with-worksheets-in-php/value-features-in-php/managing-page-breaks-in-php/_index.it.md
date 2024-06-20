---
title: Gestione degli interruzioni di pagina in Php
type: docs
weight: 20
url: /it/java/managing-page-breaks-in-php/
---

## **Aspose.Cells - Gestisci interruzioni di pagina**
### **Aggiunta dei salti di pagina**
Per aggiungere interruzioni di pagina utilizzando **Aspose.Cells Java per PHP**, chiamare il metodo **add_page_breaks** del modulo **pagebreaks**. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->add("Y30");

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->add("Y30");

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Add Page Breaks.xls");   

{{< /highlight >}}
### **Cancellazione di tutte le interruzioni di pagina**
Per cancellare tutte le interruzioni di pagina utilizzando **Aspose.Cells Java per PHP**, chiamare il metodo **clear_all_page_breaks** del modulo **pagebreaks**. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight php >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Rimuovere interruzione di pagina specifica**
Per rimuovere una specifica interruzione di pagina utilizzando **Aspose.Cells Java per PHP**, chiamare il metodo **remove_page_break** del modulo **pagebreaks**. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight php >}}

 $worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

$h_page_breaks = $worksheet->getHorizontalPageBreaks();

$h_page_breaks->removeAt(0);

$v_page_breaks = $worksheet->getVerticalPageBreaks();

$v_page_breaks->removeAt(0);

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Remove Page Break.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica **Gestione Interruzioni di Pagina (Aspose.Cells)** da uno dei siti di codice sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
