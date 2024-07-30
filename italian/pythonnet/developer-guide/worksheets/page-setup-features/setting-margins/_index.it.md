---
title: Impostazione dei margini
type: docs
weight: 20
url: /it/python-net/setting-margins/
description: In questo articolo, imparerai come impostare i margini di un foglio di lavoro di Excel utilizzando un codice di esempio. Imparerai inoltre come impostare programmaticamente i margini per il centro pagina, i margini dell intestazione e del piè di pagina della Configurazione Pagina utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, impostare margine del foglio di lavoro di Excel al centro, impostare il margine dell intestazione e del piè di pagina del foglio di lavoro usando Python.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET supporta pienamente le opzioni di impostazioni pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni della Configurazione Pagina per i fogli di lavoro per controllare il processo di stampa. Questo argomento discute come utilizzare Aspose.Cells per Python via .NET per configurare i margini di pagina.

{{% /alert %}}

## **Come impostare i margini**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file di Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene la collezione [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) che consente di accedere a ciascun foglio di lavoro nel file di Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce la proprietà [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) utilizzata per impostare le opzioni di configurazione della pagina per un foglio di lavoro. L'attributo [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) è un oggetto della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) che consente agli sviluppatori di impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. La classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) fornisce varie proprietà e metodi utilizzati per impostare le opzioni di configurazione della pagina.

## **Come impostare i margini di pagina**

Imposta i margini della pagina (sinistro, destro, superiore, inferiore) utilizzando i membri della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Di seguito sono elencati alcuni dei metodi utilizzati per specificare i margini della pagina:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Come centrare nella Pagina**

È possibile centrare qualcosa su una pagina orizzontalmente e verticalmente. A tal scopo, ci sono alcuni membri utili della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) e [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Come impostare i margini dell'intestazione e del piè di pagina**

Imposta i margini dell'intestazione e del piè di pagina con i membri della classe [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) come [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) e [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
