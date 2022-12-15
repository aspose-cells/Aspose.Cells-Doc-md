---
title: Impostazione dei margini
type: docs
weight: 20
url: /it/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells supporta completamente le opzioni di impostazione della pagina di Microsoft Excel. Gli sviluppatori potrebbero dover configurare le impostazioni di configurazione della pagina per i fogli di lavoro per controllare il processo di stampa. Questo argomento illustra come utilizzare Aspose.Cells per configurare i margini della pagina.

{{% /alert %}}

## **Impostazione dei margini**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contiene il[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

 Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) proprietà utilizzata per impostare le opzioni di impostazione della pagina per un foglio di lavoro. Il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) l'attributo è un oggetto del[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) classe che consente agli sviluppatori di impostare diverse opzioni di layout di pagina per un foglio di lavoro stampato. Il[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)class fornisce varie proprietà e metodi utilizzati per impostare le opzioni di impostazione della pagina.

### **Margini della pagina**

 Impostare i margini della pagina (sinistra, destra, superiore, inferiore) utilizzando[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)membri della classe. Di seguito sono elencati alcuni dei metodi utilizzati per specificare i margini della pagina:

- [**Margine sinistro**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Margine destro**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Margine superiore**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Margine inferiore**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centra sulla pagina**

È possibile centrare qualcosa su una pagina orizzontalmente e verticalmente. Per questo, ci sono alcuni utili membri del[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) classe,[**CentroOrizzontalmente**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) e[**CentroVerticale**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Margini di intestazione e piè di pagina**

 Imposta i margini di intestazione e piè di pagina con il file[**Impostazione della pagina**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) membri della classe come[**IntestazioneMargine**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) e[**Piè di paginaMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
