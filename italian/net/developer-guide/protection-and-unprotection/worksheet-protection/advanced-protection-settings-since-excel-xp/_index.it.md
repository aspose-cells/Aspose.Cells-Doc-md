---
title: Impostazioni di protezione avanzata da Excel XP
type: docs
weight: 30
url: /it/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Dal rilascio di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate.

{{% /alert %}}

## **introduzione**

Queste impostazioni di protezione limitano o consentono agli utenti di:

- Elimina righe o colonne.
- Modifica contenuti, oggetti o scenari.
- Formatta celle, righe o colonne.
- Inserisci righe, colonne o collegamenti ipertestuali.
- Seleziona le celle bloccate o sbloccate.
- Usa le tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni di protezione avanzate offerte da Excel XP o versioni successive.

### **Impostazioni di protezione avanzata tramite Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1.  Dal**Strumenti** menù, selezionare**Protezione** seguito da**Proteggi Foglio**. Verrà visualizzata una finestra di dialogo.

Per visualizzare le impostazioni di protezione disponibili in Excel 2016

1.  Dal**File** menù, selezionare**Proteggi la cartella di lavoro** seguito da**Proteggi foglio corrente**.
1.  Seleziona il**Proteggi Foglio** nel**Revisione** menù.

Seguendo i passaggi menzionati sopra verrà visualizzata una finestra di dialogo in cui è possibile consentire o limitare le funzionalità dei fogli di lavoro o applicare una password al foglio di lavoro.

### **Impostazioni di protezione avanzata utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni di protezione avanzate.

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

 Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la classe fornisce il[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) proprietà utilizzata per applicare queste impostazioni di protezione avanzate. Il[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la proprietà è infatti un oggetto del[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/protection)classe che incapsula diverse proprietà booleane per disabilitare o abilitare le restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni di protezione avanzate supportate da Excel XP e versioni successive.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 Si prega di non chiamare il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**Proteggere**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) metodo quando si utilizza il[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)proprietà. Inoltre, salvare il file in formato Excel97To2003 o Xlsx poiché le impostazioni di protezione avanzate sono supportate solo da Excel XP e versioni successive.

{{% /alert %}}

### **Cell Problema di blocco**

Se si desidera impedire agli utenti di modificare le celle, le celle devono essere bloccate prima che vengano applicate le impostazioni di protezione. In caso contrario, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la seguente finestra di dialogo:

|**Finestra di dialogo per bloccare le celle in Excel XP**|
|:- |
|![cose da fare:immagine_alt_testo](advanced-protection-settings-since-excel-xp_1.png)|

È possibile bloccare le celle anche utilizzando lo Aspose.Cells API. Ogni cella può ottenere[**Stile**](https://reference.aspose.com/cells/net/aspose.cells/style) formattazione che contiene una proprietà booleana,[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Impostare il[**È bloccato**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) proprietà a**VERO** o**falso** per bloccare o sbloccare la cella.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
