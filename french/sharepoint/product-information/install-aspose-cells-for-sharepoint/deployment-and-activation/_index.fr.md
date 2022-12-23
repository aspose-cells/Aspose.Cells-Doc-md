---
title: Déploiement et activation
type: docs
weight: 20
url: /fr/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[Installation Aspose.Cells for SharePoint](/cells/fr/sharepoint/installing-aspose-cells-for-sharepoint/) vous guide tout au long du processus d'installation. Cet article explique ce que le processus d'installation est déployé et activé.

{{% /alert %}} 
### **Déploiement**
Aspose.Cells for SharePoint effectue les actions suivantes lors du déploiement :

1.  Installations**Aspose.Cells.SharePoint.dll** dans le Global Assembly Cache et ajoute une entrée SafeControl au**web.config** dossier.
1. Installe le manifeste des fonctionnalités et les autres fichiers nécessaires dans les répertoires appropriés.
1. Enregistre la fonctionnalité dans la base de données SharePoint et la rend disponible pour activation au niveau de la fonctionnalité.
### **Activation**
 Aspose.Cells for SharePoint est présenté comme une fonctionnalité au niveau du site (collection de sites) et peut être activé et désactivé sur les collections de sites.

Lors de l'activation, la fonctionnalité apporte quelques modifications au répertoire virtuel de l'application Web parente de la collection de sites :

1. Ajoute la page des paramètres de conversion au fichier sitemap.
1. Copie les fichiers de ressources nécessaires dans le dossier App_GlobalResources du répertoire virtuel.
