---
title: Utilisez vos propres icônes au lieu des icônes par défaut de GridWeb
type: docs
weight: 10
url: /fr/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, icône, icônes
description: Cet article décrit comment utiliser des icônes dans GridWeb.
---

{{% alert color="primary" %}} 

Parfois, vous voudrez peut-être utiliser vos propres icônes (images) au lieu des icônes par défaut du contrôle Aspose.Cells.GridWeb. Cet article explique comment faire cela.

{{% /alert %}} 

Les icônes par défaut du contrôle se trouvent dans le chemin d'URL "/acw_client/". Le chemin du fichier peut être : "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" par défaut. Vous trouverez des fichiers comme submit.gif, save.gif etc. dans ce dossier. Si vous souhaitez remplacer ces images par les vôtres, ajoutez une section de configuration au fichier web.config de votre application web.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Vous avez peut-être remarqué que cette configuration affecte uniquement le chemin des images du contrôle et n'affecte pas le chemin des scripts clients du contrôle. Par exemple, si vous exécutez votre page avec le contrôle GridWeb et consultez le fichier source dans le navigateur, vous pouvez constater que la propriété acw_client _ path de l'élément DIV de la grille indique toujours : "/votreApp/webform1.aspx/". Dans certains cas, vous devrez peut-être redéfinir le chemin des scripts clients. Pour forcer le contrôle à utiliser le chemin d'image redéfini comme chemin des scripts clients, ajoutez un autre paramètre de configuration dans la section appSettings
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Cette configuration n'aura d'effet que sur le contrôle sous licence.

{{% /alert %}}
