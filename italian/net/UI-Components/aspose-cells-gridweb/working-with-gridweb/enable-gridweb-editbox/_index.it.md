---
title: Abilita la casella di modifica di GridWeb
type: docs
weight: 110
url: /it/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, casella di modifica, barra delle formule
description: Questo articolo illustra come lavorare con la barra delle formule o la casella di modifica in GridWeb.
---

{{% alert color="primary" %}} 

La casella di modifica di GridWeb (chiamata barra delle formule in Excel) è una barra degli strumenti che viene renderizzata nella parte superiore del controllo e può essere utilizzata per visualizzare o inserire valori o copiare dati/formule per la cella focalizzata. Mostra anche il nome della cella che si sta modificando. Dopo aver fatto clic sulla cornice o quando si inizia a scrivere dati o si digita un simbolo uguale (=), la casella di modifica verrà attivata.

{{% /alert %}} 
## **Impostazione della casella di modifica di Aspose.Cells.GridWeb**
Il controllo GridWeb fornisce la proprietà ShowCellEditBox a cui gli sviluppatori possono assegnare "True" per attivare la barra degli strumenti. Il valore predefinito dell'attributo è False. Quando si imposta il valore su "True", comparirà la casella di modifica nella parte superiore del controllo GridWeb.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Controllo GridWeb con casella di modifica** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Esempio**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
