---
title: GridWeb Editör Kutusunu Etkinleştir
type: docs
weight: 110
url: /tr/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, editör kutusu, formül çubuğu
description: Bu makale, GridWeb de formül çubuğu veya düzenleme kutusu ile nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

GridWeb'in Düzenleme Kutusu (Excel'de formül çubuğu olarak adlandırılır), odaklanılan hücre için değer girişi veya kopyalama veri/formülü yapmak için kullanabileceğiniz, aynı zamanda düzenlemekte olduğunuz hücrenin adını gösteren bir araç çubuğudur. Kenara tıklayarak veya veri yazmaya başladığınızda veya eşittir (=) simgesi yazmaya başladığınızda Düzenleme Kutusu etkinleştirilecektir.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'in Düzenleme Kutusu'nun Ayarlanması**
GridWeb denetimi, geliştiricilerin toolbar'ı göstermek için ShowCellEditBox özelliğini "True" olarak atayabileceği bir özellik sağlar. Özniteliğin varsayılan değeri False'dur. Değerini "True" olarak ayarladığınızda, Düzenleme Kutusu GridWeb denetiminin üstünde görünecektir.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Düzen Kutusu ile GridWeb Denetimi** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **Örnek**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
