---
title: Impostazioni di protezione avanzata da Excel XP in poi
type: docs
weight: 30
url: /it/python-net/advanced-protection-settings-since-excel-xp/
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

Aspose.Cells per Python via .NET supporta tutte le impostazioni avanzate di protezione offerte da Excel XP o versioni successive.

### **Impostazioni di protezione avanzate utilizzando Excel XP e versioni successive**

Per visualizzare le impostazioni di protezione disponibili in Excel XP:

1. Dal menu **Strumenti**, seleziona **Protezione** seguito da **Proteggi foglio**. Verrà visualizzata una finestra di dialogo.

Per visualizzare le impostazioni di protezione disponibili in Excel 2016

1. Dal menu **File**, seleziona **Proteggi workbook** seguito da **Proteggi foglio attivo**.
1. Seleziona **Proteggi foglio** nel menu **Revisione**.

Seguendo i passaggi sopra menzionati verrà visualizzata una finestra di dialogo in cui è possibile consentire o limitare le funzionalità dei fogli di lavoro o applicare una password al foglio di lavoro.

### **Impostazioni di Protezione Avanzata usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET supporta tutte le impostazioni avanzate di protezione.

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce la proprietà [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) che viene utilizzata per applicare queste impostazioni avanzate di protezione. La proprietà [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) è infatti un oggetto della classe [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) che incapsula diverse proprietà booleane per disabilitare o abilitare restrizioni.

Di seguito è riportato un piccolo esempio di applicazione. Apre un file Excel e utilizza la maggior parte delle impostazioni avanzate di protezione supportate da Excel XP e versioni successive.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

Si prega di non chiamare il metodo [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) quando si utilizza la proprietà [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection). Inoltre, salvare il file nel formato Excel97To2003 o Xlsx perché le impostazioni avanzate di protezione sono supportate solo da Excel XP e versioni successive.

{{% /alert %}}

### **Problema di blocco delle celle**

Se si desidera impedire agli utenti di modificare le celle, le celle devono essere bloccate prima di applicare qualsiasi impostazione di protezione. In caso contrario, le celle possono essere modificate anche se il foglio di lavoro è protetto. In Microsoft Excel XP, le celle possono essere bloccate tramite la seguente finestra di dialogo:

|**Finestra di dialogo per bloccare le celle in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

È possibile bloccare le celle anche utilizzando l'API di Aspose.Cells per Python via .NET. Ogni cella può ricevere una formattazione [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) che contiene una proprietà booleana [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Imposta la proprietà [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) su **true** o **false** per bloccare o sbloccare la cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

