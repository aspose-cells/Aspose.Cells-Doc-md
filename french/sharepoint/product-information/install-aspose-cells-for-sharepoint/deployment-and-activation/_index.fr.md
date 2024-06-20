---
title: Déploiement et Activation
type: docs
weight: 20
url: /fr/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[L'installation de Aspose.Cells for SharePoint](/cells/fr/sharepoint/installing-aspose-cells-for-sharepoint/) vous guide à travers le processus d'installation. Cet article explique le processus d'installation déployé et activé.

{{% /alert %}} 
### **Déploiement**
Aspose.Cells for SharePoint effectue les actions suivantes pendant le déploiement :

1. Installe **Aspose.Cells.SharePoint.dll** dans le Global Assembly Cache et ajoute une entrée SafeControl au fichier **web.config**.
1. Installe le manifeste de fonction et d'autres fichiers nécessaires dans les répertoires appropriés.
1. Enregistre la fonction dans la base de données SharePoint et la rend disponible pour l'activation au niveau de la fonction.
### **Activation**
Aspose.Cells for SharePoint est emballé en tant que fonctionnalité au niveau du site (collection de sites) et peut être activé et désactivé sur les collections de sites. 

Lors de l'activation, la fonctionnalité apporte quelques modifications au répertoire virtuel de l'application web parent de la collection de sites :

1. Ajoute une page de paramètres de conversion au fichier de plan du site.
1. Copie les fichiers de ressources nécessaires dans le dossier App_GlobalResources du répertoire virtuel.
