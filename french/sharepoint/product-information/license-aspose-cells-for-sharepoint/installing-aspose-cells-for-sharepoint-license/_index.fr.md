---
title: Installation de Aspose.Cells pour la licence SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 Une fois que vous êtes satisfait de votre[évaluation](/cells/fr/sharepoint/evaluate-aspose-cells/), [acheter une licence](https://purchase.aspose.com/buy).

Avant d'acheter, assurez-vous de comprendre et d'accepter les conditions d'abonnement à la licence.

{{% /alert %}}

La licence vous est envoyée par e-mail lorsque la commande a été payée. La licence est une archive ZIP contenant un package de solution SharePoint standard.

La licence ZIP contient :

- **Aspose.Cells.SharePoint.License.wsp** – Fichier de package de solution SharePoint. La licence Aspose.Cells pour SharePoint est conditionnée en tant que solution SharePoint pour faciliter le déploiement et la rétraction dans la batterie de serveurs.
- **lisezmoi.txt** – Instructions d'installation de la licence. L'installation de la licence s'effectue depuis la console du serveur via le**stsadm.exe**. Les étapes requises pour installer la licence sont indiquées ci-dessous.

#### **Installation de la licence**

{{% alert color="primary" %}}

 Les chemins sont omis pour plus de clarté. Ajoutez le chemin réel à**stsadm.exe** et/ou le fichier de solution lors de l'exécution des étapes ci-dessous.

{{% /alert %}}

1. Exécutez stsadm pour ajouter la solution au magasin de solutions SharePoint :
 stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Déployez la solution sur tous les serveurs de la ferme :
stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Exécutez les travaux du minuteur d'administration pour terminer le déploiement immédiatement :
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Vous recevrez un avertissement lors de l'exécution de l'étape de déploiement si le service d'administration des services SharePoint Windows n'a pas été démarré.**Stsadm.exe** s'appuie sur ce service et sur le service du minuteur SharePoint Windows pour répliquer les données de la solution dans la batterie de serveurs. Si ces services ne s'exécutent pas sur votre batterie de serveurs, vous devrez peut-être déployer la licence séparément sur chaque serveur.

{{% /alert %}}
