---
title: Formattare righe e colonne
linktitle: Righe e colonne
type: docs
weight: 100
url: /it/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells per Python via .NET può supportare la modifica dell altezza delle righe o della larghezza delle colonne, nonché l applicazione della formattazione sulle righe o colonne.
keywords: Libreria Python Excel, Imposta altezza riga e larghezza colonna in Python, Regola altezza riga e larghezza colonna in Python, Cambia altezza riga o larghezza colonna in Python, Formatta righe e colonne in Python, Come impostare altezza riga e larghezza colonna in Python.
---


{{% alert color="primary" %}}

Lavorando con i fogli e aggiungendo dati alle righe o colonne, potresti aver bisogno di modificare l'altezza delle righe o la larghezza delle colonne. A volte, l'applicazione della formattazione sulle righe o colonne significa che l'altezza o larghezza attuali devono essere modificate per mostrare i dati. Normalmente, gli utenti regolano le altezze delle righe e le larghezze delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Tuttavia, con Aspose.Cells per Python via .NET gli sviluppatori possono eseguire queste operazioni durante l'esecuzione del programma.

{{% /alert %}}

## **Lavorare con le righe**

### **Come regolare l'altezza della riga**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi in seguito in maggior dettaglio.

### **Come impostare l'altezza di una riga**

È possibile impostare l'altezza di una singola riga chiamando il metodo [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Il metodo [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) prende i seguenti parametri come segue:

- **riga**, l'indice della riga di cui stai modificando l'altezza.
- **altezza**, l'altezza della riga da applicare alla riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **Come impostare l'altezza di tutte le righe in un foglio di lavoro**

Se gli sviluppatori hanno bisogno di impostare la stessa altezza della riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando la proprietà [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**Esempio:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **Lavorare con colonne**

### **Come impostare la larghezza di una colonna**

Imposta la larghezza di una colonna chiamando il metodo [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Il metodo [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) prende i seguenti parametri:

- **colonna**, l'indice della colonna di cui stai cambiando la larghezza.
- **larghezza**, la larghezza di colonna desiderata.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **Come impostare la larghezza della colonna in pixel**

Imposta la larghezza di una colonna chiamando il metodo [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Il metodo [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) prende i seguenti parametri:

- **colonna**, l'indice della colonna di cui stai cambiando la larghezza.
- **pixel**, la larghezza di colonna desiderata in pixel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **Come impostare la larghezza di tutte le colonne in un foglio di lavoro**

Per impostare la stessa larghezza della colonna per tutte le colonne nel foglio di lavoro, utilizzare la proprietà [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **Argomenti avanzati**
- [Adatta automaticamente righe e colonne](/cells/it/python-net/autofit-rows-and-columns/)
- [Converti testo in colonne utilizzando Aspose.Cells](/cells/it/python-net/convert-text-to-columns-using-aspose-cells/)
- [Copia righe e colonne](/cells/it/python-net/copying-rows-and-columns/)
- [Elimina righe e colonne vuote in un foglio di lavoro](/cells/it/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [Raggruppa e scollega righe e colonne](/cells/it/python-net/grouping-and-ungrouping-rows-and-columns/)
- [Nascondi e mostra righe e colonne](/cells/it/python-net/hiding-and-showing-rows-and-columns/)
- [Inserisci o elimina righe in un foglio di lavoro di Excel](/cells/it/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Inserimento ed eliminazione di righe e colonne di un file di Excel](/cells/it/python-net/inserting-and-deleting-rows-and-columns/)
- [Rimuovere righe duplicate in un foglio di lavoro](/cells/it/python-net/remove-duplicate-rows-in-a-worksheet/)
- [Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro](/cells/it/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
