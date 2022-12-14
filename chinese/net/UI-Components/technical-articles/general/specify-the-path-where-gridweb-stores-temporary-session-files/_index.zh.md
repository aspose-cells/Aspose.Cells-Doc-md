---
title: 指定 GridWeb 存放临时会话文件的路径
type: docs
weight: 50
url: /zh/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

当 GridWeb 会话模式为 ViewState 时，它将其临时会话文件存储在应用程序基目录中。有时，将临时会话文件存储在那里是不可行的，因为应用程序基目录可能没有对其的写权限。在这种情况下，GridWeb 会抛出这样的异常

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

上述问题的解决方案是使用 GridWeb.SessionStorePath 属性授予对应用程序基本目录的写入权限或更改具有写入权限的 GridWeb 临时会话文件路径。此路径应相对于应用程序基目录。

{{% /alert %}} 
## **指定 GridWeb 存放临时会话文件的路径**
以下示例代码指定了 GridWeb 存储临时会话文件的路径。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
