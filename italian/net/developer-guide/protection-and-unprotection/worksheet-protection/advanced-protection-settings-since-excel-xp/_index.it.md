---
title: Impostazioni di protezione avanzata da Excel XP in poi
type: docs
weight: 30
url: /it/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Dalla release di Excel 2002 o XP, Microsoft ha aggiunto molte impostazioni di protezione avanzate.

{{% /alert %}}

## **Introduzione**

Queste impostazioni di protezione limitano o consentono agli utenti di:

- Eliminare righe o colonne.
- Modificare contenuti, oggetti o scenari.
- Formattare celle, righe o colonne.
- Inserire righe, colonne o collegamenti ipertestuali.
- Selezionare celle bloccate o sbloccate.
- Usare tabelle pivot e molto altro.

Aspose.Cells supporta tutte le impostazioni di protezione avanzate offerte da Excel XP o versioni successive.

### **Impostazioni di protezione avanzate utilizzando Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1. Dal menu **Strumenti**, seleziona **Protezione** seguito da **Proteggi foglio**. Verrà visualizzata una finestra di dialogo.

Per visualizzare le impostazioni di protezione disponibili in Excel 2016

1. Dal menu **File**, seleziona **Proteggi workbook** seguito da **Proteggi foglio attivo**.
1. Seleziona **Proteggi foglio** nel menu **Revisione**.

Seguendo i passaggi sopra menzionati verrà visualizzata una finestra di dialogo in cui è possibile consentire o limitare le funzionalità dei fogli di lavoro o applicare una password al foglio di lavoro.

### **Impostazioni di protezione avanzate utilizzando Aspose.Cells**

Aspose.Cells supporta tutte le impostazioni avanzate di protezione.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce la proprietà [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) che viene utilizzata per applicare queste impostazioni avanzate di protezione. La proprietà [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) è infatti un oggetto della classe [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) che incapsula diverse proprietà booleane per disabilitare o abilitare restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni avanzate di protezione supportate da Excel XP e versioni successive.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Si prega di non chiamare il metodo [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) quando si utilizza la proprietà [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). Inoltre, salvare il file nel formato Excel97To2003 o Xlsx perché le impostazioni avanzate di protezione sono supportate solo da Excel XP e versioni successive.

{{% /alert %}}

### **Problema di blocco delle celle**

Se si desidera impedire agli utenti di modificare le celle, le celle devono essere bloccate prima di applicare qualsiasi impostazione di protezione. In caso contrario, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la seguente finestra di dialogo:

|**Finestra di dialogo per bloccare le celle in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

È possibile bloccare le celle anche utilizzando l'API Aspose.Cells. Ogni cella può ottenere una formattazione che contiene una proprietà booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Impostare la proprietà [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) su **true** o **false** per bloccare o sbloccare la cella.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
