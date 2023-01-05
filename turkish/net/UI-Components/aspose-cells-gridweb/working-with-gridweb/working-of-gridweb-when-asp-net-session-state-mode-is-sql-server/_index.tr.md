---
title: ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışması
type: docs
weight: 160
url: /tr/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/
---
## **Olası Kullanım Senaryoları**
Bu makalede, ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışması açıklanmaktadır.
## **ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışması**
Oturumları tutmak için SQL Server veya StateServer kullanmak istiyorsanız, GridWeb Oturum Modunu kullanın. GridWeb kontrolü artık verilerini SQL Server veya StateServer'a seri hale getirmeyi destekliyor.

GridWeb.SessionMode'u SessionMode.Session olarak ayarlayacak ve aşağıdaki örnek Web.Config ayarlarını kullanacaksınız. Lütfen sessionState özelliklerini ihtiyaçlarınıza göre değiştirin.
## **Örnek Web.Config Oturum Durumu Ayarları**
{{< highlight "java" >}}

 <sessionState mode="SQLServer" sqlConnectionString="Password=11111111;Persist Security Info=True;User ID=testuser;Data Source=WINSHA-PC\NASIRSQL" timeout="20"></sessionState>

{{< /highlight >}}
## **Referans Makalesi**
- [Farklı GridWeb Modlarını Etkinleştirin](/cells/tr/net/enable-different-gridweb-modes/)
