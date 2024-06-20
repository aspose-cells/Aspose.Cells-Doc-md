---
title: Gestire i Fogli di Lavoro
type: docs
weight: 10
url: /it/python-java/manage-worksheets/
---

Gestire i fogli di lavoro utilizzando Aspose.Cells for Python via Java è molto facile. In questo articolo, dimostreremo come aggiungere, accedere e rimuovere i fogli di lavoro utilizzando l'API di Aspose.Cells.
## **Aggiungere fogli di lavoro a un nuovo file Excel**
Per creare un nuovo foglio di lavoro, creare un oggetto della classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). La classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) rappresenta un file Excel. Quindi, utilizzando il metodo [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) della classe [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), vengono aggiunti nuovi fogli di lavoro al file Excel. Infine, per salvare il nuovo file Excel creato, chiamare il metodo [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) della classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Il seguente snippet di codice dimostra la creazione di un nuovo file Excel e l'aggiunta di un foglio di lavoro ad esso.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**
Aggiungere fogli di lavoro a un foglio di lavoro progettato è esattamente come aggiungere il foglio di lavoro a un nuovo file Excel. L'unica differenza è che anziché creare un nuovo file Excel, apriamo un file esistente mediante la classe [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Il seguente snippet di codice dimostra l'aggiunta di un foglio di lavoro a un foglio di lavoro progettato.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Accesso ai fogli di lavoro utilizzando il nome del foglio**
Dopo aver caricato un foglio di lavoro, gli sviluppatori possono accedere a qualsiasi foglio di lavoro utilizzando il suo indice o nome. Il seguente snippet di codice dimostra l'accesso a un foglio di lavoro utilizzando il suo nome.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Rimuovere i fogli di lavoro**
Ci possono essere momenti in cui alcuni fogli devono essere rimossi dal foglio di lavoro. Per questo, l'API fornisce il metodo [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). È possibile passare l'indice del foglio o il nome del foglio da rimuovere. Gli esempi seguenti illustrano la rimozione dei fogli di lavoro utilizzando l'indice del foglio e il nome del foglio.
### **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Rimozione dei fogli di lavoro utilizzando il nome del foglio**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
