---
title: Укажите путь, по которому GridWeb хранит временные файлы сеансов.
type: docs
weight: 50
url: /ru/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

Когда режим сеанса GridWeb — ViewState, он сохраняет свои временные файлы сеанса в базовом каталоге приложения. Иногда хранить там временные файлы сеансов недопустимо, поскольку базовый каталог приложений может не иметь прав на запись в него. В таких случаях GridWeb выдает такое исключение

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

Решение вышеуказанной проблемы состоит в том, чтобы предоставить доступ для записи к базовому каталогу приложений или изменить путь к файлам временных сеансов GridWeb с доступом для записи с помощью свойства GridWeb.SessionStorePath. Этот путь должен относиться к базовому каталогу приложений.

{{% /alert %}} 
## **Укажите путь, по которому GridWeb хранит временные файлы сеансов.**
В следующем примере кода указывается путь, по которому GridWeb хранит временные файлы сеансов.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
