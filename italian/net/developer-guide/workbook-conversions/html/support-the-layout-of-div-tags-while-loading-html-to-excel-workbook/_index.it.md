---
title: Supporto del layout dei tag DIV durante il caricamento dell HTML nel foglio di lavoro di Excel
type: docs
weight: 50
url: /it/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalmente, il layout dei tag div viene ignorato durante il caricamento dell'HTML in un oggetto foglio di lavoro di Excel. Tuttavia, se si desidera che il layout dei tag div non venga ignorato, si prega di impostare la proprietà [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) su **true**. Il valore predefinito di questa proprietà è **false**.

{{% /alert %}} 

Il codice di esempio seguente illustra l'uso della proprietà [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag). Si prega di scaricare il [logo Aspose](5115218.png) utilizzato all'interno dell'HTML di input e il [file di Excel di output](5115220.xlsx) generato dal codice.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
