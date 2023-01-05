---
title: Utilisation de vos propres icônes au lieu des icônes par défaut de GridWeb
type: docs
weight: 10
url: /fr/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

Parfois, vous voudrez peut-être utiliser vos propres icônes (images) au lieu des icônes par défaut du contrôle Aspose.Cells.GridWeb. Cet article explique comment procéder.

{{% /alert %}} 

Les icônes par défaut du contrôle sont situées dans le chemin URL "/acw_client/". Le chemin du fichier peut être : "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" par défaut. Vous trouverez des fichiers comme submit.gif, save.gif etc. dans ce dossier. Si vous souhaitez remplacer ces images par les vôtres, ajoutez une section de configuration au fichier web.config de votre application Web.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Vous avez peut-être remarqué que cette configuration n'affecte que le chemin des images de contrôle et n'affecte pas le chemin des scripts client du contrôle. Par exemple, si vous exécutez votre page avec le contrôle GridWeb et vérifiez le fichier source dans le navigateur, vous pouvez constater que l'acw_ client_La propriété path de l'élément DIV de la grille indique toujours : "/yourApp/webform1.aspx/". Dans certains cas, vous devrez peut-être redéfinir le chemin du script client. Pour forcer le contrôle à utiliser le chemin de l'image redéfini comme chemin du script client, ajoutez un autre paramètre de configuration dans la section appSettings
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Cette configuration ne prendra effet qu'avec le contrôle sous licence.

{{% /alert %}}
