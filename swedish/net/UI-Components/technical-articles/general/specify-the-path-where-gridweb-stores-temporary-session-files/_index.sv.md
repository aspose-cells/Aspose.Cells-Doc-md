---
title: Ange sökvägen där GridWeb lagrar temporära sessionsfiler
type: docs
weight: 50
url: /sv/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

När GridWeb-sessionsläget är ViewState, lagrar det sina temporära sessionsfiler i Application Base Directory. Ibland är det inte OK att lagra temporära sessionsfiler där eftersom Application Base Directory kanske inte har skrivbehörighet på den. I sådana fall gör GridWeb ett sådant undantag

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

Lösningen på ovanstående problem är att ge skrivåtkomst till Application Base Directory eller ändra sökvägen till GridWebs temporära sessionsfiler med skrivåtkomst med hjälp av egenskapen GridWeb.SessionStorePath. Den här sökvägen bör vara relativ till Application Base Directory.

{{% /alert %}} 
## **Ange sökvägen där GridWeb lagrar temporära sessionsfiler**
Följande exempelkod anger sökvägen där GridWeb lagrar temporära sessionsfiler.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
