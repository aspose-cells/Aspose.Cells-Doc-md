---
title: ASP.NET Oturum durumu modu SQL Server olan durumunda GridWeb in çalışması
type: docs
weight: 160
url: /tr/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
keywords: GridWeb, web oturum durumu, sqlserver, oturum durumu modu
description: Bu makale, web oturum durumu modu SQL Server olan GridWeb in nasıl yapılandırılacağını tanıtıyor.
---

## **Olası Kullanım Senaryoları**
Bu makale, ASP.NET Oturum durumu modu SQL Server olan GridWeb'in çalışmasını açıklar.
## **ASP.NET Oturum durumu modu SQL Server olan GridWeb'in çalışması**
Oturumları tutmak için SQL Server veya StateServer kullanmak istiyorsanız, GridWeb Oturum Modunu kullanın. GridWeb kontrolü artık verilerini SQL Server veya StateServer'a serileştirmeyi destekler.

GridWeb.SessionMode'u SessionMode.Session olarak ayarlayacaksınız ve aşağıdaki örnek Web.Config ayarlarını kullanacaksınız. Lütfen ihtiyaçlarınıza göre sessionState özniteliklerini değiştirin.
## **Örnek Web.Config Oturum Durumu Ayarları**
{{< highlight java >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referans Makale**
- [Farklı GridWeb Modlarını Etkinleştirme](/cells/tr/net/aspose-cells-gridweb/enable-different-gridweb-modes/)
