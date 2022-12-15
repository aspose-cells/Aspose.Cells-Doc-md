---
title: Gestione delle interruzioni di pagina in Php
type: docs
weight: 20
url: /it/java/managing-page-breaks-in-php/
---
## **Aspose.Cells - Gestione interruzioni di pagina**
### **Aggiunta di interruzioni di pagina**
 Per aggiungere interruzioni di pagina utilizzando**Aspose.Cells Giava for PHP** , chiamata**add_page_breaks** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight "php" >}}

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
 Per cancellare tutte le interruzioni di pagina utilizzando**Aspose.Cells Giava for PHP** , chiamata**cancella_tutte_le_interruzioni_di_pagina** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight "php" >}}

 $workbook->getWorksheets()->get(0)->getHorizontalPageBreaks()->clear();

$workbook->getWorksheets()->get(0)->getVerticalPageBreaks()->clear();

\# Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "Clear All Page Breaks.xls");

{{< /highlight >}}
### **Rimozione di un'interruzione di pagina specifica**
 Per rimuovere un'interruzione di pagina specifica utilizzando**Aspose.Cells Giava for PHP** , chiamata**remove_page_break** metodo di**interruzioni di pagina** modulo. Di seguito puoi vedere un esempio di codice.

**Codice PHP**

{{< highlight "php" >}}

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
Scarica**Gestione interruzioni di pagina (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ValueFeatures/ManagingPageBreaks.php)
