---
title: Spécifiez le chemin où GridWeb stocke les fichiers de session temporaires
type: docs
weight: 50
url: /fr/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

Lorsque le mode de session GridWeb est ViewState, il stocke ses fichiers de session temporaires dans le répertoire de base de l'application. Parfois, il n'est pas acceptable d'y stocker des fichiers de session temporaires, car le répertoire de base de l'application peut ne pas disposer d'autorisations d'écriture dessus. Dans de tels cas, GridWeb lève une telle exception

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

La solution au problème ci-dessus consiste à donner un accès en écriture au répertoire de base de l'application ou à modifier le chemin des fichiers de session temporaires GridWeb ayant un accès en écriture à l'aide de la propriété GridWeb.SessionStorePath. Ce chemin doit être relatif au répertoire de base de l'application.

{{% /alert %}} 
## **Spécifiez le chemin où GridWeb stocke les fichiers de session temporaires**
L'exemple de code suivant spécifie le chemin où GridWeb stocke les fichiers de session temporaires.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
