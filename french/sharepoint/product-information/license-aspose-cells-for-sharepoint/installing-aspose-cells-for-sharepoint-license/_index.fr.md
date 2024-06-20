---
title: Installation de la licence Aspose.Cells for SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

Une fois que vous êtes satisfait de votre [évaluation](/cells/fr/sharepoint/evaluate-aspose-cells/), [achetez une licence](https://purchase.aspose.com/buy).

Avant d'acheter, assurez-vous de comprendre et d'accepter les termes de l'abonnement à la licence.

{{% /alert %}}

La licence vous est envoyée par e-mail lorsque la commande a été payée. La licence est une archive ZIP contenant un package de solution SharePoint régulier.

Le fichier ZIP de la licence contient :

- **Aspose.Cells.SharePoint.License.wsp** – Fichier de package de solution SharePoint. La licence Aspose.Cells for SharePoint est emballée en tant que solution SharePoint pour faciliter le déploiement et la rétractation sur l'ensemble du serveur.
- **readme.txt** – Instructions d'installation de la licence. L'installation de la licence s'effectue à partir de la console du serveur via **stsadm.exe**. Les étapes requises pour installer la licence sont données ci-dessous.

#### **Installation de la licence**

{{% alert color="primary" %}}

Les chemins sont omis pour plus de clarté. Ajoutez le chemin réel vers **stsadm.exe** et/ou le fichier de solution lors de l'exécution des étapes ci-dessous.

{{% /alert %}}

1. Exécutez stsadm pour ajouter la solution au magasin de solutions SharePoint :
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Déployez la solution sur tous les serveurs de la ferme :
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Exécutez les travaux d'administration pour terminer immédiatement le déploiement :
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Vous recevrez un avertissement lors de l'exécution de l'étape de déploiement si le service d'administration de Windows SharePoint Services n'a pas été démarré. **Stsadm.exe** repose sur ce service et le service de minuterie Windows SharePoint pour répliquer les données des solutions sur l'ensemble de la ferme. Si ces services ne sont pas en cours d'exécution sur votre ferme de serveurs, vous devrez peut-être déployer la licence séparément sur chaque serveur.

{{% /alert %}}
