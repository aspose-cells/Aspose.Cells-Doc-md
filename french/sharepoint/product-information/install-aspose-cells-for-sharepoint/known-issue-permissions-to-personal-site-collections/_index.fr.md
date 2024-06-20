---
title: Problème connu  Autorisations pour les collections de sites personnels
type: docs
weight: 40
url: /fr/sharepoint/known-issue-permissions-to-personal-site-collections/
---

{{% alert color="primary" %}} 

SharePoint par défaut ne accorde pas les autorisations complètes pour gérer les sites personnels aux administrateurs du portail. C'est pourquoi l'activation et la désactivation sur une collection de sites personnels peut échouer lorsqu'elle est effectuée par les administrateurs du portail. Cela inclut l'activation et la désactivation pendant l'installation.

{{% /alert %}} 
### **Accorder l'autorisation aux sites personnels**
Lorsque ce problème se produit pendant l'installation, une UnauthorizedAccessException à Microsoft.SharePoint.SPFeature.Activate() est enregistrée dans le journal de trace de SharePoint. Lorsque la désactivation échoue dans le cadre de la désinstallation, une UnauthorizedAccessException est affichée sur le dernier écran d'installation pour les désactivations en échec.

Pour éviter ce problème, accordez aux administrateurs du portail la permission de gérer l'application Web MySite :

1. Accédez à **l'administration centrale de SharePoint** et sélectionnez l'onglet **Gestion des applications**.
1. Choisissez **Politique pour l'application Web** dans le groupe **Sécurité de l'application**.
1. Assurez-vous de sélectionner la bonne application Web pour votre “My Site” dans la liste de l'**Application Web** sur la droite.
1. Sélectionnez **Ajouter des utilisateurs** en haut à gauche.
1. Choisissez **Toutes les zones** par défaut sur l'écran **Ajouter des utilisateurs** et cliquez sur **Suivant**.
1. Ajoutez le(s) utilisateur(s) approprié(s) ou le groupe de l'annuaire actif que vous souhaitez avoir le contrôle sur votre application Web “My Site”.
1. Sélectionnez le niveau de contrôle. 

   **Ajout d'utilisateurs et définition du niveau de contrôle** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Cliquez sur **Terminer**.
