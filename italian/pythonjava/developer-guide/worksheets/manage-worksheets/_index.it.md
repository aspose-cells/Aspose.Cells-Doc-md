---
title: Gestisci fogli di lavoro
type: docs
weight: 10
url: /it/python-java/manage-worksheets/
---
Gestire i fogli di lavoro utilizzando Aspose.Cells for Python via Java è molto semplice. In questo articolo, dimostreremo l'aggiunta, l'accesso e la rimozione di fogli di lavoro utilizzando Aspose.Cells API.
## **Aggiunta di fogli di lavoro a un nuovo file Excel**
 Per creare una nuova cartella di lavoro, creare un oggetto del file[Cartella di lavoro](https://reference.aspose.com/cells/python/asposecells.api/Workbook) classe. Il[Cartella di lavoro](https://reference.aspose.com/cells/python/asposecells.api/Workbook) class rappresenta un file Excel. Quindi utilizzando il[Inserisci](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) metodo del[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , i nuovi fogli di lavoro vengono aggiunti al file Excel. Infine, per salvare il file Excel appena creato, chiama il file[Salva](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) metodo del[Cartella di lavoro](https://reference.aspose.com/cells/python/asposecells.api/Workbook)classe.

Il frammento di codice seguente illustra la creazione di un nuovo file Excel e l'aggiunta di un foglio di lavoro.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Aggiunta di fogli di lavoro a un foglio di calcolo di Designer**
L'aggiunta di fogli di lavoro a un foglio di calcolo del progettista equivale esattamente all'aggiunta del foglio di lavoro a un nuovo file Excel. L'unica differenza è che invece di creare un nuovo file Excel, apriamo un file esistente con l'estensione[Cartella di lavoro](https://reference.aspose.com/cells/python/asposecells.api/Workbook)classe.

Il seguente frammento di codice illustra l'aggiunta di un foglio di lavoro a un foglio di lavoro per designer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Accesso ai fogli di lavoro utilizzando il nome del foglio**
Dopo aver caricato una cartella di lavoro, gli sviluppatori possono accedere a qualsiasi foglio di lavoro utilizzando il relativo indice o nome. Il frammento di codice seguente illustra l'accesso a un foglio di lavoro usando il relativo nome.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Rimozione di fogli di lavoro**
Potrebbero esserci momenti in cui alcuni fogli si incontrano per essere rimossi dalla cartella di lavoro. Per questo, il API fornisce il[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) metodo. Puoi passare l'indice del foglio o il nome del foglio da rimuovere. Gli esempi seguenti illustrano la rimozione dei fogli di lavoro utilizzando l'indice del foglio e il nome del foglio.
### **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Rimozione di fogli di lavoro utilizzando il nome del foglio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
