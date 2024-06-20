---
title: Installation de Aspose.Cells for SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint est téléchargeable sous forme d'archive Aspose.Cells.SharePoint.zip. 

{{% /alert %}} 
### **Contenu de l'archive**
L'archive Aspose.Cells.SharePoint.zip contient :

- Aspose.Cells.SharePoint.wsp – Fichier de solution SharePoint. Aspose.Cells for SharePoint est emballé en tant que solution SharePoint pour faciliter le déploiement/rétraction et l'activation/désactivation de fonctionnalités sur la ferme de serveurs.
- Aspose_LicenseAgreement.rtf – Contrat de licence utilisateur final
- Aspose.Cells for SharePoint.pdf – Documentation utilisateur
- Aspose.Cells for SharePoint Documentation.chm – Documentation utilisateur avec référence à l'API publique
- setup.exe – Programme d'installation
- setup.exe.config – Fichier de configuration de l'installation

Le programme d'installation vérifie les conditions suivantes avant de procéder à l'installation :

- WSS 3.0, MOSS 2007 ou SharePoint 2010 est installé.
- L'utilisateur a l'autorisation d'installer des solutions SharePoint.
- La base de données SharePoint est en ligne.
- Le service d'administration WSS est démarré.
- Le service Timer WSS est démarré.

Le service d'administration WSS et le service de minuterie sont nécessaires car certaines actions de configuration dépendent d'une tâche de minuterie pour se propager à tous les serveurs de la ferme de serveurs. 
#### **Pour installer Aspose.Cells for SharePoint**
1. Décompressez le fichier zip Aspose.Cells.SharePoint sur le lecteur local du serveur MOSS 7.0 ou WSS 3.0.
1. Exécutez setup.exe et suivez les instructions à l'écran.

Le programme d'installation effectue les actions suivantes :

1. Vérifier les prérequis d'installation. L'installation ne se poursuivra pas si l'une des vérifications échoue. 

   **Vérification du système** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. Afficher le Contrat de licence utilisateur final. L'utilisateur doit accepter l'accord pour pouvoir continuer. 

   **Le CLUF** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. Afficher la boîte de dialogue de sélection de la cible de déploiement. L'utilisateur sélectionne les applications Web et les collections de sites où la fonctionnalité doit être activée. Voir la figure ci-dessous. 

   **Cibles de déploiement** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. Déployer la fonctionnalité dans la ferme de serveurs. 

   **Installation en cours** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Activer la fonctionnalité pour les collections de sites sélectionnées et configurer leurs applications Web parentes.
1. Afficher la liste des applications Web et des collections de sites où la fonctionnalité a été déployée et activée. 

   **Installation terminée** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
