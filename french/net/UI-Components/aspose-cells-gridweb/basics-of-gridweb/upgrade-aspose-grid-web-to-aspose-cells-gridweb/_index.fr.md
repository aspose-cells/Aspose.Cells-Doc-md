---
title: Mettre à niveau Aspose.Grid.Web vers Aspose.Cells.GridWeb
type: docs
weight: 30
url: /fr/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Cet article présente comment effectuer une mise à niveau dans GridWeb.
---

{{% alert color="primary" %}}

Pour faciliter la mise à niveau, nous tenons à jour un document décrivant les informations essentielles pour les utilisateurs existants, en particulier ceux qui ont utilisé l'ancien Aspose.Grid.Web et doivent passer à Aspose.Cells.GridWeb.

Il s'agit de notes succinctes et vous devriez pouvoir trouver plus d'informations en consultant les sections du [Guide du développeur](/cells/fr/net/aspose-cells-gridweb/developer-guide/).

{{% /alert %}}

## **Mise à niveau vers Aspose.Cells.GridWeb**

Les utilisateurs d'Aspose.Grid.Web peuvent rencontrer des problèmes lorsqu'ils passent à la nouvelle version d'Aspose.Cells.GridWeb. Il est à noter qu'Aspose.Grid.Web a été renommé et est devenu une partie d'Aspose.Cells, nous ne continuerons donc pas à apporter des modifications aux anciennes versions du contrôle. 

Il n'est pas difficile de passer à la dernière version du composant Aspose.Cells.GridWeb.

{{% alert color="primary" %}}

Il y a quelques changements dans l'API, les classes avec les membres, les structures, les énumérations, etc. restent les mêmes. La plupart des changements ont été apportés aux espaces de noms du contrôle et à d'autres balises ou attributs.

{{% /alert %}}

Ce qui suit est la liste des espaces de noms et autres attributs/balises qui ont été modifiés maintenant :

1. L'espace de noms Aspose.Grid.Web a été renommé Aspose.Cells.GridWeb.
1. L'espace de noms Aspose.Grid.Web.Data a été renommé Aspose.Cells.GridWeb.Data.
1. L'espace de noms Aspose.Grid.Web.Design a été renommé Aspose.Cells.GridWeb.Design.
1. L'espace de noms Aspose.Grid.Formula a été renommé Aspose.Cells.GridFormula et avec les versions récentes du composant, ledit espace de noms a été complètement supprimé de l'API publique.
1. La balise agw:GridWeb est devenue acw:GridWeb dans le formulaire aspx.
1. Le chemin client Aspose.Grid.Web, agw_client, a été modifié en acw_client pour Aspose.Cells.GridWeb.
1. Les paramètres du chemin client dans le fichier web.config, par exemple : 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

ont été changés en 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
