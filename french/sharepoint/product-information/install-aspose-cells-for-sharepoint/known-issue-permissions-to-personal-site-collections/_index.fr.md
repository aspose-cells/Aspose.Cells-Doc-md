---
title: Problème connu - Autorisations sur les collections de sites personnels
type: docs
weight: 40
url: /fr/sharepoint/known-issue-permissions-to-personal-site-collections/
---
{{% alert color="primary" %}} 

Par défaut, SharePoint n'accorde pas d'autorisations complètes pour gérer les sites personnels aux administrateurs du portail. C'est pourquoi l'activation et la désactivation sur une collection de sites personnels peuvent échouer lorsqu'elles sont effectuées par les administrateurs du portail. Cela inclut l'activation et la désactivation lors de la configuration.

{{% /alert %}} 
### **Accorder une autorisation aux sites personnels**
Lorsque ce problème se produit lors de l'installation, une exception UnauthorizedAccessException à Microsoft.SharePoint.SPFeature.Activate() est consignée dans le journal de suivi SharePoint. Lorsque la désactivation échoue dans le cadre de la désinstallation, une exception UnauthorizedAccessException s'affiche sur le dernier écran de configuration pour la ou les désactivations ayant échoué.

Pour éviter ce problème, accordez aux administrateurs du portail l'autorisation de gérer l'application Web MySite :

1.  Aller à**Administration centrale de SharePoint**et sélectionnez le**Gestion des applications** languette.
1.  Choisir**Politique pour les applications Web** sous le**Sécurité des applications** groupe.
1.  Assurez-vous de sélectionner la bonne application Web pour votre « Mon site » dans la**Application Web** liste à droite.
1.  Sélectionner**Ajouter des utilisateurs** en haut à gauche.
1.  Choisir**Toutes les zones** par défaut sur le**Ajouter des utilisateurs** écran et cliquez**Suivant**.
1. Ajoutez le ou les utilisateurs appropriés ou le groupe Active Directory que vous souhaitez contrôler sur votre application Web « Mon site ».
1.  Sélectionnez le niveau de contrôle.

   **Ajouter des utilisateurs et définir le niveau de contrôle** 

![tâche : image_autre_texte](known-issue-permissions-to-personal-site-collections_1.png)




1.  Cliquez sur**Finir**.
