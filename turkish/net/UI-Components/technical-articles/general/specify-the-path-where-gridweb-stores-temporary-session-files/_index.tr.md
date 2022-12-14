---
title: GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtin
type: docs
weight: 50
url: /tr/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

GridWeb oturum modu ViewState olduğunda, geçici oturum dosyalarını Uygulama Temel Dizininde depolar. Bazen, Uygulama Temel Dizini üzerinde yazma izinleri olmayabileceğinden, geçici oturum dosyalarını burada depolamak uygun değildir. Bu gibi durumlarda, GridWeb böyle bir istisna atar.

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

Yukarıdaki sorunun çözümü, Uygulama Temel Dizinine yazma erişimi vermek veya GridWeb.SessionStorePath özelliğini kullanarak yazma erişimi olan GridWeb geçici oturum dosyalarının yolunu değiştirmektir. Bu yol, Uygulama Temel Dizinine göre olmalıdır.

{{% /alert %}} 
## **GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtin**
Aşağıdaki örnek kod, GridWeb'in geçici oturum dosyalarını depoladığı yolu belirtir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
