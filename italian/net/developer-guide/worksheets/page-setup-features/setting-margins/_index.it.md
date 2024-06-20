---
title: Impostazione dei margini
type: docs
weight: 20
url: /it/net/setting-margins/
description: In questo articolo, imparerai come impostare i margini di un foglio di lavoro di Excel utilizzando un codice di esempio. Imparerai anche come impostare programmatticamente i margini per il centro della pagina, i margini dell intestazione e del piè di pagina di Imposta pagina utilizzando l API C# o la libreria .NET.
keywords: imposta il margine del foglio di lavoro di Excel al centro c#, imposta il margine dell intestazione e del piè di pagina del foglio di lavoro c#
---

{{% alert color="primary" %}}

Aspose.Cells supporta completamente le opzioni di impostazione della pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni del layout di pagina per controllare il processo di stampa dei fogli di lavoro. Questo argomento discute come utilizzare Aspose.Cells per configurare i margini di pagina.

{{% /alert %}}

## **Impostazione margini**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file di Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene la raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) che consente di accedere a ciascun foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce la proprietà [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) utilizzata per impostare le opzioni di configurazione della pagina per un foglio di lavoro. L'attributo [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) è un oggetto della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) che consente agli sviluppatori di impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. La classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) fornisce varie proprietà e metodi utilizzati per impostare le opzioni di configurazione della pagina.

### **Margini di Pagina**

Imposta i margini della pagina (sinistro, destro, superiore, inferiore) utilizzando i membri della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). Di seguito sono elencati alcuni dei metodi utilizzati per specificare i margini della pagina:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centra sulla Pagina**

È possibile centrare qualcosa su una pagina orizzontalmente e verticalmente. A tal scopo, ci sono alcuni membri utili della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) e [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Margini Intestazione e Piè di Pagina**

Imposta i margini dell'intestazione e del piè di pagina con i membri della classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) come [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) e [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
