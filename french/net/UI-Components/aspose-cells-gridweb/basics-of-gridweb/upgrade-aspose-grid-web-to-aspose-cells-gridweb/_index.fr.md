---
title: Mettre à niveau Aspose.Grid.Web vers Aspose.Cells.GridWeb
type: docs
weight: 30
url: /fr/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Pour faciliter la mise à niveau, nous maintenons un document décrivant les informations essentielles pour les utilisateurs existants, en particulier ceux qui ont utilisé l'ancien Aspose.Grid.Web et doivent effectuer une mise à niveau vers le Aspose.Cells.GridWeb fusionné.

 Il s'agit de brèves notes, et vous devriez pouvoir trouver plus d'informations en consultant les sections du[Guide du développeur](/cells/fr/net/developer-guide/).

{{% /alert %}}

## **Mise à niveau vers Aspose.Cells.GridWeb**

 Les utilisateurs de Aspose.Grid.Web peuvent rencontrer des problèmes lors de l'utilisation du nouveau Aspose.Cells.GridWeb lors de la mise à niveau vers celui-ci. Il est à noter que Aspose.Grid.Web a été renommé et fait désormais partie de Aspose.Cells, nous ne continuerons donc pas ni n'apporterons de modifications aux anciennes versions du contrôle.

Il n'est pas difficile de mettre à niveau vers le dernier composant Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

Il y a quelques changements dans le API car les classes avec les membres, les structures, les énumérations, etc. restent les mêmes. La plupart des modifications ont été apportées aux espaces de noms du contrôle et à d'autres balises ou attributs.

{{% /alert %}}

Voici la liste des espaces de noms et d'autres attributs/balises qui ont été modifiés :

1. L'espace de noms Aspose.Grid.Web a été renommé Aspose.Cells.GridWeb.
1. L'espace de noms Aspose.Grid.Web.Data a été renommé Aspose.Cells.GridWeb.Data.
1. L'espace de noms Aspose.Grid.Web.Design a été renommé Aspose.Cells.GridWeb.Design.
1. L'espace de noms Aspose.Grid.Formula a été renommé en Aspose.Cells.GridFormula, et avec les versions récentes du composant, ledit espace de noms a été complètement supprimé du public API.
1. La balise agw:GridWeb a été remplacée par acw:GridWeb au format aspx.
1. L'ancien chemin client Aspose.Grid.Web, agw_client, est passé à acw_client pour Aspose.Cells.GridWeb .
1.  Le paramètre de chemin client dans le fichier web.config, par exemple :

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 a changé pour

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
