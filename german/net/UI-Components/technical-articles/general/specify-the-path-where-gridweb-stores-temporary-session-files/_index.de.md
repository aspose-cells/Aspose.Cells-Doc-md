---
title: Geben Sie den Pfad an, in dem GridWeb temporäre Sitzungsdateien speichert
type: docs
weight: 50
url: /de/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

Wenn der GridWeb-Sitzungsmodus ViewState ist, speichert es seine temporären Sitzungsdateien im Application Base Directory. Manchmal ist es nicht in Ordnung, temporäre Sitzungsdateien dort zu speichern, da das Application Base Directory möglicherweise keine Schreibberechtigungen dafür hat. In solchen Fällen löst GridWeb eine solche Ausnahme aus

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

Die Lösung für das obige Problem besteht darin, Schreibzugriff auf das Basisverzeichnis der Anwendung zu gewähren oder den Pfad der temporären GridWeb-Sitzungsdateien mit Schreibzugriff mithilfe der GridWeb.SessionStorePath-Eigenschaft zu ändern. Dieser Pfad sollte relativ zum Application Base Directory sein.

{{% /alert %}} 
## **Geben Sie den Pfad an, in dem GridWeb temporäre Sitzungsdateien speichert**
Der folgende Beispielcode gibt den Pfad an, in dem GridWeb temporäre Sitzungsdateien speichert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
