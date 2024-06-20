---
title: Applicare stili a GridWeb
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, stile, stili
description: Questo articolo illustra come applicare o impostare uno stile in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ha il suo aspetto predefinito ma è possibile cambiarne l'aspetto. Aspose.Cells.GridWeb fornisce diverse proprietà per consentire agli sviluppatori di controllarne completamente l'aspetto. Questo argomento tratta alcune di quelle proprietà.

{{% /alert %}} 
## **Applicare stili predefiniti o personalizzati a Aspose.Cells.GridWeb**
### **Stili preimpostati**
Per risparmiare gli sforzi degli sviluppatori, Aspose.Cells.GridWeb offre alcuni stili preimpostati. Seleziona semplicemente uno stile dalla lista per applicarlo.

|**Stili**|**Schema colore**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Quando viene selezionato uno stile particolare, cambia l'aspetto completo del controllo GridWeb. Gli sviluppatori possono selezionare uno Stile predefinito da applicare al Grid durante il tempo di progettazione, ma questo compito può anche essere realizzato durante l'esecuzione utilizzando la flessibile API di Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Il controllo Aspose.Cells.GridWeb è rappresentato dalla classe GridWeb.

{{% /alert %}} 

Per selezionare uno stile predefinito:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un modulo web.
1. Selezionare uno stile predefinito da applicare al controllo.

Il controllo GridWeb fornisce la proprietà PresetStyle a cui gli sviluppatori possono assegnare qualsiasi stile predefinito desiderato.

L'output dell'estratto di codice seguente è mostrato di seguito. 

**Controllo GridWeb con lo stile Colorful1 applicato ad esso** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Stile della barra dell'intestazione**
Se dai un'occhiata al controllo GridWeb, noterai due barre degli header. Una per le colonne (quindi A, B, C, D ecc.) e l'altra per le righe (quindi 1, 2, 3, 4 ecc.). Aspose.Cells.GridWeb consente agli sviluppatori di controllare l'aspetto di queste barre degli header. Gli sviluppatori possono impostare lo stile delle barre degli header sia durante il design che a runtime.

{{% alert color="primary" %}} 

Il controllo GridWeb fornisce la proprietà HeaderBarStyle che applica uno stile a entrambe le barre dell'intestazione del controllo.

{{% /alert %}} 

L'output del codice di esempio qui sotto è mostrato qui. 

**Stile modificato della barra degli header** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Stile della barra delle schede**
E' possibile impostare lo stile della barra delle schede. 

**Stili modificati delle barre delle schede attive e non attive** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

Nella figura precedente, Sheet4 è la scheda attiva quindi il suo aspetto è diverso dalle altre schede, come definito nel codice di esempio qui sotto.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **File di Stile Personalizzato Riutilizzabile**
Aspose.Cells.GridWeb supporta anche il mantenimento delle sue impostazioni di aspetto o stile in un file. Quando hai impostato tutte le proprietà di aspetto del controllo GridWeb, è possibile salvare queste proprietà o impostazioni su un file disco. Questo approccio è molto utile per gli sviluppatori che desiderano risparmiare tempo ed sforzi riutilizzando le loro vecchie configurazioni di stile da un file di stile anziché impostare tutte le proprietà di stile (o aspetto) del controllo una per una.
### **Salvataggio del File di Stile**
Una volta finito di impostare le proprietà di stile, puoi salvare le impostazioni di configurazione dello stile sotto forma di file XML (è perché quel file di stile è memorizzato come un file XML) chiamando il metodo SaveCustomStyleFile sul controllo GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Il file di stile salvato è in formato XML quindi, gli sviluppatori possono anche modificare questo file con qualsiasi editor di testo, se lo desiderano.

{{% /alert %}} 
### **Caricamento del file di stile**
Per applicare le impostazioni di stile da un file di stile esistente al controllo GridWeb, gli sviluppatori possono impostare il percorso del file di stile alla proprietà CustomStyleFileName del controllo. Ma, prima di fare ciò è necessario impostare la proprietà PresetStyle del controllo su Personalizzato. Questo perché il file di stile contiene informazioni di stile personalizzato già definite da uno sviluppatore.

{{% alert color="primary" %}} 

E' anche possibile caricare o salvare un file di stile utilizzando Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: Il caricamento del file di stile nel controllo GridWeb non influisce sulle impostazioni di formattazione delle celle del controllo.

{{% /alert %}} 
### **Formato Standard del Modello di Stile XML**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
