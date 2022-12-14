---
title: Applica stili a GridWeb
type: docs
weight: 20
url: /it/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ha il proprio aspetto predefinito ma è possibile modificarne l'aspetto. Aspose.Cells.GridWeb fornisce diverse proprietà per consentire agli sviluppatori di controllarne completamente l'aspetto. In questo argomento vengono illustrate alcune di queste proprietà.

{{% /alert %}} 
## **Applicazione di stili preimpostati o personalizzati a Aspose.Cells.GridWeb**
### **Stili preimpostati**
Per salvare gli sforzi degli sviluppatori, Aspose.Cells.GridWeb offre alcuni stili preimpostati. Basta selezionare uno stile dall'elenco per applicare lo stile.

|**Stili**|**Combinazione di colori**|
|:- |:- |
|Standard|D'argento|
|Colorato1|Rosa|
|Colorato2|Blu|
|Professionale1|Ciano|
|Professionale2|Di nuovo ciano|
|Tradizionale1|Scuro|
|Tradizionale2|Grigio|
|Costume|Personalizzato|
Quando viene selezionato uno stile particolare, cambia l'intero aspetto del controllo GridWeb. Gli sviluppatori possono selezionare uno stile preimpostato da applicare su Grid durante la fase di progettazione, ma questa attività può anche essere eseguita in fase di esecuzione utilizzando il flessibile API di Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells. Il controllo GridWeb è rappresentato dalla classe GridWeb.

{{% /alert %}} 

Per selezionare uno stile predefinito:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Selezionare uno stile preimpostato da applicare al controllo.

Il controllo GridWeb fornisce la proprietà PresetStyle a cui gli sviluppatori possono assegnare qualsiasi stile preimpostato desiderato.

 L'output del seguente frammento di codice è mostrato di seguito.

**Controllo GridWeb con lo stile Colorful1 applicato su di esso** 

![cose da fare:immagine_alt_testo](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Stile barra di intestazione**
Se dai un'occhiata al controllo GridWeb, noterai due barre di intestazione. Uno per le colonne (ovvero A, B, C, D ecc.) e l'altro per le righe (ovvero 1, 2, 3, 4 ecc.). Aspose.Cells.GridWeb consente agli sviluppatori di controllare l'aspetto di queste barre di intestazione. Gli sviluppatori possono impostare lo stile delle barre di intestazione in fase di progettazione o in fase di esecuzione.

{{% alert color="primary" %}} 

Il controllo GridWeb fornisce la proprietà HeaderBarStyle che applica uno stile a entrambe le barre di intestazione del controllo.

{{% /alert %}} 

 L'output del codice di esempio riportato di seguito è mostrato qui.

**Stile modificato della barra dell'intestazione** 

![cose da fare:immagine_alt_testo](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Stile barra delle schede**
 È possibile impostare lo stile della barra delle schede.

**Stili modificati delle barre delle schede attive e non attive** 

![cose da fare:immagine_alt_testo](apply-styles-to-gridweb_3.png)

Nella figura sopra, Sheet4 è la scheda attiva, quindi il suo aspetto è diverso dalle altre schede, come definito dal codice di esempio riportato di seguito.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **File di stile personalizzato riutilizzabile**
Aspose.Cells.GridWeb supporta anche la persistenza dell'aspetto o delle impostazioni di stile in un file. Dopo aver impostato tutte le proprietà di aspetto del controllo GridWeb, è possibile salvare queste proprietà o impostazioni in un file su disco. Questo approccio è molto utile per gli sviluppatori per risparmiare tempo e sforzi riutilizzando le loro vecchie configurazioni di stile da un file di stile invece di impostare tutte le proprietà di stile (o aspetto) del controllo una per una.
### **Salvataggio del file di stile**
Una volta terminata l'impostazione delle proprietà dello stile, è possibile salvare le impostazioni di configurazione dello stile sotto forma di un file XML (perché tale file Style è archiviato come file XML) chiamando il metodo SaveCustomStyleFile del controllo GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Il file di stile salvato è in formato XML, quindi gli sviluppatori possono anche modificare questo file con qualsiasi editor di testo, se lo desiderano.

{{% /alert %}} 
### **Caricamento del file di stile**
Per applicare le impostazioni di stile da un file di stile esistente al controllo GridWeb, gli sviluppatori possono impostare il percorso del file di stile sulla proprietà CustomStyleFileName del controllo. Ma, prima di farlo, è necessario impostare la proprietà PresetStyle del controllo su Custom. È perché quel file di stile contiene informazioni di stile personalizzate già definite da uno sviluppatore.

{{% alert color="primary" %}} 

È anche possibile caricare o salvare il file di stile utilizzando Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANTE: il caricamento del file di stile nel controllo GridWeb non influisce sulle impostazioni di formattazione delle celle del controllo.

{{% /alert %}} 
### **Formato standard del modello di stile XML**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
