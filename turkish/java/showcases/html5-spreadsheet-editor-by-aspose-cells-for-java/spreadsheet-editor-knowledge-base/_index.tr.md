---
title: Elektronik Tablo Düzenleyici Bilgi Bankası
type: docs
weight: 30
url: /tr/java/spreadsheet-editor-knowledge-base/
---

## **Herhangi bir yere HTML5 Elektronik Tablo Düzenleyici Gömme**

HTML5 Elektronik Tablo Düzenleyici, internet üzerinden elektronik tabloları paylaşmak için herhangi bir web sitesine, bloga ve foruma gömülebilir. Bağımsız bir düzenleyici olarak gömülebilir veya bir elektronik tablo dosyasıyla yüklenebilir.

**Bağımsız düzenleyici olarak gömme**

Bağımsız bir düzenleyici olarak gömmek için HTML IFRAME etiketini web sitesine ekleyin. Örneğin:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Elektronik tablo ile gömme**

Gömülü bir düzenleyiciye bir elektronik tablo yüklemek için **url** parametresini kullanın. Örneğin:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
