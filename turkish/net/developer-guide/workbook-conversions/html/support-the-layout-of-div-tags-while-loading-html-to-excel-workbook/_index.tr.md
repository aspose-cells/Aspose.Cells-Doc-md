---
title: HTML yi elektronik tabloya yüklerken DIV etiketlerinin düzenini destekleyin
type: docs
weight: 50
url: /tr/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Normalde, bir HTML dosyasını bir elektronik tablo nesnesine yüklerken DIV etiketlerinin düzeni görmezden gelinir. Ancak, DIV etiketlerinin düzeninin görmezden gelinmemesini istiyorsanız, lütfen [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) özelliğini **true** olarak ayarlayın. Bu özelliğin varsayılan değeri **false**'dir.

{{% /alert %}} 

Aşağıdaki örnek kod, [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) özelliğini kullanımını göstermektedir. Lütfen, giriş HTML içinde kullanılan [Aspose Logosu](5115218.png) ve kod tarafından oluşturulan [çıktı excel dosyasını](5115220.xlsx) indirin.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
